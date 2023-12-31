def generate_standings(teams, matches):
    standings = {}
    for team in teams:
        standings[team["id_team"]] = {
            "name": team["name"],
            "games": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "goals_scored": 0,
            "missed_scored": 0,
            "goal_difference": 0,
            "points": 0,
        }

    for match in matches:

        # team_id хозяев и гостей
        owner = match["owner_id"]
        guest = match["guest_id"]

        # Количество голов хозяев и гостей
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

        if owner_goals > guest_goals:
            standings[owner]["won"] += 1
            standings[owner]["points"] += 3

            standings[guest]["lost"] += 1

        elif owner_goals == guest_goals:
            standings[owner]["drawn"] += 1
            standings[owner]["points"] += 1

            standings[guest]["drawn"] += 1
            standings[guest]["points"] += 1

        else:
            standings[guest]["won"] += 1
            standings[guest]["points"] += 3

            standings[owner]["lost"] += 1

    return sorted(standings.values(), key=lambda team: (team['points'], team["won"], team['goal_difference']), reverse=True)
