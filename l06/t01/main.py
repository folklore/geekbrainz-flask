import uvicorn
from db import database
from fastapi import FastAPI

import users, products, orders


app = FastAPI()


@app.on_event("startup")
async def startup():
  await database.connect()


@app.on_event("shutdown")
async def shutdown():
  await database.disconnect()


@app.get("/")
async def home():
  return {"Home": "Home"}


app.include_router(users.router, tags=["users"])
app.include_router(products.router, tags=["products"])
app.include_router(orders.router, tags=["orders"])
  

if __name__ == '__main__':
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
