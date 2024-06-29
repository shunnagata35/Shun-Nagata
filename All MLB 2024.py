import statsapi, csv
from datetime import datetime

teamIds = []
rcvPlayerNameList = []
allStats = []

standings = statsapi.standings_data(division="all", season=2024)
#print(standings)

for divisionId, divisionStandings in standings.items():
    for team in divisionStandings["teams"]:
        print(team["name"], team["team_id"])
        teamIds.append(team["team_id"])
# print(len(teamIds), "teams in total")
# print(teamIds)

for teamId in teamIds:
    players = statsapi.lookup_player(teamId)
    # print(len(players))
    # print(players)

    for player in players:
        playerId = player["id"]
        playerData = statsapi.player_stat_data(playerId, group="hitting", type="yearByYear")
        stats = playerData["stats"]
        playerPitchingData = statsapi.player_stat_data(playerId, group="pitching", type="yearByYear")
        if playerPitchingData["stats"]:
                    continue

        if len(stats) != 0:
                    print(player["fullName"], playerId)
                    mostRecentSeasonStats = stats[len(stats)-1]
                    hittingStats = mostRecentSeasonStats["stats"]
            #         print(hittingStats)
        else:
                    continue

doubles = hittingStats["doubles"]
triples = hittingStats["triples"]
HR = hittingStats["homeRuns"]
singles = hittingStats["hits"] - doubles - triples - HR
BB = hittingStats["baseOnBalls"]
HBP = hittingStats["hitByPitch"]
SB = hittingStats["stolenBases"]
SO = hittingStats["strikeOuts"]
CS = hittingStats["caughtStealing"]
GDP = hittingStats["groundIntoDoublePlay"]
PA = hittingStats["plateAppearances"]
SF = hittingStats["sacFlies"]
SH = hittingStats["sacBunts"]
Div = PA - SF - SH

if Div != 0:
    RCV = (singles * 0.4 + doubles * 0.7 + triples * 1.1 + HR * 1.5 + BB * 0.3 + HBP * 0.3 + SB * 0.2 - SO * 0.3 - CS * 0.3 - GDP * 1.3)/ (PA - SF - SH)
    print("RCV:", RCV)
    rcvPlayerNameList.append( [RCV, player["fullName"]] )
    allStats.append( [player["fullName"], singles, doubles, triples, HR, BB, HBP, SB, SO, CS, GDP, PA, SF, SH, RCV] )
              

# print(rcvPlayerNameList)
sortedRcvPlayerNameList = sorted(rcvPlayerNameList, reverse=True)
# print(sortedRcvPlayerNameList)
for i in range(0,10):
    print(i, sortedRcvPlayerNameList[i][1], sortedRcvPlayerNameList[i][0])

dt = datetime.now().isoformat()
today = dt.split("T")[0]

with open("rcv-" + today + ".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["RCV", "Name"])
    writer.writerows(sortedRcvPlayerNameList)

with open("allstatt-" + today + ".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "singles", "doubles", "triples", "HR", "BB", "HBP", "SB", "SO", "CS", "GDP", "PA", "SF", "SH", "RCV"])
    writer.writerows(allStats)
