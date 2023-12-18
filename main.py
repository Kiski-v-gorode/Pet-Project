import json
import os
import time


json_file_path = os.path.abspath("soccer.json")

with open(json_file_path, "r", encoding="utf-8") as file:
    json_content = json.load(file)

teams = json_content["teams"]
matches = json_content["matches"]


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

    standings = sorted(standings.values(), key=lambda team: (team["points"], team["won"], team["goal_difference"], team["goals_scored"]), reverse=True)

    for i in range(len(standings) - 1):
        current_team = standings[i]
        next_team = standings[i + 1]

        if current_team["points"] == next_team["points"]:

            team1_name, team2_name = current_team["name"], next_team["name"]

            # Сколько раз team2 выйграла у team1 + сколь раз они сыграли в ничью и наоборот (Считаю количество очков
            # команд)
            points2 = (current_team["head_to_head"][team2_name]["won"] * 3) + current_team["head_to_head"][team2_name]["drawn"]
            points1 = (next_team["head_to_head"][team1_name]["won"] * 3) + next_team["head_to_head"][team1_name]["drawn"]

            # Сколько раз team2 выйграла у team1 и наоборот
            won2 = current_team["head_to_head"][team2_name]["won"]
            won1 = next_team["head_to_head"][team1_name]["won"]

            # Сколько раз team2 забила и пропустила от team1 и наоборот (Считаю разницу голов в личных встречах)
            goal_difference2 = current_team["head_to_head"][team2_name]["goals_scored"] - current_team["head_to_head"][team2_name]["missed_scored"]
            goal_difference1 = next_team["head_to_head"][team1_name]["goals_scored"] - next_team["head_to_head"][team1_name]["missed_scored"]

            # Сколько раз team2 забила team1 и наоборот
            goals2 = current_team["head_to_head"][team2_name]["goals_scored"]
            goals1 = next_team["head_to_head"][team1_name]["goals_scored"]

            if points2 > points1:
                standings[i], standings[i + 1] = next_team, current_team

            elif won2 > won1:
                standings[i], standings[i + 1] = next_team, current_team

            elif goal_difference2 > goal_difference1:
                standings[i], standings[i + 1] = next_team, current_team

            elif goals2 > goals1:
                standings[i], standings[i + 1] = next_team, current_team

    print(f'{"Место":<5}{"Клуб":>20}{"И":>5}{"В":>5}{"Н":>5}{"П":>5}{"ЗМ":>5}{"ПМ":>5}{"РМ":>5}{"О":>5}')
          
    for index in range(len(standings)):

        print(f'{index + 1:<5}{standings[index]["name"]:>20}{standings[index]["games"]:>5} {standings[index]["won"]:>5}'
              f'{standings[index]["drawn"]:>5}{standings[index]["lost"]:>5}{standings[index]["goals_scored"]:>5}'
              f'{standings[index]["missed_scored"]:>5}{standings[index]["goal_difference"]:>5}{standings[index]["points"]:>5}')


start = time.time()
generate_standings(teams=teams, matches=matches)
print((time.time() - start))

"""Нужно хранить исход личных встреч (набранные очки, количество побед, разницу голов, число забитых мячей) для 
каждой команды (Т.е. в поле head_to_head я храню те же поля что и в обычной турнирной таблице)

Пример поля head_to_head:
{head_to_head: {"Арсенал Тула":{"won":1, "drawn":0, "lost": 1, "goals_scored": 3, "missed_scored": 2}}}

won - поле, которое указывает сколько раз команда "Арсенал Тула" победила команду "хозяина"
drawn - поле, которое указывает сколько раз команда "Арсенал Тула" сыграла в ничью с командой "хозяина"
lost - поле, которое указывает сколько раз команда "Арсенал Тула" проиграла команде "хозяина"
goals_scored - поле, которое указывает сколько раз команда "Арсенал Тула" забила команде "хозяина"
missed_scored - поле, которое указывает сколько раз команда "Арсенал Тула" пропустила от команды "хозяина"

Пример данных для команды, которая сыграла, только два матча с командой "Арсенал Тула" 
{name:Динамо Москва, head_to_head:{"Арсенал Тула":{"won":1, "drawn":0, "lost": 1, "goals_scored": 3, "missed_scored": 2}}}

Пример отсортированного списка:
Место                Клуб    И     В    Н    П   ЗМ   ПМ   РМ    О
1               Краснодар   17    10    5    2   27   14   13   35
2                   Зенит   17    10    3    4   34   17   17   33
3                Динамо М   17     8    7    2   28   21    7   31
4          Крылья Советов   17     8    5    4   36   24   12   29

Ведем дополнительный список для прошедших проверку команд

Затем пройдем по списку, который отсортирован по очкам (по полю "points"), 

1) если у текущей команды очков больше чем у следующей добавляем ее в доп список и переходим к следующей команде,
2) если у текущей команды одинаковое количество очков со следующей командой, то мы по очереди смотрим следующее:

    1) Количество набранных очков в личных встречах 
    2) Количество побед в личных встречах
    3) Лучшая разница забитых и пропущенных голов в личных встречах
    4) Количество забитых мячей в личных встречах

"""
