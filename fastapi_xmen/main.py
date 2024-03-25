from typing import Union
from enum import Enum

from fastapi import FastAPI

from pydantic import BaseModel

xmen_api = FastAPI()

@xmen_api.get("/")
async def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
#Creating an Enum class
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@xmen_api.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#Order Matters -- make sure to add endpoints in the order they may be accessed
@xmen_api.get('/users/me')
async def read_user_me():
    return {"user_id": "the current user" }

@xmen_api.get("/users/{user_id}")
async def read_user_(user_id: str):
    return {"user_id": user_id }

@xmen_api.put("/items/item_id")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@xmen_api.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    
    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

# If we need to grab a file based on a path
@xmen_api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@xmen_api.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit] # produces this: http://127.0.0.1:8000/items/?skip=0&limit=10

# Optional Parameters
@xmen_api.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id }

# Query paramerter type conversion
@xmen_api.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({q:q})
    if not short: 
        item.update({"description": "This is an amazing item that has a description"})
    return item

# multipe path and query parameters
@xmen_api.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id:str, q:str | None = None, short:bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({q:q})
        
    if not short:
        item.update({"description": "text"})
    return item



