def modify(dataset, u_data):
    
    for data in dataset:
        del data['pattern_sensitivity']
        del data['cleaning_sensitivity']
        del data['food_sensitivity']
        del data['study_sensitivity']
        del data['noise_sensitivity']
        del data['alarm_sensitivity']
        del data['latenoise_sensitivity']
        del data['snoring_sensitivity']
        del data['overnight_sensitivity']
        del data['summer_or_winter']

    del u_data['pattern_sensitivity']
    del u_data['cleaning_sensitivity']
    del u_data['food_sensitivity']
    del u_data['study_sensitivity']
    del u_data['noise_sensitivity']
    del u_data['alarm_sensitivity']
    del u_data['latenoise_sensitivity']
    del u_data['snoring_sensitivity']
    del u_data['overnight_sensitivity']
    del u_data['summer_or_winter']

    return dataset, u_data