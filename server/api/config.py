import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
DATABASE_NAME = os.getenv("DATABASE_NAME", "postman")
DATABASE_PORT = os.getenv("DATABASE_PORT", "3306")
