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
    ID: int
    sleep_score: int
    wakeup_score: int
    lifestyle_sensitivity: int
    cleaning_score: int
    cleaning_sensitivity: int
    indoor_food_score: int
    indoor_food_sensitivity: int
    smoking_score: int
    indoor_study_score: int
    indoor_study_sensitivity: int
    indoor_noise_score: int
    indoor_noise_sensitivity: int
    alarm_score: int
    alarm_sensitivity: int
    late_study_score: int
    late_study_sensitivity: int
    sleeping_habit_score: int
    sleeping_habit_sensitivity: int
    intimacy_score: int
    overnight_score: int
    overnight_sensitivity: int
    hot_or_cold: int
    summer_or_winter: int
class UpdatingData(BaseModel):
    ID: int
class WishlistData(BaseModel):
    ID: int
    wishID: int
class MatchingData(BaseModel):
    ID: int
    matchingID: int
class StateData(BaseModel):
    ID: int
    state: bool

# 308관 남자 추천 API 엔드포인트: /8m_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.post('/8m_rec')
def man_308_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "man_308_dataset.json")
    return response

# 309관 남자 추천 API 엔드포인트: /9m_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.post('/9m_rec')
def man_309_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "man_309_dataset.json")
    return response

# 308관 여자 추천 API 엔드포인트: /8w_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.post('/8w_rec')
def man_308_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "man_308_dataset.json")
    return response

# 309관 여자 추천 API 엔드포인트: /9w_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.post('/9w_rec')
def man_309_recommendation(data: UserData):
    data = jsonable_encoder(data)
    response = main.main(data, "man_309_dataset.json")
    return response

# 추천 리스트 업데이트 API 엔드포인트: /up_rec
# input: {"ID": int}
# output: {"IDs": [int, int, ...]}
@app.post('/up_rec')
def update_recommendation(data: UpdatingData):
    data = jsonable_encoder(data)
    response = main.main(data, "update")
    return response

# 찜 목록 업데이트 API 엔드포인트 : /wish_up
# input: {"ID": int, "wishID": int}
# output: {}
@app.post('/wish_up')
def wishlist_update(data: WishlistData):
    data = jsonable_encoder(data)
    func.update_wishlist(data)
    return Response(content=None, status_code=200)

# 매칭 데이터 업데이트 API 엔드포인트 : /real_data_up
# input: {"ID": int, "matchingID": int}
# output: {}
@app.post('/mdata_up')
def real_matching_data_update(data: MatchingData):
    data = jsonable_encoder(data)
    func.update_matching_data(data)
    return Response(content=None, status_code=200)

# 룸메이트 구하는 상태 업데이트 API 엔드포인트 : /state_up
# input: {"ID": int, "state": bool}
# output: {}
@app.post('/state_up')
def seeking_state_update(data: StateData):
    data = jsonable_encoder(data)
    func.update_state_data(data)
    return Response(content=None, status_code=200)

# 서버 실행 코드
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)
    #uvicorn appController:app --reload