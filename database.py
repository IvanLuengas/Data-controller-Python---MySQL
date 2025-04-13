from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve database credentials from environment variables
DB_USER  = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("BD_NAME")

# Construct the database connection URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# Create the SQLAlchemy engine, which is the entry point to the database
engine = create_engine(DATABASE_URL, echo=True)  # echo=True will log SQL statements
# Create a base for declarative models, which will be used to define database tables as Python classes
base = declarative_base()

# Define the 'user' model, which maps to the 'user_a' table in the database
class user(base):
    __tablename__ = 'user_a'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

 # Constructor for the 'user' class
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create all the tables defined in the declarative base in the database
base.metadata.create_all(engine)

# Create a sessionmaker, which is a factory for creating database sessions
session = sessionmaker(bind=engine)
# Create an active database session
sessionActive = session()