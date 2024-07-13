# 성향 수치는 그대로 두고, 성향 민감도는 삭제하는 함수
def modify(dataset, u_data):
    
    if u_data != "":
        del u_data['wakeupSensitivity']
        del u_data['cleaningSensitivity']
        del u_data['foodSensitivity']
        del u_data['studySensitivity']
        del u_data['notebookSensitivity']
        del u_data['alarmSensitivity']
        del u_data['latestudySensitivity']
        del u_data['snoringSensitivity']
        del u_data['inhomeSensitivity']
        del u_data['summerOrWinter']
    
    for data in dataset:
        del data['wakeupSensitivity']
        del data['cleaningSensitivity']
        del data['foodSensitivity']
        del data['studySensitivity']
        del data['notebookSensitivity']
        del data['alarmSensitivity']
        del data['latestudySensitivity']
        del data['snoringSensitivity']
        del data['inhomeSensitivity']
        del data['summerOrWinter']

    return dataset, u_data

# 클러스터링용 modify 함수
def clustering_modify(dataset):
    
    for data in dataset:
        del data['wakeupSensitivity']
        del data['cleaningSensitivity']
        del data['foodSensitivity']
        del data['studySensitivity']
        del data['notebookSensitivity']
        del data['alarmSensitivity']
        del data['latestudySensitivity']
        del data['snoringSensitivity']
        del data['inhomeSensitivity']
        del data['summerOrWinter']
        
    return dataset