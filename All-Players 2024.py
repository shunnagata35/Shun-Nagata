import statsapi
import csv
from datetime import datetime

teamIds = []
rcvPlayerNameList = []
allStats = []

standings = statsapi.standings_data(division="all", season=2024)

for divisionId, divisionStandings in standings.items():
    for team in divisionStandings["teams"]:
        print(team["name"], team["team_id"])
        teamIds.append(team["team_id"])

for teamId in teamIds:

    players = statsapi.lookup_player(teamId)

    for player in players:
        playerId = player["id"]
        playerData = statsapi.player_stat_data(playerId, group="hitting", type="yearByYear")
        stats = playerData["stats"]
        playerPitchingData = statsapi.player_stat_data(playerId, group="pitching", type="yearByYear")
        if playerPitchingData["stats"]:
            continue  # Skip pitchers

        if len(stats) != 0:
            print(player["fullName"], playerId)
            mostRecentSeasonStats = stats[-1]
            hittingStats = mostRecentSeasonStats["stats"]
        else:
            continue

    

        doubles = hittingStats.get("doubles", 0)
        triples = hittingStats.get("triples", 0)
        HR = hittingStats.get("homeRuns", 0)
        singles = hittingStats.get("hits", 0) - doubles - triples - HR
        BB = hittingStats.get("baseOnBalls", 0)
        HBP = hittingStats.get("hitByPitch", 0)
        SB = hittingStats.get("stolenBases", 0)
        SO = hittingStats.get("strikeOuts", 0)
        CS = hittingStats.get("caughtStealing", 0)
        GDP = hittingStats.get("groundIntoDoublePlay", 0)
        PA = hittingStats.get("plateAppearances", 0)
        SF = hittingStats.get("sacFlies", 0)
        SH = hittingStats.get("sacBunts", 0)
        Div = PA - SF - SH

        if Div != 0:
            RCV = (singles * 0.4 + doubles * 0.7 + triples * 1.1 + HR * 1.5 + BB * 0.3 + HBP * 0.3 + SB * 0.2 - SO * 0.3 - CS * 0.3 - GDP * 1.3) / Div
            print("RCV:", RCV)
            rcvPlayerNameList.append([RCV, player["fullName"]])
            allStats.append([player["fullName"], singles, doubles, triples, HR, BB, HBP, SB, SO, CS, GDP, PA, SF, SH, RCV])

sortedRcvPlayerNameList = sorted(rcvPlayerNameList, reverse=True)

# Print the top 10 players or the available players if fewer than 10
for i in range(min(10, len(sortedRcvPlayerNameList))):
    print(i, sortedRcvPlayerNameList[i][1], sortedRcvPlayerNameList[i][0])

dt = datetime.now().isoformat()
today = dt.split("T")[0]

with open("rcv-" + today + ".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["RCV", "Name"])
    writer.writerows(sortedRcvPlayerNameList)

with open("allstats-" + today + ".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "singles", "doubles", "triples", "HR", "BB", "HBP", "SB", "SO", "CS", "GDP", "PA", "SF", "SH", "RCV"])
    writer.writerows(allStats)
