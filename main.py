import functions as func
import clustering as clus
from fastapi import Response


# 추천 알고리즘 실행 함수
def main(u_data, f_name):
    
    if f_name == "percent":
        u_id = u_data["userId"]
        recommended_ids = func.get_recommended_data(u_data)
        recommended_ids.append(u_id)
        temp = func.measure_similarities(u_id, recommended_ids)
        result = {}
        result["sensitivity1"] = temp[0]
        result["sensitivity2"] = temp[1]
        result["sensitivity3"] = temp[2]
        result["sensitivity4"] = temp[3]
        result["sensitivity5"] = temp[4]
        result["sensitivity6"] = temp[5]
        return result
    
    elif f_name == "update":
        u_id = u_data["userId"]
        u_data, f_name = func.get_userdata_whichfile(u_id)
    
    if not func.check_data(f_name):
        return Response(content=None, status_code=400)
    
    func.add_user(u_data, f_name)
    #clus.clustering(u_data, f_name)
    
    basic = func.basic_recommend(u_data, f_name)
    basic = func.check_seeking_state(basic)
    wish = func.wishlist_filtering_recommend(u_data, f_name)
    wish = func.check_seeking_state(wish)
    real = func.result_filtering_recommend(u_data, f_name)
    real = func.check_seeking_state(real)
    total = func.check_recommended_data(u_data, basic, wish, real)
    func.update_recommended_data(u_data, total)
    
    result = {}
    result["userId1"] = total[0]
    result["userId2"] = total[1]
    result["userId3"] = total[2]
    result["userId4"] = total[3]
    result["userId5"] = total[4]
    result["userId6"] = total[5]

    return result

# 정상 실행 확인용 코드
if __name__ == '__main__':
    #print(main({"userId":"1111","bedtimeScore":3,"wakeupScore":3,"wakeupSensitivity":1,"cleaningScore":3,"cleaningSensitivity":3,"foodScore":2,"foodSensitivity":2,"cigaretteScore":3,"studyScore":2,"studySensitivity":1,"notebookScore":3,"notebookSensitivity":2,"alarmScore":3,"alarmSensitivity":2,"latestudyScore":3,"latestudySensitivity":1,"snoringScore":3,"snoringSensitivity":2,"friendlyScore":3,"inhomeScore":2,"inhomeSensitivity":1,"coldOrHot":1,"summerOrWinter":1}, "man_308_dataset.json"))
    #print(main({"userId":"2222","bedtimeScore":4,"wakeupScore":3,"wakeupSensitivity":1,"cleaningScore":2,"cleaningSensitivity":2,"foodScore":1,"foodSensitivity":1,"cigaretteScore":1,"studyScore":3,"studySensitivity":3,"notebookScore":3,"notebookSensitivity":2,"alarmScore":2,"alarmSensitivity":1,"latestudyScore":3,"latestudySensitivity":3,"snoringScore":3,"snoringSensitivity":1,"friendlyScore":1,"inhomeScore":2,"inhomeSensitivity":2,"coldOrHot":0,"summerOrWinter":3}, "man_308_dataset.json"))
    print(main({"userId":"ex1","bedtimeScore":3,"wakeupScore":3,"wakeupSensitivity":2,"cleaningScore":2,"cleaningSensitivity":2,"foodScore":2,"foodSensitivity":3,"cigaretteScore":3,"studyScore":2,"studySensitivity":2,"notebookScore":1,"notebookSensitivity":2,"alarmScore":2,"alarmSensitivity":1,"latestudyScore":1,"latestudySensitivity":2,"snoringScore":2,"snoringSensitivity":1,"friendlyScore":1,"inhomeScore":2,"inhomeSensitivity":2,"coldOrHot":1,"summerOrWinter":1}, "man_308_dataset.json"))
    print(main({"userId":"ex2","bedtimeScore":3,"wakeupScore":3,"wakeupSensitivity":2,"cleaningScore":2,"cleaningSensitivity":2,"foodScore":2,"foodSensitivity":3,"cigaretteScore":3,"studyScore":2,"studySensitivity":2,"notebookScore":2,"notebookSensitivity":1,"alarmScore":1,"alarmSensitivity":2,"latestudyScore":2,"latestudySensitivity":1,"snoringScore":1,"snoringSensitivity":2,"friendlyScore":1,"inhomeScore":2,"inhomeSensitivity":2,"coldOrHot":2,"summerOrWinter":3}, "man_308_dataset.json"))
    print(main({"userId":"ex3","bedtimeScore":3,"wakeupScore":3,"wakeupSensitivity":2,"cleaningScore":2,"cleaningSensitivity":2,"foodScore":2,"foodSensitivity":3,"cigaretteScore":3,"studyScore":2,"studySensitivity":2,"notebookScore":1,"notebookSensitivity":2,"alarmScore":2,"alarmSensitivity":3,"latestudyScore":1,"latestudySensitivity":2,"snoringScore":2,"snoringSensitivity":3,"friendlyScore":1,"inhomeScore":2,"inhomeSensitivity":2,"coldOrHot":1,"summerOrWinter":1}, "man_308_dataset.json"))