import uvicorn
from fastapi import FastAPI, HTTPException, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
  id: int | None = None
  name: str
  email: str | None = None


collection = {
  1: User(name='Lila'),
  2: User(name='Stas', email='email@liame.ru'),
  '_3': User(name='Pan')
}


@app.get('/users/', response_class=HTMLResponse)
async def users(request: Request):
  return templates.TemplateResponse("users.html", {"request": request, "users": __active_users()})


@app.get('/users/{id}', response_model=User)
async def user(id: int):
  if id in collection:
    return collection[id]
  raise HTTPException(status_code=404, detail="User not found")


@app.post('/users/', response_model=User)
async def create_user(request: Request, name: str = Form(), email: str = Form()):
  collection[len(collection) + 1] = User(name=name, email=email)
  return templates.TemplateResponse("users.html", {"request": request, "users": __active_users()})


@app.put('/users/{id}', response_model=User)
def update_user(id: int, user: User):
  if id in collection:
    collection[id] = user
    return user
  raise HTTPException(status_code=404, detail="User not found")


@app.delete('/users/{id}', response_model=dict)
async def destroy_users(id: int):
  if id in collection:
    collection[f'_{id}'] = collection[id]
    del collection[id]
    return {'message': 'Destroy was successfully'}
  raise HTTPException(status_code=404, detail="User not found")


def __active_users():
  active_users = []

  for id, user in collection.items():
    if isinstance(id, int):
      user.id = id
      active_users.append(user)

  return active_users


if __name__ == '__main__':
  uvicorn.run(
    "main:app",
    host="127.0.0.1",
    port=8000,
    reload=True
  )
