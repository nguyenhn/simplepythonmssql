from typing import Optional

from fastapi import FastAPI

from os import getenv

import pymssql  

app = FastAPI()


@app.get("/")
def read_root():
    server = getenv("DB_SERVER")
    usr = getenv("DB_USER")
    pwd = getenv("DB_USER_PASSWORD")
    try:
        conn = pymssql.connect(server=server, user=usr, password=pwd, database='master')
        return {'Conneted'}
    except Exception as e:
        return {f'Connection failed dues to: {e}'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}