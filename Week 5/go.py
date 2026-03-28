# Write your solution here
def who_won(game_board:list):
    pl1 = 0
    pl2 = 0
    for i in game_board:
        for j in i:
            if j == 1:
                pl1 +=1
            elif j == 2:
                pl2 +=1

    if pl1 > pl2:
        return 1
    elif pl2 > pl1:
        return 2
    else:
        return 0
        
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]

    print(who_won(m))