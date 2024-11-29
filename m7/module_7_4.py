def match_statistics(team1, team2, team1_num, team2_num, score_1, score_2, team1_time, team2_time):
    print("В команде %s: %s! " % (team1, team1_num))
    print("В команде %s: %s! " % (team2, team2_num))
    print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

    print("Команда {} решила задач: {}!".format(team1, score_1))
    print("Команда {} решила задач: {}!".format(team2, score_2))
    print("{} решили задачи за {}!".format(team1, team1_time))
    print("{} решили задачи за {}!".format(team2, team2_time))

    print(f"Команды решили {score_1} и {score_2} задач.")

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print(f"Победа команды {team1}!")
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print(f"Победа команды {team2}!")
    else:
        print("Ничья!")

    tasks_total = score_1 + score_2
    time_avg = (team1_time + team2_time) / (score_1 + score_2)

    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

match_statistics(team1, team2, team1_num, team2_num, score_1, score_2, team1_time, team2_time)