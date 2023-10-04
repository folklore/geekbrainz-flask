from settings import settings
import databases
import sqlalchemy as alchemy
import enum


DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = alchemy.MetaData()

users = alchemy.Table(
  "users",
  metadata,
  alchemy.Column("id", alchemy.Integer, primary_key=True),
  alchemy.Column("name", alchemy.String(32)),
  alchemy.Column("surname", alchemy.String(128)),
  alchemy.Column("email", alchemy.String(128)),
  alchemy.Column("password", alchemy.String(128)),
)

products = alchemy.Table(
  "products",
  metadata,
  alchemy.Column("id", alchemy.Integer, primary_key=True),
  alchemy.Column("title", alchemy.String(512)),
  alchemy.Column("price", alchemy.Float, alchemy.CheckConstraint('price > 0')),
)

class OrderState(enum.Enum):
  pending = 1
  completed = 2
  shipped = 3
  cancelled = 4

orders = alchemy.Table(
  "orders",
  metadata,
  alchemy.Column("id", alchemy.Integer, primary_key=True),
  alchemy.Column("user_id", alchemy.Integer, alchemy.ForeignKey("users.id")),
  alchemy.Column("product_id", alchemy.Integer, alchemy.ForeignKey("products.id")),
  alchemy.Column("on", alchemy.Date, default=alchemy.text('NOW()')),
  alchemy.Column("state", alchemy.Enum(OrderState), default=1),
)

engine = alchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
