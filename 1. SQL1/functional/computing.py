GROUP_ALL_TIME = {}
GROUP_TIME = {}

def average_time(info):
    # TODO: Распределение времени ответа по группам
    for i in info:
        if i[2] is not None:
            try:
                GROUP_ALL_TIME[i[0][0]].append((int(i[2]) - int(i[1])))
            except:
                GROUP_ALL_TIME[i[0][0]] = []
                GROUP_ALL_TIME[i[0][0]].append((int(i[2]) - int(i[1])))

    # TODO: Рассчёт среднего времени
    for key, value in GROUP_ALL_TIME.items():
        average = sum(value) / len(value) / 1000 / 60 / 60
        average = round(average, 2)
        GROUP_TIME[key] = average

    return GROUP_TIME
