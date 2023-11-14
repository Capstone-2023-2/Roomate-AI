def modify(dataset, u_data):
    
    lifestyle_sensitivity = u_data['lifestyle_sensitivity']
    cleaning_sensitivity = u_data['cleaning_sensitivity']
    indoor_food_sensitivity = u_data['indoor_food_sensitivity']
    indoor_study_sensitivity = u_data['indoor_study_sensitivity']
    indoor_noise_sensitivity = u_data['indoor_noise_sensitivity']
    alarm_sensitivity = u_data['alarm_sensitivity']
    late_study_sensitivity = u_data['late_study_sensitivity']
    sleeping_habit_sensitivity = u_data['sleeping_habit_sensitivity']
    overnight_sensitivity = u_data['overnight_sensitivity']
    hot_or_cold = u_data['hot_or_cold']
                
    for data in dataset:
        data['sleep_score'] = (data['sleep_score'] / 2 + 0.5) * lifestyle_sensitivity
        data['wakeup_score'] = (data['wakeup_score'] / 2 + 0.5) * lifestyle_sensitivity
        del data['lifestyle_sensitivity']
        data['cleaning_score'] *= cleaning_sensitivity
        del data['cleaning_sensitivity']
        if indoor_food_sensitivity == 1: data['indoor_food_score'] = 0
        elif indoor_food_sensitivity == 2: data['indoor_food_score'] *= 2
        elif indoor_food_sensitivity == 3: data['indoor_food_score'] *= 3
        del data['indoor_food_sensitivity']
        data['smoking_score'] *= 3
        data['indoor_study_score'] *= indoor_study_sensitivity       
        del data['indoor_study_sensitivity']
        if indoor_noise_sensitivity == 1: data['indoor_noise_score'] = 0
        elif indoor_noise_sensitivity == 2: data['indoor_noise_score'] *= 2
        elif indoor_noise_sensitivity == 3: data['indoor_noise_score'] *= 3
        del data['indoor_noise_sensitivity']
        if alarm_sensitivity == 1: data['alarm_score'] = 0
        elif alarm_sensitivity == 2: data['alarm_score'] *= 2
        elif alarm_sensitivity == 3: data['alarm_score'] *= 3
        del data['alarm_sensitivity']
        if late_study_sensitivity == 1: data['laten_study_score'] = 0
        elif late_study_sensitivity == 2: data['late_study_score'] *= 2
        elif late_study_sensitivity == 3: data['late_study_score'] *= 3
        del data['late_study_sensitivity']
        if sleeping_habit_sensitivity == 1: data['sleeping_habit_score'] = 0
        elif sleeping_habit_sensitivity == 2: data['sleeping_habit_score'] *= 2
        elif sleeping_habit_sensitivity == 3: data['sleeping_habit_score'] *= 3
        del data['sleeping_habit_sensitivity']
        data['intimacy_score'] *= 3
        if overnight_sensitivity == 1: data['overnight_score'] = 0
        elif overnight_sensitivity == 2: data['overnight_score'] *= 2
        elif overnight_sensitivity == 3: data['overnight_score'] *= 3
        del data['overnight_sensitivity']
        if hot_or_cold == 0: data['hot_or_cold'] = 0
        else: data['hot_or_cold'] *= 3
        del data['summer_or_winter']
        
    u_data['sleep_score'] = (u_data['sleep_score'] / 2 + 0.5) * lifestyle_sensitivity
    u_data['wakeup_score'] = (u_data['wakeup_score'] / 2 + 0.5) * lifestyle_sensitivity
    del u_data['lifestyle_sensitivity']
    u_data['cleaning_score'] *= cleaning_sensitivity
    del u_data['cleaning_sensitivity']
    if indoor_food_sensitivity == 1: u_data['indoor_food_score'] = 0
    elif indoor_food_sensitivity == 2: u_data['indoor_food_score'] += 3
    elif indoor_food_sensitivity == 3: u_data['indoor_food_score'] += 6
    del u_data['indoor_food_sensitivity']
    u_data['smoking_score'] *= 3
    u_data['indoor_study_score'] *= indoor_study_sensitivity       
    del u_data['indoor_study_sensitivity']
    if indoor_noise_sensitivity == 1: u_data['indoor_noise_score'] = 0
    elif indoor_noise_sensitivity == 2: u_data['indoor_noise_score'] += 3
    elif indoor_noise_sensitivity == 3: u_data['indoor_noise_score'] += 6
    del u_data['indoor_noise_sensitivity']
    if alarm_sensitivity == 1: u_data['alarm_score'] = 0
    elif alarm_sensitivity == 2: u_data['alarm_score'] += 3
    elif alarm_sensitivity == 3: u_data['alarm_score'] += 6
    del u_data['alarm_sensitivity']
    if late_study_sensitivity == 1: u_data['late_study_score'] = 0
    elif late_study_sensitivity == 2: u_data['late_study_score'] += 3
    elif late_study_sensitivity == 3: u_data['late_study_score'] += 6
    del u_data['late_study_sensitivity']
    if sleeping_habit_sensitivity == 1: u_data['sleeping_habit_score'] = 0
    elif sleeping_habit_sensitivity == 2: u_data['sleeping_habit_score'] += 3
    elif sleeping_habit_sensitivity == 3: u_data['sleeping_habit_score'] += 6
    del u_data['sleeping_habit_sensitivity']
    u_data['intimacy_score'] *= 3
    if overnight_sensitivity == 1: u_data['overnight_score'] = 0
    elif overnight_sensitivity == 2: u_data['overnight_score'] += 3
    elif overnight_sensitivity == 3: u_data['overnight_score'] += 6
    del u_data['overnight_sensitivity']
    if hot_or_cold == 0: u_data['hot_or_cold'] = 0
    else: u_data['hot_or_cold'] *= 3
    del u_data['summer_or_winter']
    
    return dataset, u_data