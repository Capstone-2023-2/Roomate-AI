def modify(dataset, u_data):
    
    wakeupSensitivity = u_data['wakeupSensitivity']
    cleaningSensitivity = u_data['cleaningSensitivity']
    foodSensitivity = u_data['foodSensitivity']
    studySensitivity = u_data['studySensitivity']
    notebookSensitivity = u_data['notebookSensitivity']
    alarmSensitivity = u_data['alarmSensitivity']
    latestudySensitivity = u_data['latestudySensitivity']
    snoringSensitivity = u_data['snoringSensitivity']
    inhomeSensitivity = u_data['inhomeSensitivity']
    coldOrHot = u_data['coldOrHot']
                
    for data in dataset:
        data['bedtimeScore'] = (data['bedtimeScore'] / 2 + 0.5) * wakeupSensitivity
        data['wakeupScore'] = (data['wakeupScore'] / 2 + 0.5) * wakeupSensitivity
        del data['wakeupSensitivity']
        data['cleaningScore'] *= cleaningSensitivity
        del data['cleaningSensitivity']
        if foodSensitivity == 1: data['foodScore'] = 0
        elif foodSensitivity == 2: data['foodScore'] *= 2
        elif foodSensitivity == 3: data['foodScore'] *= 3
        del data['foodSensitivity']
        data['cigaretteScore'] *= 3
        data['studyScore'] *= studySensitivity       
        del data['studySensitivity']
        if notebookSensitivity == 1: data['notebookScore'] = 0
        elif notebookSensitivity == 2: data['notebookScore'] *= 2
        elif notebookSensitivity == 3: data['notebookScore'] *= 3
        del data['notebookSensitivity']
        if alarmSensitivity == 1: data['alarmScore'] = 0
        elif alarmSensitivity == 2: data['alarmScore'] *= 2
        elif alarmSensitivity == 3: data['alarmScore'] *= 3
        del data['alarmSensitivity']
        if latestudySensitivity == 1: data['latestudyScore'] = 0
        elif latestudySensitivity == 2: data['latestudyScore'] *= 2
        elif latestudySensitivity == 3: data['latestudyScore'] *= 3
        del data['latestudySensitivity']
        if snoringSensitivity == 1: data['snoringScore'] = 0
        elif snoringSensitivity == 2: data['snoringScore'] *= 2
        elif snoringSensitivity == 3: data['snoringScore'] *= 3
        del data['snoringSensitivity']
        data['friendlyScore'] *= 3
        if inhomeSensitivity == 1: data['inhomeScore'] = 0
        elif inhomeSensitivity == 2: data['inhomeScore'] *= 2
        elif inhomeSensitivity == 3: data['inhomeScore'] *= 3
        del data['inhomeSensitivity']
        if coldOrHot == 0: data['coldOrHot'] = 0
        else: data['coldOrHot'] *= 3
        del data['summerOrWinter']
        
    u_data['bedtimeScore'] = (u_data['bedtimeScore'] / 2 + 0.5) * wakeupSensitivity
    u_data['wakeupScore'] = (u_data['wakeupScore'] / 2 + 0.5) * wakeupSensitivity
    del u_data['wakeupSensitivity']
    u_data['cleaningScore'] *= cleaningSensitivity
    del u_data['cleaningSensitivity']
    if foodSensitivity == 1: u_data['foodScore'] = 0
    elif foodSensitivity == 2: u_data['foodScore'] += 3
    elif foodSensitivity == 3: u_data['foodScore'] += 6
    del u_data['foodSensitivity']
    u_data['cigaretteScore'] *= 3
    u_data['studyScore'] *= studySensitivity       
    del u_data['studySensitivity']
    if notebookSensitivity == 1: u_data['notebookScore'] = 0
    elif notebookSensitivity == 2: u_data['notebookScore'] += 3
    elif notebookSensitivity == 3: u_data['notebookScore'] += 6
    del u_data['notebookSensitivity']
    if alarmSensitivity == 1: u_data['alarmScore'] = 0
    elif alarmSensitivity == 2: u_data['alarmScore'] += 3
    elif alarmSensitivity == 3: u_data['alarmScore'] += 6
    del u_data['alarmSensitivity']
    if latestudySensitivity == 1: u_data['latestudyScore'] = 0
    elif latestudySensitivity == 2: u_data['latestudyScore'] += 3
    elif latestudySensitivity == 3: u_data['latestudyScore'] += 6
    del u_data['latestudySensitivity']
    if snoringSensitivity == 1: u_data['snoringScore'] = 0
    elif snoringSensitivity == 2: u_data['snoringScore'] += 3
    elif snoringSensitivity == 3: u_data['snoringScore'] += 6
    del u_data['snoringSensitivity']
    u_data['friendlyScore'] *= 3
    if inhomeSensitivity == 1: u_data['inhomeScore'] = 0
    elif inhomeSensitivity == 2: u_data['inhomeScore'] += 3
    elif inhomeSensitivity == 3: u_data['inhomeScore'] += 6
    del u_data['inhomeSensitivity']
    if coldOrHot == 0: u_data['coldOrHot'] = 0
    else: u_data['coldOrHot'] *= 3
    del u_data['summerOrWinter']
    
    return dataset, u_data