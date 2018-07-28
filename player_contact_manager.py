def player_manager(players):
    if players == None:
        return []
    else:
        players = list(players.split(','))
        l = []
        i = 0
        while i < len(players) - 1:
            d = dict()
            d['player'] = players[i].strip()
            d['contact'] = int(players[i + 1])
            l.append(d)
            i += 2
        return(l)


print(player_manager("John Doe, 8167238327, Jane Doe, 8163723827"))
