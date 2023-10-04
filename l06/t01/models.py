from pydantic import BaseModel, Field
from datetime import date


class UserIn(BaseModel):
  name: str = Field(..., min_length=2)
  surname: str = Field(..., min_length=2)
  email: str = Field(..., max_length=128)
  password: str = Field(..., min_length=6)
class User(UserIn):
  id: int


class ProductIn(BaseModel):
  title: str = Field(..., min_length=3)
  price: float = Field(..., gt=0)
class Product(ProductIn):
  id: int


class OrderIn(BaseModel):
  user_id: int = Field(...)
  product_id: int = Field(...)
  on: date = Field(..., format="%Y-%m-%d")
  state: int = Field(None)
class Order(OrderIn):
  id: int
