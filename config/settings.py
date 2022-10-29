from pydantic import BaseSettings

class Settings(BaseSettings):
    #"postgresql://postgres_user:postgres_password@localhost:5432/store_db"
    url_database: str = "postgresql://postgres:aAXqrvPcibNkmZ7z@db.ekldcsdbjdxuzybnbvys.supabase.co:5432/postgres"