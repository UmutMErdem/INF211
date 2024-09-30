def generate(row, column):
    liste = []
    number = 0
    if 2 <= row <= 10 and 2 <= column <= 10:
        for i in range(row):
            liste.append([*range(number, number + column)])
            number += column
        return liste

def shuffle(board, times=20):
    if is_valid(board) == True:
        if 0 < times:
            direction = []
            counter = 0
            flag = False
            while not flag:
                while counter < times:
                    direction.append(move_random(board))
                    counter += 1
                if len(direction) % 2 == 0:
                    b = ["U", "L"]
                    c = ["D", "R"]
                    if len(direction) == 4:
                        liste = direction[:int(len(direction)/2)]
                        liste_inverse = direction[int(len(direction)/2):]
                        if liste == liste_inverse[::-1]:
                            flag = False
                        else:
                            for j in range(int(len(direction) / 2)):
                                if direction[j] in b:
                                    if c[b.index(direction[j])] != direction[-(j + 1)]:
                                        flag = True
                                        break
                                    else:
                                        flag = False
                                else:
                                    if b[c.index(direction[j])] != direction[-(j + 1)]:
                                        flag = True
                                        break
                                    else:
                                        flag = False
                    else:
                        for j in range(int(len(direction) / 2)):
                            if direction[j] in b:
                                if c[b.index(direction[j])] != direction[-(j + 1)]:
                                    flag = True
                                    break
                                else:
                                    flag = False
                            else:
                                if b[c.index(direction[j])] != direction[-(j + 1)]:
                                    flag = True
                                    break
                                else:
                                    flag = False
                    if not flag:
                        counter = 0
                        direction.clear()
                        continue
                flag = True
            return direction


def reset(board):
    if board == generate(len(board), len(board[0])):
        pass
    else:
        a = generate(len(board), len(board[0]))
        board.clear()
        for i in a:
            board.append(i)

def is_valid(board):
    flag = True
    if board:
        a = len(board[0])
        for i in range(len(board)):
            if len(board[i]) != a and not 1 < len(board[i]) <= 10:
                flag = False
                break
            a = len(board[i])
    else:
        flag = False
    if 1 < len(board) <= 10 and flag:
        liste = []
        for i in board:
            for j in i:
                liste.append(j)
        for k in liste:
            if liste.count(k) != 1 or len(board)*len(board[0]) <= k:
                return False
        return True
    else:
        return False

def is_solved(board):
    if is_valid(board) == True:
        if board == generate(len(board), len(board[0])):
            return True
        return False

def get_board_size(board):
    if is_valid(board) == True:
        return (len(board), len(board[0]))

def move_right(board):
    if is_valid(board) == True:
        x = [i.index(j) for i in board if 0 in i for j in i if 0 == j]
        y = [i for i in range(len(board)) if 0 in board[i]]
        if len(board[0]) - 1 > x[0]:
            liste = []
            number1 = board[y[0]][x[0]]
            number2 = board[y[0]][x[0]+1]
            board[y[0]][x[0]], board[y[0]][x[0]+1] = number2, number1
            for i in board:
                liste.append(i)
            board.clear()
            for i in liste:
                board.append(i)
            return 1
        else:
            return 0

def move_left(board):
    if is_valid(board) == True:
        x = [i.index(j) for i in board if 0 in i for j in i if 0 == j]
        y = [i for i in range(len(board)) if 0 in board[i]]
        if 0 < x[0]:
            liste = []
            number1 = board[y[0]][x[0]]
            number2 = board[y[0]][x[0] - 1]
            board[y[0]][x[0]], board[y[0]][x[0] - 1] = number2, number1
            for i in board:
                liste.append(i)
            board.clear()
            for i in liste:
                board.append(i)
            return 1
        else:
            return 0

def move_up(board):
    if is_valid(board) == True:
        x = [i.index(j) for i in board if 0 in i for j in i if 0 == j]
        y = [i for i in range(len(board)) if 0 in board[i]]
        if 0 < y[0]:
            liste = []
            number1 = board[y[0]][x[0]]
            number2 = board[y[0]-1][x[0]]
            board[y[0]][x[0]], board[y[0]-1][x[0]] = number2, number1
            for i in board:
                liste.append(i)
            board.clear()
            for i in liste:
                board.append(i)
            return 1
        else:
            return 0

def move_down(board):
    if is_valid(board) == True:
        x = [i.index(j) for i in board if 0 in i for j in i if 0 == j]
        y = [i for i in range(len(board)) if 0 in board[i]]
        if len(board) - 1 > y[0]:
            liste = []
            number1 = board[y[0]][x[0]]
            number2 = board[y[0]+1][x[0]]
            board[y[0]][x[0]], board[y[0]+1][x[0]] = number2, number1
            for i in board:
                liste.append(i)
            board.clear()
            for i in liste:
                board.append(i)
            return 1
        else:
            return 0

def move_random(board):
    import random
    if is_valid(board) == True:
        x = [i.index(j) for i in board if 0 in i for j in i if 0 == j]
        y = [i for i in range(len(board)) if 0 in board[i]]
        coordinatsf = [x[::], y[::]]
        coordinatsl = [x, y]
        liste = list()
        numbers = [-1, 1]
        direction = ""
        a = random.choice(coordinatsl)
        b = random.choice(numbers)
        if a == x:
            if x[0] == 0:
                x[0] += 1
                direction += "R"
            elif x[0] + 1 == len(board[0]):
                x[0] -= 1
                direction += "L"
            else:
                x[0] += b
                if b < 0:
                    direction += "L"
                else:
                    direction += "R"

        elif a == y:
            if y[0] == 0:
                y[0] += 1
                direction += "D"
            elif y[0] + 1 == len(board):
                y[0] -= 1
                direction += "U"
            else:
                y[0] += b
                if b < 0:
                    direction += "U"
                else:
                    direction += "D"
        number1 = board[coordinatsf[1][0]][coordinatsf[0][0]]
        number2 = board[coordinatsl[1][0]][coordinatsl[0][0]]
        board[coordinatsf[1][0]][coordinatsf[0][0]], board[coordinatsl[1][0]][coordinatsl[0][0]] = number2, number1
        for i in board:
            liste.append(i)
        board.clear()
        for i in liste:
            board.append(i)
        return direction

def move(board, moves):
    if is_valid(board) == True:
        direct = [i for i in moves if i in "LRDU" or i in "lrdu"]
        counter = 0
        for i in moves:
            x = [i.index(j) for i in board if 0 in i for j in i if 0 == j]
            y = [i for i in range(len(board)) if 0 in board[i]]
            coordinatsf = [x[::], y[::]]
            coordinatsl = [x, y]
            liste = list()
            if i.upper() == "L" and x[0] != 0:
                x[0] -= 1
                counter += 1
            elif i.upper() == "R" and x[0] + 1 != len(board[0]):
                x[0] += 1
                counter += 1
            elif i.upper() == "U" and y[0] != 0:
                y[0] -= 1
                counter += 1
            elif i.upper() == "D" and y[0] + 1 != len(board[0]):
                y[0] += 1
                counter += 1
            number1 = board[coordinatsf[1][0]][coordinatsf[0][0]]
            number2 = board[coordinatsl[1][0]][coordinatsl[0][0]]
            board[coordinatsf[1][0]][coordinatsf[0][0]], board[coordinatsl[1][0]][coordinatsl[0][0]] = number2, number1
            for i in board:
                liste.append(i)
            board.clear()
            for i in liste:
                board.append(i)
        return counter

def rotate(board):
    if is_valid(board) == True:
        liste = []
        for j in range(len(board[0])):
            a = [board[i][j] for i in range(len(board)-1,-1,-1)]
            liste.append(a)
        return liste

def print_board(board):
    if is_valid(board) == True:
        for i in board:
            print(*i, sep="\t", end= "\n")

def play(board, moves):
    if is_valid(board) == True:
        if is_solved(board) != True:
            counter = 0
            for i in moves:
                if is_solved(board) == True:
                    return counter
                elif i == "U" or i == "u":
                    if move_up(board) == 1:
                        counter += 1
                    else:
                        continue
                elif i == "D" or i == "d":
                    if move_down(board) == 1:
                        counter += 1
                    else:
                        continue
                elif i == "R" or i == "r":
                    if move_right(board) == 1:
                        counter += 1
                    else:
                        continue
                elif i == "L" or i == "l":
                    if move_left(board) == 1:
                        counter += 1
                    else:
                        continue
                else:
                    continue
            if is_solved(board) == True:
                return counter
            return -1
        else:
            return 0
    else:
        return -2

def play_interactive(board=None):
    while True:
        if not board:
            row = 0
            column = 0
            while not row and not column:
                print("Please type the puzzle size number.")
                row = input("Row number:")
                column = input("Column number:")
            board = generate(int(row), int(column))
            shuffle(board)
        else:
            if is_valid(board) == True:
                counter = 0
                slctn_list = ""
                while is_solved(board) == False:
                    print(f"Current board is:\n")
                    print_board(board)
                    selection = input("\nWhere do you want to move: ")
                    if selection.upper() == "Q":
                        print("Exiting.")
                        return (slctn_list, -1)
                    elif selection.upper() == "U":
                        if move_up(board) == 1:
                            slctn_list += "U"
                            counter += 1
                        else:
                            continue
                    elif selection.upper() == "D":
                        if move_down(board) == 1:
                            slctn_list += "D"
                            counter += 1
                        else:
                            continue
                    elif selection.upper() == "R":
                        if move_right(board) == 1:
                            slctn_list += "R"
                            counter += 1
                        else:
                            continue
                    elif selection.upper() == "L":
                        if move_left(board) == 1:
                            slctn_list += "L"
                            counter += 1
                        else:
                            continue
                    elif selection.upper() == "M":
                        slctn_list += move_random(board)
                        counter += 1
                    else:
                        print("\nWrong move.\n")
                print(f"Current board is:\n")
                print_board(board)
                print(f"\nCongrats! You solved the board in {counter} moves.")
                return (slctn_list, counter)
            else:
                print("The board matrix elements must be between 0:1:row*column-1")
                return ('', -2)