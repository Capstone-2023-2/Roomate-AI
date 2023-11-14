def modify(dataset, u_data):
    
    pattern_sensitivity = u_data['pattern_sensitivity']
    cleaning_sensitivity = u_data['cleaning_sensitivity']
    food_sensitivity = u_data['food_sensitivity']
    study_sensitivity = u_data['study_sensitivity']
    noise_sensitivity = u_data['noise_sensitivity']
    alarm_sensitivity = u_data['alarm_sensitivity']
    latenoise_sensitivity = u_data['latenoise_sensitivity']
    snoring_sensitivity = u_data['snoring_sensitivity']
    overnight_sensitivity = u_data['overnight_sensitivity']
    cold_or_hot = u_data['cold_or_hot']
                
    for data in dataset:
        data['sleep_score'] = (data['sleep_score'] / 2 + 0.5) * pattern_sensitivity
        data['wakeup_score'] = (data['wakeup_score'] / 2 + 0.5) * pattern_sensitivity
        del data['pattern_sensitivity']
        data['cleaning_score'] *= cleaning_sensitivity
        del data['cleaning_sensitivity']
        if food_sensitivity == 1: data['food_score'] = 0
        elif food_sensitivity == 2: data['food_score'] *= 2
        elif food_sensitivity == 3: data['food_score'] *= 3
        del data['food_sensitivity']
        data['cigarette_score'] *= 3
        data['study_score'] *= study_sensitivity       
        del data['study_sensitivity']
        if noise_sensitivity == 1: data['noise_score'] = 0
        elif noise_sensitivity == 2: data['noise_score'] *= 2
        elif noise_sensitivity == 3: data['noise_score'] *= 3
        del data['noise_sensitivity']
        if alarm_sensitivity == 1: data['alarm_score'] = 0
        elif alarm_sensitivity == 2: data['alarm_score'] *= 2
        elif alarm_sensitivity == 3: data['alarm_score'] *= 3
        del data['alarm_sensitivity']
        if latenoise_sensitivity == 1: data['latenoise_score'] = 0
        elif latenoise_sensitivity == 2: data['latenoise_score'] *= 2
        elif latenoise_sensitivity == 3: data['latenoise_score'] *= 3
        del data['latenoise_sensitivity']
        if snoring_sensitivity == 1: data['snoring_score'] = 0
        elif snoring_sensitivity == 2: data['snoring_score'] *= 2
        elif snoring_sensitivity == 3: data['snoring_score'] *= 3
        del data['snoring_sensitivity']
        data['outsider_score'] *= 3
        if overnight_sensitivity == 1: data['overnight_score'] = 0
        elif overnight_sensitivity == 2: data['overnight_score'] *= 2
        elif overnight_sensitivity == 3: data['overnight_score'] *= 3
        del data['overnight_sensitivity']
        if cold_or_hot == 0: data['cold_or_hot'] = 0
        else: data['cold_or_hot'] *= 3
        del data['summer_or_winter']
        
    u_data['sleep_score'] = (u_data['sleep_score'] / 2 + 0.5) * pattern_sensitivity
    u_data['wakeup_score'] = (u_data['wakeup_score'] / 2 + 0.5) * pattern_sensitivity
    del u_data['pattern_sensitivity']
    u_data['cleaning_score'] *= cleaning_sensitivity
    del u_data['cleaning_sensitivity']
    if food_sensitivity == 1: u_data['food_score'] = 0
    elif food_sensitivity == 2: u_data['food_score'] = 5
    elif food_sensitivity == 3: u_data['food_score'] = 9
    del u_data['food_sensitivity']
    u_data['cigarette_score'] *= 3
    u_data['study_score'] *= study_sensitivity       
    del u_data['study_sensitivity']
    if noise_sensitivity == 1: u_data['noise_score'] = 0
    elif noise_sensitivity == 2: u_data['noise_score'] = 5
    elif noise_sensitivity == 3: u_data['noise_score'] = 9
    del u_data['noise_sensitivity']
    if alarm_sensitivity == 1: u_data['alarm_score'] = 0
    elif alarm_sensitivity == 2: u_data['alarm_score'] = 5
    elif alarm_sensitivity == 3: u_data['alarm_score'] = 9
    del u_data['alarm_sensitivity']
    if latenoise_sensitivity == 1: u_data['latenoise_score'] = 0
    elif latenoise_sensitivity == 2: u_data['latenoise_score'] = 5
    elif latenoise_sensitivity == 3: u_data['latenoise_score'] = 9
    del u_data['latenoise_sensitivity']
    if snoring_sensitivity == 1: u_data['snoring_score'] = 0
    elif snoring_sensitivity == 2: u_data['snoring_score'] = 5
    elif snoring_sensitivity == 3: u_data['snoring_score'] = 9
    del u_data['snoring_sensitivity']
    u_data['outsider_score'] *= 3
    if overnight_sensitivity == 1: u_data['overnight_score'] = 0
    elif overnight_sensitivity == 2: u_data['overnight_score'] = 5
    elif overnight_sensitivity == 3: u_data['overnight_score'] = 9
    del u_data['overnight_sensitivity']
    if cold_or_hot == 0: u_data['cold_or_hot'] = 0
    else: u_data['cold_or_hot'] *= 3
    del u_data['summer_or_winter']
    
    return dataset, u_data