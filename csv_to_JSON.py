import json

file = open('teams_csv.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]
print (lines)
teams_from_csv = []
for line in lines:
    club_data = line.split(',')
    club = club_data[0]
    city = club_data[1]
    country = club_data[2]
    dict_line = {'Club':club, 'City':city, 'Country':country}
    teams_from_csv.append(dict_line)
file_json = open('teams_json.txt', 'w')
json.dump(teams_from_csv, file_json)
file_json.close()
