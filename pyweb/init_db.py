from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mysql_url = "mysql+pymysql://root:rootroot@sangwon-rds-test.cwmns3xrahu0.ap-northeast-2.rds.amazonaws.com/test"
engine = create_engine(mysql_url, echo=True, convert_unicode=True)

db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()

def init_database():
    Base.metadata.create_all(bind=engine)