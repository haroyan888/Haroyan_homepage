from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 接続先データベースの設定
DATABASE = "sqlite:///instance/database.sqlite3"

#Engineの作成
engine = create_engine(DATABASE, echo=False)
base = declarative_base()

class Test(base) :
    __tablename__ = 'Test'
    id = Column(Integer, primary_key=True)
    sentence = Column(String(1000))

    def to_dict(self):
        test = {
            'id':self.id,
            'sentence':self.sentence
        }
        return test

def create_database():
    base.metadata.create_all(bind=engine)

def create_session():
    return sessionmaker(bind=engine)()

if __name__=="__main__":
    create_database()