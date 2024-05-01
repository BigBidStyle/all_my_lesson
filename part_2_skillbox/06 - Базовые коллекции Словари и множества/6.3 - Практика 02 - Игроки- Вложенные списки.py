# Есть готовый словарь игроков, у каждого игрока есть имя, команда,
# в которой он играет, а также его текущий статус, в котором указано,
# отдыхает он, тренируется или путешествует:

# Напишите программу, которая выводит на экран вот такие данные в разных строчках:

# Все члены команды из команды А, которые отдыхают.
# Все члены команды из группы B, которые тренируются.
# Все члены команды из команды C, которые путешествуют.

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}}
print(players_dict)
# Члены команды А которые сейчас отдыхают.
command = input("Enter the command number (A,B,C)\n: ")
does = input("Output team members who: \n(Training, Rest, Travel)\n:")

team_a_members = [
    player["name"]
    for player in players_dict.values()
    if player["team"] == command.capitalize() and player["status"] == does.capitalize()
]
print(f"Members of team {command}, who are now {does} : {team_a_members}")

