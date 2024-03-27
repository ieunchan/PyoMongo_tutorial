from pymongo import MongoClient
from crud import create_mongodb
client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')
# 데이터베이스 선택 (없으면 새로 생성됨)
db = client['tutorial_db_eunchan']
# 컬렉션 선택 (없으면 새로 생성됨)
collection = db['tutorial_collection_eunchan']

