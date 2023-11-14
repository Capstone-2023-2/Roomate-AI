import functions as func
import clustering as clus
from flask import jsonify


# 추천 알고리즘 실행 함수
def main(u_data, f_name):
    
    if f_name == "update":
        u_id = u_data["ID"]
        u_data, f_name = func.get_userdata_whichfile(u_id)
         
    if not func.check_data(f_name):
        result = jsonify({"error": "Not enough users"}), 400
        return result
    
    func.add_user(u_data, f_name)
    clus.clustering(u_data, f_name)
    
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
    # 성향 점수가 평균적인 사람: test1
    test1 = main({"ID":201,"sleep_score":3,"wakeup_score":3,"lifestyle_sensitivity":2,"cleaning_score":2,"cleaning_sensitivity":2,"indoor_food_score":2,"indoor_food_sensitivity":2,"smoking_score":3,"indoor_study_score":2,"indoor_study_sensitivity":2,"indoor_noise_score":2,"indoor_noise_sensitivity":2,"alarm_score":2,"alarm_sensitivity":2,"late_study_score":3,"late_study_sensitivity":2,"sleeping_habit_score":2,"sleeping_habit_sensitivity":2,"intimacy_score":1,"overnight_score":2,"overnight_sensitivity":2,"hot_or_cold":2,"summer_or_winter":1}, "man_308_dataset.json")
    # 성향 점수가 좋은 사람: test2
    test2 = main({"ID":202,"sleep_score":3,"wakeup_score":3,"lifestyle_sensitivity":1,"cleaning_score":3,"cleaning_sensitivity":1,"indoor_food_score":3,"indoor_food_sensitivity":1,"smoking_score":3,"indoor_study_score":3,"indoor_study_sensitivity":1,"indoor_noise_score":3,"indoor_noise_sensitivity":1,"alarm_score":3,"alarm_sensitivity":1,"late_study_score":3,"late_study_sensitivity":1,"sleeping_habit_score":3,"sleeping_habit_sensitivity":1,"intimacy_score":1,"overnight_score":3,"overnight_sensitivity":1,"hot_or_cold":0,"summer_or_winter":1}, "man_308_dataset.json")
    # 성향 점수가 나쁜 사람: test3
    test3 = main({"ID":203,"sleep_score":5,"wakeup_score":5,"lifestyle_sensitivity":3,"cleaning_score":1,"cleaning_sensitivity":3,"indoor_food_score":1,"indoor_food_sensitivity":3,"smoking_score":1,"indoor_study_score":1,"indoor_study_sensitivity":3,"indoor_noise_score":1,"indoor_noise_sensitivity":3,"alarm_score":1,"alarm_sensitivity":3,"late_study_score":1,"late_study_sensitivity":3,"sleeping_habit_score":1,"sleeping_habit_sensitivity":3,"intimacy_score":3,"overnight_score":1,"overnight_sensitivity":3,"hot_or_cold":2,"summer_or_winter":3}, "man_308_dataset.json")
    print(test1)
    print(test2)
    print(test3)