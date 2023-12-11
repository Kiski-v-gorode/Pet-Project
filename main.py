import json

json_file_path = r"/home/muhammad/Desktop/Pet-Project/soccer.json"

with open(json_file_path, "r", encoding="utf-8") as file:
    json_content = json.load(file)

teams = json_content["teams"]
matches = json_content["matches"]

"""
4 {'name': 'Локомотив М', 'games': 17, 'won': 7, 'drawn': 7, 'lost': 3, 'goals_scored': 27, 'missed_scored': 23, 'goal_difference': 4, 'points': 28, 'head_to_head': {'Рубин': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 2}, 'Факел': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 4}, 'ЦСКА': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 4, 'missed_scored': 1}, 'Крылья Советов': {'won': 0, 'drawn': 2, 'lost': 0, 'goals_scored': 4, 'missed_scored': 4}, 'Краснодар': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}, 'Сочи': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 1}, 'Балтика': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 2, 'missed_scored': 3}, 'Оренбург': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 0}, 'Зенит': {'won': 0, 'drawn': 0, 'lost': 2, 'goals_scored': 2, 'missed_scored': 5}, 'Пари Нижний Новгород': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 1}, 'Урал': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 2}, 'Динамо М': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 0, 'missed_scored': 0}, 'Ростов': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 1, 'missed_scored': 0}, 'Спартак М': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}, 'Ахмат': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 2}}}
5 {'name': 'ЦСКА', 'games': 17, 'won': 7, 'drawn': 7, 'lost': 3, 'goals_scored': 31, 'missed_scored': 23, 'goal_difference': 8, 'points': 28, 'head_to_head': {'Урал': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 1}, 'Ахмат': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 2, 'missed_scored': 3}, 'Локомотив М': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 4}, 'Сочи': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 3}, 'Динамо М': {'won': 2, 'drawn': 0, 'lost': 0, 'goals_scored': 5, 'missed_scored': 3}, 'Оренбург': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}, 'Зенит': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}, 'Крылья Советов': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 2}, 'Ростов': {'won': 0, 'drawn': 1, 'lost': 1, 'goals_scored': 3, 'missed_scored': 5}, 'Балтика': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 1}, 'Спартак М': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 2}, 'Рубин': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 0, 'missed_scored': 0}, 'Краснодар': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 1}, 'Пари Нижний Новгород': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 2, 'missed_scored': 3}, 'Факел': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}}}
9 {'name': 'Ростов', 'games': 17, 'won': 5, 'drawn': 5, 'lost': 7, 'goals_scored': 24, 'missed_scored': 29, 'goal_difference': -5, 'points': 20, 'head_to_head': {'Факел': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 2}, 'Зенит': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}, 'Крылья Советов': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 5, 'missed_scored': 1}, 'Рубин': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 3}, 'Сочи': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 4, 'missed_scored': 0}, 'Пари Нижний Новгород': {'won': 1, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 1}, 'Динамо М': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 1}, 'Балтика': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 2}, 'ЦСКА': {'won': 1, 'drawn': 1, 'lost': 0, 'goals_scored': 5, 'missed_scored': 3}, 'Урал': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 2}, 'Краснодар': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 3, 'missed_scored': 2}, 'Ахмат': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 3}, 'Локомотив М': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 1}, 'Оренбург': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}, 'Спартак М': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 1}}}
10 {'name': 'Факел', 'games': 17, 'won': 5, 'drawn': 5, 'lost': 7, 'goals_scored': 14, 'missed_scored': 18, 'goal_difference': -4, 'points': 20, 'head_to_head': {'Ростов': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 1}, 'Локомотив М': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 4, 'missed_scored': 1}, 'Балтика': {'won': 1, 'drawn': 1, 'lost': 0, 'goals_scored': 2, 'missed_scored': 1}, 'Зенит': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 0}, 'Пари Нижний Новгород': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 2}, 'Краснодар': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 0, 'missed_scored': 0}, 'Крылья Советов': {'won': 1, 'drawn': 0, 'lost': 0, 'goals_scored': 3, 'missed_scored': 0}, 'Урал': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 0, 'missed_scored': 0}, 'Рубин': {'won': 2, 'drawn': 0, 'lost': 0, 'goals_scored': 2, 'missed_scored': 0}, 'Сочи': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 2}, 'Динамо М': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 0, 'missed_scored': 0}, 'Оренбург': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 2}, 'Спартак М': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 0, 'missed_scored': 2}, 'Ахмат': {'won': 0, 'drawn': 0, 'lost': 1, 'goals_scored': 1, 'missed_scored': 2}, 'ЦСКА': {'won': 0, 'drawn': 1, 'lost': 0, 'goals_scored': 1, 'missed_scored': 1}}}
"""


# team1 - это JSON первой команды
# team2 - это JSON это второй команды
# возвращаем два элемента, первый, команда которая должна быть раньше в таблице и вторая команда
def stagings_sorting(team1, team2):
    team1_name, team2_name = team1["name"], team2["name"]

    criteria = [
        lambda t, o: t["head_to_head"][o]["won"] + t["head_to_head"][o]["drawn"],
        lambda t, o: t["head_to_head"][o]["won"],
        lambda t, o: t["head_to_head"][o]["goals_scored"] - t["head_to_head"][o]["missed_scored"],
        lambda t, o: t["head_to_head"][o]["goals_scored"]
    ]

    for criterion in criteria:
        points1, points2 = criterion(team1, team2_name), criterion(team2, team1_name)
        if points1 > points2:
            return team1, team2
        elif points1 < points2:
            return team2, team1

    return team1, team2


def generate_standings(teams, matches):
    standings = {}
    for team in teams:
        standings[teams[team]["id"]] = {
            "name": teams[team]["name"],
            "games": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "goals_scored": 0,
            "missed_scored": 0,
            "goal_difference": 0,
            "points": 0,
            "head_to_head": {}
        }

    for match in matches:
        if match["is_over"]:
            owner = match["owner_id"]
            guest = match["guest_id"]
            owner_goals = match["owner_goals"]
            guest_goals = match["guest_goals"]

            # Количество игр
            standings[owner]["games"] += 1
            standings[guest]["games"] += 1

            # Забитые голы обеих команд
            standings[owner]["goals_scored"] += match["owner_goals"]
            standings[guest]["goals_scored"] += match["guest_goals"]

            # Пропущенные голы обеих команд
            standings[owner]["missed_scored"] += match["guest_goals"]
            standings[guest]["missed_scored"] += match["owner_goals"]

            # Разница забитых и пропущенных
            standings[owner]["goal_difference"] = standings[owner]["goals_scored"] - standings[owner]["missed_scored"]
            standings[guest]["goal_difference"] = standings[guest]["goals_scored"] - standings[guest]["missed_scored"]

            # Обновление личных встреч
            if standings[guest]["name"] not in standings[owner]["head_to_head"]:
                standings[owner]["head_to_head"][standings[guest]["name"]] = {"won": 0, "drawn": 0, "lost": 0,
                                                                              "goals_scored": 0, "missed_scored": 0}

            if standings[owner]["name"] not in standings[guest]["head_to_head"]:
                standings[guest]["head_to_head"][standings[owner]["name"]] = {"won": 0, "drawn": 0, "lost": 0,
                                                                              "goals_scored": 0, "missed_scored": 0}

            standings[owner]["head_to_head"][standings[guest]["name"]]["goals_scored"] += guest_goals
            standings[owner]["head_to_head"][standings[guest]["name"]]["missed_scored"] += owner_goals

            standings[guest]["head_to_head"][standings[owner]["name"]]["goals_scored"] += owner_goals
            standings[guest]["head_to_head"][standings[owner]["name"]]["missed_scored"] += guest_goals

            if owner_goals > guest_goals:
                standings[owner]["won"] += 1
                standings[owner]["points"] += 3

                standings[guest]["lost"] += 1

                standings[owner]["head_to_head"][standings[guest]["name"]]["lost"] += 1
                standings[guest]["head_to_head"][standings[owner]["name"]]["won"] += 1

            elif owner_goals == guest_goals:
                standings[owner]["drawn"] += 1
                standings[owner]["points"] += 1

                standings[guest]["drawn"] += 1
                standings[guest]["points"] += 1

                standings[owner]["head_to_head"][standings[guest]["name"]]["drawn"] += 1
                standings[guest]["head_to_head"][standings[owner]["name"]]["drawn"] += 1

            else:
                standings[guest]["won"] += 1
                standings[guest]["points"] += 3

                standings[owner]["lost"] += 1

                standings[guest]["head_to_head"][standings[owner]["name"]]["lost"] += 1
                standings[owner]["head_to_head"][standings[guest]["name"]]["won"] += 1

        # else:
        #     standings = sorted(standings.values(), key=lambda team: team["points"], reverse=True)
    # return standings
    sub_standings = sorted(standings.values(), key=lambda team: team["points"], reverse=True)
    # print(sub_standings)
    standings = []
    team = 0
    teams = len(sub_standings) - 1

    while team <= teams:
        if team != teams and sub_standings[team]["points"] == sub_standings[team + 1]["points"]:
            standings.extend(stagings_sorting(sub_standings[team], sub_standings[team + 1]))
            # Чтобы не вставлять обработанное значение дважды
            team += 1

        else:
            standings.append(sub_standings[team])

        team += 1
    # for team in range(len(sub_standings) - 1):
    #     if sub_standings[team]["points"] == sub_standings[team + 1]["points"]:
    #         print(team)
    #     else:
    #         print(team)
    # print(f"{team, sub_standings[team]}")
    # print(f"{team + 1, sub_standings[team + 1]}")

    # print(standings)
    # standings = sorted(standings.values(), key=lambda team: (team["points"], team["won"], team["goal_difference"], team["goals_scored"]), reverse=True)
    #
    print(f'{"Место":<5}{"Клуб":>20}{"И":>5}{"В":>5}{"Н":>5}{"П":>5}{"ЗМ":>5}{"ПМ":>5}{"РМ":>5}{"О":>5}')
    for index in range(len(standings)):

        print(f'{index + 1:<5}{standings[index]["name"]:>20}{standings[index]["games"]:>5} {standings[index]["won"]:>5}'
              f'{standings[index]["drawn"]:>5}{standings[index]["lost"]:>5}{standings[index]["goals_scored"]:>5}'
              f'{standings[index]["missed_scored"]:>5}{standings[index]["goal_difference"]:>5}{standings[index]["points"]:>5}')


print(generate_standings(teams=teams, matches=matches))

"""
Нужно хранить исход личных встреч (набранные очки, количество побед, разницу голов, число забитых мячей) для каждой команды 
(Т.е. в поле head_to_head я храню теже поля что и в обычной турнирной таблице)

Пример поля head_to_head:
{head_to_head: {"Арсенал Тула":{"won":1, "drawn":0, "lost": 1, "goals_scored": 3, "missed_scored": 2}}}

won - поле, которое указывает сколько раз команда "Арсенал Тула" победила команду "хозяина"
drawn - поле, которое указывает сколько раз команда "Арсенал Тула" сыграла в гичью с командой "хозяина"
lost - поле, которое указывает сколько раз команда "Арсенал Тула" проиграла команде "хозяина"
goals_scored - поле, которое указывает сколько раз команда "Арсенал Тула" забила команде "хозяина"
missed_scored - поле, которое указывает сколько раз команда "Арсенал Тула" пропустила от команды "хозяина"

Пример данных для команды, которая ссыграла, только два матча с командой "Арсенал Тула"
{name:Динамо Москва, head_to_head:{"Арсенал Тула":{"won":1, "drawn":0, "lost": 1, "goals_scored": 3, "missed_scored": 2}}}

Пример отсортиованного списка:
Место                Клуб    И     В    Н    П   ЗМ   ПМ   РМ    О
1               Краснодар   17    10    5    2   27   14   13   35
2                   Зенит   17    10    3    4   34   17   17   33
3                Динамо М   17     8    7    2   28   21    7   31
4          Крылья Советов   17     8    5    4   36   24   12   29

Ведем дополнительный список для прошедших проверку команд

Затем пройдем по списку, который отсортирован по очкам (по полю "points"), 

1) если у текущей команды очков больше чем у следующей добавлем ее в доп список и переходим к следующей команде,
2) если у текущей команды одинаковое количество очков со следующей командой, то мы по очереди смотрим следующее:

    1) Количество набранных очков в личных встречах 
    2) Количество побед в личных встречах
    3) Лучшая разница забитых и пропущенных голов в лчных встречах
    4) Количество забитых мячей в лчных встречах

"""
