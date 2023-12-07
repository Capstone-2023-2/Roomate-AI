import json
import numpy as np
import pandas as pd
import featureByScore as fsc
import featureBySensitivity as fse
from sklearn.metrics.pairwise import euclidean_distances


# 충분한 사용자 데이터가 있는지 파악하여 추천이 가능한지 반환하는 함수
def check_data(f_name):
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
        
    if len(dataset) < 20:
        return False
    else:
        return True
        
# 기존 사용자 삭제 후 반환하는 함수
def del_user(u_data, f_name):
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    for data in dataset:
        if u_data["userId"] == data["userId"]:
            dataset.remove(data)
            break
        
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return dataset

# 신규 사용자 추가 후 반환하는 함수
def add_user(u_data, f_name):
    
    dataset = del_user(u_data, f_name)
    dataset.append(u_data)
    add_state(u_data)
    
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return dataset

# 신규 사용자의 찾기 상태를 true로 바꾸는 함수
def add_state(u_data):
    
    with open("state_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    for data in dataset:
        if u_data["userId"] == data["userId"]:
            dataset.remove(data)
            break
    
    temp = {"userId": u_data["userId"], "state": True}
    dataset.append(temp)
    
    with open("state_dataset.json", 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return

# ID로 사용자의 정보를 받아와서 반환하는 함수
def get_userdata(u_id, f_name):
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    for data in dataset:
        if u_id == data["userId"]:
            return data
    
    return {}

# 사용자 정보가 어디에 있는지 모를 때 ID로 정보를 받아와 반환하는 함수
def get_userdata_whichfile(u_id):
    
    f_names = ["man_308_dataset.json", "man_309_dataset.json", "woman_308_dataset.json", "woman_309_dataset.json"]
    
    for f_name in f_names:
        with open(f_name, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        for data in dataset:
            if u_id == data["userId"]:
                return data, f_name
    
    return {}

# 해당 사용자의 찜 데이터를 받아와서 찜 리스트를 반환하는 함수
def get_wishlist_data(u_data):
    
    with open("wishlist_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    for data in dataset:
        if  u_data["userId"] == data["userId"]:
            return data["wishIds"]
    
    return []

# 실제 모든 매칭 데이터를 받아와서 반환하는 함수
def get_matching_data():
    
    with open("matching_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    return dataset

# 이전 추천 기록을 받아와서 추천했던 리스트를 반환하는 함수
def get_recommended_data(u_data):
    
    with open("recommended_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
        
    for data in dataset:
        if u_data["userId"] == data["userId"]:
            return data["recommendedIds"]
    
    return []

# 룸메이트 찾기 상태 데이터를 받아와서 반환하는 함수
def get_state_data():
    
    with open("state_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
        
    return dataset

# wishlist.json 파일을 업데이트하는 함수
def update_wishlist(wishlist):
    
    with open("wishlist_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    found = False
    for data in dataset:
        if wishlist["userId"] == data["userId"]:
            found = True
            data["wishIds"].append(wishlist["wishId"])
            break
    if not found:
        temp = {"userId": wishlist["userId"], "wishIds": [wishlist["wishId"]]}
        dataset.append(temp)
                  
    with open('wishlist_dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return

# matching_data.json을 업데이트하는 함수 - 한 번 매칭되면 변경 불가 가정
def update_matching_data(matching):
    
    with open("matching_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
        
    dataset.append(matching)
            
    with open('matching_dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return

# recommended_data.json을 업데이트하는 함수
def update_recommended_data(u_data, recommendedIDs):
    
    with open("recommended_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    found = False
    for data in dataset:
        if u_data["userId"] == data["userId"]:
            found = True
            data["recommendedIds"] = recommendedIDs
    if not found:
        temp = {"userId": u_data["userId"], "recommendedIds": recommendedIDs}
        dataset.append(temp)
    
    with open('recommended_dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return

# state_data.json을 업데이트하는 함수
def update_state_data(state):
    
    with open("state_dataset.json", 'r', encoding='utf-8') as f:
        dataset = json.load(f)
        
    for data in dataset:
        if state["userId"] == data["userId"]:
            dataset.remove(data)
            break    
    dataset.append(state)
            
    with open('state_dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f)
    
    return

# 개인성향 유사도 기반 순위 매기기 함수 (score only)
def score_similarity_ranking(u_data, f_name):
    
    result = []
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    dataset, user_data = fsc.modify(dataset, u_data)
    dataset[-1] = user_data
    
    df = pd.DataFrame(dataset)
    n_array = df.to_numpy()
    
    IDs = n_array[:, 0]
    features = n_array[:, 1:]
    
    euclidean_distances_result = euclidean_distances(features, features)
    ranking = np.argsort(euclidean_distances_result)[-1]
    ranking = ranking.tolist()
    
    for rank in ranking:
        result.append(IDs[rank])
    if u_data["userId"] in result: 
        result.remove(u_data["userId"])
    
    return result

# 개인성향 및 민감도 유사도 기반 순위 매기기 함수 (score + sensitivity)
def total_similarity_ranking(u_data, f_name):
    
    result = []
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    df = pd.DataFrame(dataset)
    n_array = df.to_numpy()
    
    IDs = n_array[:, 0]
    features = n_array[:, 1:]
    
    euclidean_distances_result = euclidean_distances(features, features)
    ranking = np.argsort(euclidean_distances_result)[-1]
    ranking = ranking.tolist()
    
    for rank in ranking:
        result.append(IDs[rank])
    if u_data["userId"] in result: 
        result.remove(u_data["userId"])
    
    return result

# 민감도 적용한 개인성향 유사도 기반 순위 매기기 함수 (sensitivity 적용한 score only)
def sensitive_score_similarity_ranking(u_data, f_name):
    
    result = []
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    dataset, user_data = fse.modify(dataset, u_data)
    dataset[-1] = user_data
    #dataset = check_cluster(u_data, f_name)
    
    df = pd.DataFrame(dataset)
    n_array = df.to_numpy()
    
    IDs = n_array[:, 0]
    features = n_array[:, 1:]
    
    euclidean_distances_result = euclidean_distances(features, features)
    ranking = np.argsort(euclidean_distances_result)[-1]
    ranking = ranking.tolist()
    
    for rank in ranking:
        result.append(IDs[rank])
    if u_data["userId"] in result: 
        result.remove(u_data["userId"])
    
    return result

# 성향 유사도 기반 추천 함수
def basic_recommend(u_data, f_name):
    
    result = sensitive_score_similarity_ranking(u_data, f_name)   
    
    return result

# 찜 관련 협업 필터링 기반 추천 함수
def wishlist_filtering_recommend(u_data, f_name):
    
    res, result = [], []
    wishlist = get_wishlist_data(u_data)
    
    for wish in wishlist:
        res.append(score_similarity_ranking(get_userdata(wish, f_name), f_name)[0:20])
    
    for i in range(20):
        for j in range(len(res)):
            temp = res[j][i]
            if temp not in result and temp != u_data["userId"]:
                result.append(res[j][i])   
    
    return result

# 실제 매칭 데이터 관련 협업 필터링 기반 추천 함수
def result_filtering_recommend(u_data, f_name):
    
    res, result = [], []
    matching = get_matching_data()
    similar = total_similarity_ranking(u_data, f_name)[0:5]
    
    for sim in similar:
        for match in matching:
            if sim == match["userId"]:
                res.append(score_similarity_ranking(get_userdata(match["matchingId"], f_name), f_name)[0:20])
                break
            elif sim == match["matchingId"]:
                res.append(score_similarity_ranking(get_userdata(match["userId"], f_name), f_name)[0:20])
                break
    
    for i in range(20):
        for j in range(len(res)):
            temp = res[j][i]
            if temp not in result and temp != u_data["userId"]:
                result.append(res[j][i])
    
    return result

# 찾기 상태를 확인해서 찾지 않는 사용자를 빼는 함수
def check_seeking_state(recommends):

    result = []
    state_data = get_state_data()
    
    for rec_id in recommends:
        for state in state_data:
            if rec_id == state["userId"] and state["state"]:
                result.append(rec_id)
                break
                    
    return result

# 이전에 추천했던 기록을 확인해서 추천할 사용자를 조정하는 함수
def check_recommended_data(u_data, a, b, c):

    a = a[:12]
    b = b[:12]
    c = c[:12]
    
    result = []
    recommended_data = get_recommended_data(u_data)
    
    basic = [rec for rec in a if rec not in recommended_data]
    wish = [rec for rec in a if rec not in recommended_data and rec not in basic]
    real = [rec for rec in a if rec not in recommended_data and rec not in basic and rec not in wish]
    
    if len(real) == 0 and len(wish) == 0:
        result += basic[:6]
    elif len(real) == 0 and len(wish) == 1:
        result += basic[:5]
        result += wish[0]
    elif len(real) == 0 and len(wish) > 1:
        result += basic[:4]
        result += wish[:2]
    elif len(real) > 0 and len(wish) == 0:
        result += basic[:5]
        result += wish[0]
    elif len(real) > 0 and len(wish) == 1:
        result += basic[:4]
        result += wish[0]
        result += real[0]
    else:
        result += basic[:3]
        result += wish[:2]
        result += real[0]
    
    return result

# 같은 클러스터에 속하는 사용자의 정보만 반환하는 함수
def check_cluster(u_data, f_name):
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    if f_name == "man_308_dataset.json":
        f_name = "man_308_cluster_dataset.json"
    elif f_name == "man_309_dataset.json":
        f_name = "man_309_cluster_dataset.json"
    elif f_name == "woman_308_dataset.json":
        f_name = "woman_308_cluster_dataset.json"
    elif f_name == "woman_309_dataset.json":
        f_name = "woman_309_cluster_dataset.json"
    
    with open(f_name, 'r', encoding='utf-8') as f:
        cluster_dataset = json.load(f)
    
    cluster = -1
    for cluster_data in cluster_dataset:
        if u_data["userId"] == cluster_data["userId"]:
            cluster = cluster_data["cluster"]
            
    result = [cluster_data["userId"] for cluster_data in cluster_dataset if cluster == cluster_data["cluster"]]
    result = [data for data in dataset if data["userId"] in result]
    
    return result

# 추천 리스트에 대한 유사도 측정
def measure_similarities(u_id, recommended_ids):
    
    result = []
    dataset = []
    
    for recommended_id in recommended_ids:
        data, _ = get_userdata_whichfile(recommended_id)
        dataset.append(data)
    
    dataset, _ = fsc.modify(dataset, "")
    
    df = pd.DataFrame(dataset)
    n_array = df.to_numpy()
    
    IDs = n_array[:, 0]
    features = n_array[:, 1:]
    
    euclidean_distances_result = euclidean_distances(features, features)
    ranking = np.argsort(euclidean_distances_result)[-1]
    ranking = ranking.tolist()
    
    for rank in ranking:
        if IDs[rank] != u_id:
            temp = euclidean_distances_result[-1][rank]
            similarity = round((15 - temp) / 3 * 20, 1)
            result.append(similarity)
    
    return result

# 전체 추천 목록 업데이트
def update_user():
      
    return