import json
import pandas as pd
import featureByScore as fsc
from sklearn.cluster import KMeans


# 개인성향을 기반으로 한 클러스터링 결과를 파일로 저장하는 함수
def clustering(u_data, f_name):

    result = []
    
    with open(f_name, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    clustering_dataset = fsc.clustering_modify(dataset)

    df = pd.DataFrame(clustering_dataset)
    IDs = df['ID'].tolist()
    df = df.drop('ID', axis=1)

    kmeans = KMeans(n_clusters=3, random_state=10, n_init=10)
    kmeans.fit(df)
    
    for i, label in enumerate(kmeans.labels_):
        temp = {"ID": IDs[i], "cluster": str(label)}
        result.append(temp)
    
    if f_name == "man_308_dataset.json":
        f_name = "man_308_cluster_dataset.json"
    elif f_name == "man_309_dataset.json":
        f_name = "man_309_cluster_dataset.json"
    elif f_name == "woman_308_dataset.json":
        f_name = "woman_308_cluster_dataset.json"
    elif f_name == "woman_309_dataset.json":
        f_name = "woman_309_cluster_dataset.json"
    
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(result, f)
        
    return