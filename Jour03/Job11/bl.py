def time_to_text(minutes):
    heures = minutes // 60
    minutes = minutes % 60
    print(f'{heures} heure(s) et {minutes} minutes')


time_to_text(83)
time_to_text(888)
time_to_text(181000)