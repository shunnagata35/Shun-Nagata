import statsapi
import csv
from datetime import datetime

teamIds = []
avgPlayerNameList = []
allStats = []

standings = statsapi.standings_data(division="all", season=2024)

# Get the number of games played by each team
teamGames = {}
for divisionId, divisionStandings in standings.items():
    for team in divisionStandings["teams"]:
        team_id = team["team_id"]
        games_played = team["w"] + team["l"]
        teamGames[team_id] = games_played
        print(team["name"], team_id, games_played)
        teamIds.append(team_id)

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

        PA = hittingStats.get("plateAppearances", 0)

        # Calculate PA per game based on team games and exclude players with less than 3.1 PA per game
        if PA / teamGames[teamId] < 3.1:
            continue

        hits = hittingStats.get("hits", 0)
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
        SF = hittingStats.get("sacFlies", 0)
        SH = hittingStats.get("sacBunts", 0)
        
        AVG = hittingStats.get("avg", 0)
        avgPlayerNameList.append([AVG, player["fullName"]])
        allStats.append([player["fullName"], singles, doubles, triples, HR, BB, HBP, SB, SO, CS, GDP, PA, SF, SH, AVG])

sortedavgPlayerNameList = sorted(avgPlayerNameList, reverse=True)

# Print the top 10 players or the available players if fewer than 10
for i in range(min(10, len(sortedavgPlayerNameList))):
    print(i, sortedavgPlayerNameList[i][1], sortedavgPlayerNameList[i][0])

dt = datetime.now().isoformat()
today = dt.split("T")[0]

with open("avg-" + today + ".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["AVG", "Name"])
    writer.writerows(sortedavgPlayerNameList)

with open("allstats-" + today + ".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "singles", "doubles", "triples", "HR", "BB", "HBP", "SB", "SO", "CS", "GDP", "PA", "SF", "SH", "RCV"])
    writer.writerows(allStats)

