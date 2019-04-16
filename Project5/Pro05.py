
Printboard = [[0] * 8 for i in range(8)]

for i in range(0, 8):
    for j in range(0, 8):
        if i % 2 == 0:
            if j % 2 == 1:
                Printboard[i][j] = "■"
            else:
                Printboard[i][j] = "□"

        else:
             if j % 2 == 1:
                Printboard[i][j] = "□"
             else:
                Printboard[i][j] = "■"

def Board(ex):
    count = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if ex[i][j] == 'F':
                if Printboard[i][j] == "□":
                    count += 1

    print(count)


board = []
for i in range(8):
    B = input()
    board.append(B)

Board(board)