def lineup(*players):
    player_counts = {}

    for player, country in players:
        if country in player_counts:
            player_counts[country].append(player)
        else:
            player_counts[country] = [player]

    sorted_player_counts = sorted(player_counts.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for country, country_players in sorted_player_counts:
        result += f"{country}:\n"
        for player in country_players:
            result += f"  -{player}\n"

    return result.strip()



print(lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))