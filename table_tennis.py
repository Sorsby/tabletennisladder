players = []


def add_player(name):
    players.append(name)


def get_player_pos(name):
    return players.index(name)


def update_ladder(winner, loser):
    global players
    if winner in players:
        if loser in players:
            #both in list
            winner_pos = get_player_pos(winner)
            loser_pos = get_player_pos(loser)
            untouched = players[:loser_pos]

            shift = list(players)
            del shift[winner_pos]

            players = untouched + [winner] + shift
        else:
            #loser not in players
            players.append(loser)
    else:
        if loser in players:
            # winner not in list player in list
            loser_pos = get_player_pos(loser)
            untouched = players[:loser_pos]
            shift = players[loser_pos:]
            untouched.append(winner)
            players = untouched + shift
        else:
            # winner not in list loser not in list
            players.append(winner)
            players.append(loser)


def init_players():
    add_player('Matt')
    add_player('Dan')
    add_player('Ash')
    add_player('James')
    add_player('Doge')


def main():
    init_players()
    print players

# both in ladder already
    update_ladder('Ash', 'Matt')
    print players

# new winner to ladder
    update_ladder('Mike', 'Ash')
    print players

#both not in ladder
    update_ladder('Lee', 'Andy')
    print players

# loser not in ladder already
    update_ladder('Matt', 'Emily')
    print players


if __name__ == '__main__':
    main()
