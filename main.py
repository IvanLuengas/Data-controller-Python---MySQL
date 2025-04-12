from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER  = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("BD_NAME")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
base = declarative_base()

class user(base):
    __tablename__ = 'user_a'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
sessionActive = session()

try:
    name = input("Give me your name: ")
    age = int(input("Give me your age: "))
    new_user = user(name, age)
    sessionActive.add(new_user)
    sessionActive.commit()
    print("✅ Usuario insertado correctamente.")

except Exception as e:
    sessionActive.rollback()
    print("❌ Error al insertar usuario:", e)

finally:
    sessionActive.close()