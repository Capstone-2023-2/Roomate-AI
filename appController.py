from flask import Flask, request, jsonify
import main
import functions as func

app = Flask(__name__)

# 308관 남자 추천 API 엔드포인트: /8m_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.route('/8m_rec', methods=['POST'])
def man_308_recommendation():
    if request.method == 'POST':
        data = request.get_json()
        response = main.main(data, "man_308_dataset.json")
        return response

# 309관 남자 추천 API 엔드포인트: /9m_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.route('/9m_rec', methods=['POST'])
def man_309_recommendation():
    if request.method == 'POST':
        data = request.get_json()
        response = main.main(data, "man_309_dataset.json")
        return response

# 308관 여자 추천 API 엔드포인트: /8w_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.route('/8w_rec', methods=['POST'])
def woman_308_recommendation():
    if request.method == 'POST':
        data = request.get_json()
        response = main.main(data, "woman_308_dataset.json")
        return response

# 309관 여자 추천 API 엔드포인트: /9w_rec
# input: {"ID": int, "_score": int, "_sensitivity": int, ...}
# output: {"IDs": [int, int, ...]}
@app.route('/9w_rec', methods=['POST'])
def woman_309_recommendation():
    if request.method == 'POST':
        data = request.get_json()
        response = main.main(data, "woman_309_dataset.json")
        return response
    
# 추천 리스트 업데이트 API 엔드포인트: /up_rec
# input: {"ID": int}
# output: {"IDs": [int, int, ...]}
@app.route('/up_rec', methods=['POST'])
def update_recommendation():
    if request.method == 'POST':
        data = request.get_json()
        response = main.main(data, "update")
        return response

# 찜 목록 업데이트 API 엔드포인트 : /wish_up
# input: {"ID": int, "wishID": int}
# output: {}
@app.route('/wish_up', methods=['POST'])
def wishlist_update():
    if request.method == 'POST':
        data = request.get_json()
        func.update_wishlist(data)
        response = jsonify({"result": "Success"}), 200
        return response

# 매칭 데이터 업데이트 API 엔드포인트 : /real_data_up
# input: {"ID": int, "matchingID": int}
# output: {}
@app.route('/mdata_up', methods=['POST'])
def real_matching_data_update():
    if request.method == 'POST':
        data = request.get_json()
        func.update_matching_data(data)
        response = jsonify({"result": "Success"}), 200
        return response

# 룸메이트 구하는 상태 업데이트 API 엔드포인트 : /state_up
# input: {"ID": int, "state": bool}
# output: {}
@app.route('/state_up', methods=['POST'])
def seeking_state_update():
    if request.method == 'POST':
        data = request.get_json()
        func.update_state_data(data)
        response = jsonify({"result": "Success"}), 200
        return response

# 서버 실행 코드
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)