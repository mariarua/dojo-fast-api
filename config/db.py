from sqlalchemy import create_engine, MetaData
from .settings import Settings

set = Settings()
engine = create_engine(set.url_database)
meta = MetaData()
conn = engine.connect()