from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, FileResponse, StreamingResponse
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
app = FastAPI()

class Article(BaseModel):
    #id:Optional[int] = None
    id:int
    name:str
    price:int
class ArticleAdd(BaseModel):
    #id:Optional[int] = None
    id:int
    #name:str = Field(min_length=3, max_length=10, default="Artciculo")
    name:str = Field(min_length=3, max_length=10)
    price:int = Field(gt=0)
    model_config = {
        "json_schema_extra": {
            'example': {
                "id": 1,
                "name": "Articulo",
                "price": 1000
            }
        }
    }
    @field_validator("name")
    def validate_name(cls, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if len(value) > 10:
            raise ValueError("Name must be at most 10 characters long")
        return value

    #gt greater than
    #ge greater than or equal
    #lt less than
    #le less than or equal
class Articleupdate(BaseModel):
    name:str
    price:int
    
articles: List[Article]=[]
@app.get("/articles", tags=["Articles"])
def get_articles() -> List[Article]:
    #return [art.model_dump() for art in articles] #JSONResponse
    content = [art.model_dump() for art in articles]
    return JSONResponse(content=content)

@app.get("/articles/{id}", tags=["Articles"])
def get_article(id:int=Path(gt=0))->Article:
    for art in articles:
        if art["id"] == id:
            return art.model_dump()
    return {"data": "Not found"}
@app.get("/articles/", tags=["Articles"])
def get_articles_by_name(name:str=Query(min_length=3, max_length=10))->Article:
    for art in articles:
        if art["name"] == name:
            return art
    return {"data": "Not found"}

@app.post("/articles", tags=["Articles"])
def add_article(article:ArticleAdd)->List[Article]:
    articles.append(article)
    #return [article.model_dump() for article in articles]
    return RedirectResponse(url="/about", status_code=303)
@app.put("/articles/{id}", tags=["Articles"])
def update_article(id:int,article:Articleupdate)->List[Article]:
    for art in articles:
        if art["id"] == id:
            art["name"] = article.name
            art["price"] = article.price
            return articles
    return {"data": "Not found"}
@app.delete("/articles/{id}", tags=["Articles"])
def delete_article(id:int)->List[Article]:
    for art in articles:
        if art["id"] == id:
            articles.remove(art)
            return articles
    return {"data": "Not found"}

movies=[{
    "id":1,
    "title":"The Matrix",   
    "year":1999
},{
    "id":2,
    "title":"The Matrix 2",   
    "year":2000
}]
productos=[{
    "id":1,
    "name":"iPhone",
    "price":1000
},{
    "id":2,
    "name":"iPhone 2",
    "price":2000
},{
    "id":3,
    "name":"iPhone 3",
    "price":3000
}]
@app.get("/", tags=["Home"])
def home():
    return {"message": "Hello World"}
@app.get("/about", tags=["About"])
def about():
    return {"message": "This is About Page"}
@app.get("/contact", tags=["Contact"])
def contact():
    return HTMLResponse("<h1>This is Contact Page</h1>")
@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies
@app.get("/products", tags=["Products"])
def products():
    return products
#path params
@app.get("/products/{id}", tags=["Products"])
def get_product(id:int):
    for product in productos:
        if product["id"] == id:
            return product
    return {"data": "Not found"}
#query params
@app.get("/products/", tags=["Products"])
def get_products_by_title(name:str,price:int):
    for product in productos:
        if product["name"] == name:
            return product
    return {"data": "Not found"}
#METODO post
@app.post("/movies", tags=["Movies"])
def add_movie(id:int=Body(),
              title:str=Body(),
              year:int=Body()):
    movien={
        "id":id,
        "title":title,
        "year":year
    }
    movies.append(movien)
    return movies
#METODO put
@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id:int,
                 title:str=Body(),
                 year:int=Body()):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["year"] = year
            return movies
    return {"data": "Not found"}
#METODO delete
@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id:int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return movies
    return {"data": "Not found"}

@app.get("/getfile")
async def getfile():
    return FileResponse("1-SS-plan-de-actividades.pdf", media_type='application/pdf', filename='plan-de-actividades.pdf')

@app.get("/getstream")
async def getstream():
    file_path = "1-SS-plan-de-actividades.pdf"
    return StreamingResponse(
            open(file_path, mode="rb"), 
            media_type='application/pdf', 
            headers={"Content-Disposition": "attachment; filename=plan-de-actividades.pdf"}
        )
