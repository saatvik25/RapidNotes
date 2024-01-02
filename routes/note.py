from fastapi import APIRouter
# APIRouter is a tool that helps organize and structure your API routes. It allows you to define endpoints, handle HTTP requests, and manage different parts of your API in a modular way.

# ye par notes ke sare logic hoga routes weghra
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from typing import Union
from pymongo import MongoClient
# import connection
from config.db import conn
from schemas.note import noteEntity, notesEntity
from models.note import Note

note = APIRouter()

# now we want our static,teplates file to be served
templates = Jinja2Templates(directory="templates")
# to make connection with mongodb


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Insert a sample document into the "notes" collection
    # conn.Notes.notes.insert_one({"key": "value"})

    docs = conn.Notes.notes.find({})
    newdocs=[]
    for doc in docs:
        # print(i["_id"])
        newdocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc": doc["desc"],
            # "important": doc["important"],
        })
    # print(docs)
    return templates.TemplateResponse("index.html", {"request": request, "newdocs": newdocs})

# @note.post("/")
# def add_note(note: Note):
#     inserted_note = conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)

@note.post("/")
async def create_item(request:Request):
    form = await request.form()
    formdict = dict(form)
    formdict["important"] = True if formdict.get("important") == "on" else False
    note = conn.Notes.notes.insert_one(dict(formdict))
    return{"Sucess":True}