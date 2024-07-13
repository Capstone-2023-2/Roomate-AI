import main
import functions as func
from pydantic import BaseModel
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UserData(BaseModel):
    userId: str
    bedtimeScore: int
    wakeupScore: int
    wakeupSensitivity: int
    cleaningScore: int
    cleaningSensitivity: int
    foodScore: int
    foodSensitivity: int
    cigaretteScore: int
    studyScore: int
    studySensitivity: int
    notebookScore: int
    notebookSensitivity: int
    alarmScore: int
    alarmSensitivity: int
    latestudyScore: int
    latestudySensitivity: int
    snoringScore: int
    snoringSensitivity: int
    friendlyScore: int
    inhomeScore: int
    inhomeSensitivity: int
    coldOrHot: int
    summerOrWinter: int
class UpdatingData(BaseModel):
    userId: str
class WishlistData(BaseModel):
    userId: str
    wishId: str
class MatchingData(BaseModel):
    userId: str
    matchingId: str
class StateData(BaseModel):
    userId: str
    state: bool

# 308관 남자 추천 API 엔드포인트: /8m_rec
# input: {"ID": str, "_score": int, "_sensitivity": int, ...}
# output: {"ID1": str, "ID2": str, ...}
@app.post('/8m_rec')
def man_308_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "man_308_dataset.json")
    return response

# 309관 남자 추천 API 엔드포인트: /9m_rec
# input: {"ID": str, "_score": int, "_sensitivity": int, ...}
# output: {"ID1": str, "ID2": str, ...}
@app.post('/9m_rec')
def man_309_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "man_309_dataset.json")
    return response

# 308관 여자 추천 API 엔드포인트: /8w_rec
# input: {"ID": str, "_score": int, "_sensitivity": int, ...}
# output: {"ID1": str, "ID2": str, ...}
@app.post('/8w_rec')
def woman_308_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "woman_308_dataset.json")
    return response

# 309관 여자 추천 API 엔드포인트: /9w_rec
# input: {"ID": str, "_score": int, "_sensitivity": int, ...}
# output: {"ID1": str, "ID2": str, ...}
@app.post('/9w_rec')
def woman_309_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "woman_309_dataset.json")
    return response

# 추천 리스트 업데이트 API 엔드포인트: /up_rec
# input: {"ID": str}
# output: {"similarity1": float, "similarity2": float, ...}
@app.post('/percent')
def measure_recommendation(data: UpdatingData):
    data = jsonable_encoder(data)
    response = main.main(data, "percent")
    return response

# 추천 리스트 업데이트 API 엔드포인트: /up_rec
# input: {"ID": str}
# output: {"ID1": str, "ID2": str, ...}
@app.post('/up_rec')
def update_recommendation(data: UpdatingData):
    data = jsonable_encoder(data)
    response = main.main(data, "update")
    return response

# 찜 목록 업데이트 API 엔드포인트 : /wish_up
# input: {"ID": str, "wishID": str}
# output: {}
@app.post('/wish_up')
def wishlist_update(data: WishlistData):
    data = jsonable_encoder(data)
    func.update_wishlist(data)
    return Response(content=None, status_code=200)

# 매칭 데이터 업데이트 API 엔드포인트 : /real_data_up
# input: {"ID": str, "matchingID": str}
# output: {}
@app.post('/mdata_up')
def real_matching_data_update(data: MatchingData):
    data = jsonable_encoder(data)
    func.update_matching_data(data)
    return Response(content=None, status_code=200)

# 룸메이트 구하는 상태 업데이트 API 엔드포인트 : /state_up
# input: {"ID": str, "state": bool}
# output: {}
@app.post('/state_up')
def seeking_state_update(data: StateData):
    data = jsonable_encoder(data)
    func.update_state_data(data)
    return Response(content=None, status_code=200)

# 테스트용 API 엔드포인트 : /hello
@app.get('/hello')
def hello():
    return {"message": "Hello World!"}

# 서버 실행 명령어 (localhost:8080)
# uvicorn appController:app --host=localhost --port=8080 --reload