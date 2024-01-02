# https://fastapi.tiangolo.com/tutorial/first-steps/
# this is above website to gat base code

from fastapi import FastAPI
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
# # now we want our static,teplates file to be served
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")
# # to make connection with mongodb
# conn = MongoClient("mongodb+srv://saatvik:saatvik@mongoyoutube.voxlzff.mongodb.net")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.get("/items/{item_id}")
# # agar srt hai to theek nahi to none
# def read_item(item_id : int,q: Union[str,None]=None):
#     return {"item id":item_id,"q":q}
# https://fastapi.tiangolo.com/advanced/templates/
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     # Insert a sample document into the "notes" collection
#     # conn.Notes.notes.insert_one({"key": "value"})
#
#     docs = conn.Notes.notes.find({})
#     newdocs=[]
#     for i in docs:
#         # print(i["_id"])
#         newdocs.append({
#             "id":i["_id"],
#             "note":i["note"]
#         })
#     # print(docs)
#     return templates.TemplateResponse("index.html", {"request": request, "newdocs":newdocs})







