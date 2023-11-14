def modify(dataset, u_data):
    
    for data in dataset:
        del data['lifestyle_sensitivity']
        del data['cleaning_sensitivity']
        del data['indoor_food_sensitivity']
        del data['indoor_study_sensitivity']
        del data['indoor_noise_sensitivity']
        del data['alarm_sensitivity']
        del data['late_study_sensitivity']
        del data['sleeping_habit_sensitivity']
        del data['overnight_sensitivity']
        del data['summer_or_winter']

    del u_data['lifestyle_sensitivity']
    del u_data['cleaning_sensitivity']
    del u_data['indoor_food_sensitivity']
    del u_data['indoor_study_sensitivity']
    del u_data['indoor_noise_sensitivity']
    del u_data['alarm_sensitivity']
    del u_data['late_study_sensitivity']
    del u_data['sleeping_habit_sensitivity']
    del u_data['overnight_sensitivity']
    del u_data['summer_or_winter']

    return dataset, u_data

def clustering_modify(dataset):
    
    for data in dataset:
        del data['lifestyle_sensitivity']
        del data['cleaning_sensitivity']
        del data['indoor_food_sensitivity']
        del data['indoor_study_sensitivity']
        del data['indoor_noise_sensitivity']
        del data['alarm_sensitivity']
        del data['late_study_sensitivity']
        del data['sleeping_habit_sensitivity']
        del data['overnight_sensitivity']
        del data['summer_or_winter']
        
    return dataset