import functions as func
from flask import jsonify


# 추천 알고리즘 실행 함수
def main(u_data, f_name):
    
    if f_name == "update":
        u_id = u_data["ID"]
        u_data, f_name = func.get_userdata_whichfile(u_id)
         
    if not func.check_data(f_name):
        result = jsonify({"error": "Not enough users"}), 400
        return result
       
    basic = func.basic_recommend(u_data, f_name)
    basic = func.check_seeking_state(basic)
    wish = func.wishlist_filtering_recommend(u_data, f_name)
    wish = func.check_seeking_state(wish)
    real = func.result_filtering_recommend(u_data, f_name)
    real = func.check_seeking_state(real)
    total = func.check_recommended_data(u_data, basic, wish, real)
    
    func.update_recommended_data(u_data, total)
    
    result = "{'userIDs': " + str(total) + "}"           

    return result

# 정상 실행 확인용 코드
if __name__ == '__main__':
    print(main({"ID": 201, "sleep_score": 5, "wakeup_score": 2, "pattern_sensitivity": 1, "cleaning_score": 3, "cleaning_sensitivity": 3, "food_score": 1, "food_sensitivity": 3, "cigarette_score": 1, "study_score": 2, "study_sensitivity": 3, "noise_score": 1, "noise_sensitivity": 1, "alarm_score": 3, "alarm_sensitivity": 1, "latenoise_score": 3, "latenoise_sensitivity": 3, "snoring_score": 1, "snoring_sensitivity": 3, "outsider_score": 1, "overnight_score": 2, "overnight_sensitivity": 3, "cold_or_hot": 2, "summer_or_winter": 1}, "man_308_dataset.json"))