from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Request
from app.util_constant import Constant

app = FastAPI()

@app.get(Constant.ROOT_PATH+"/health/liveness")
def health_liveness( request: Request):
    return {"status": "OK"}

@app.get(Constant.ROOT_PATH+"/greeting")
def greeting( request: Request):
    return {
        "greeting":"Hello World Python",
        "hostname":"http://127.0.0.1:8000",
        "version":"v1",
        "domain": request.base_url
    }

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Person(BaseModel):
    person_id: int
    name: str

@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name.title(), "item_id": item_id}


@app.get("/person/{person_id}")
def read_items(person_id: int, q: Union[str, None] = None):
    try:
        assert person_id == 1234, "Not found!"
        person = Person(person_id=person_id, name="Mr.Fast")
        print(person.model_dump())
        return person
    except AssertionError as error:
        print(error)
        return error
