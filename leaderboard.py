@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    try:
        # 1. Get total games played for each team in 2025
        standings = statsapi.standings_data(division="all", season=2025)
        team_games = {}
        for division in standings.values():
            for team in division["teams"]:
                team_id = team["team_id"]
                team_games[team_id] = team["w"] + team["l"]

        # 2. Get all hitters' season stats
        raw = statsapi.get('stats', {
            'stats': 'season',
            'group': 'hitting',
            'season': 2025,
            'sportIds': 1
        })

        players = raw['stats'][0]['splits']
        qualified = []

        for player in players:
            stat = player['stat']
            team_id = player['team']['id']
            team_g = team_games.get(team_id, 162)  # default to 162 if not found
            pa = int(stat.get('plateAppearances', 0))

            if team_g == 0 or pa / team_g < 3.1:
                continue

            qualified.append({
                'Name': player['player']['fullName'],
                'Team': player['team']['name'],
                'HR': int(stat.get('homeRuns', 0)),
                'OPS': float(stat.get('ops', 0)),
                'AVG': float(stat.get('avg', 0)),
                'RBI': int(stat.get('rbi', 0)),
                'BB': int(stat.get('baseOnBalls', 0)),
                'SO': int(stat.get('strikeOuts', 0)),
                'PA': pa
            })

        df = pd.DataFrame(qualified)
        df = df.sort_values('AVG', ascending=False).head(70)  # optional sort key
        return jsonify(df.to_dict(orient='records'))


    except Exception as e:
        print("Leaderboard error:", e)
        return jsonify({'error': str(e)}), 500
