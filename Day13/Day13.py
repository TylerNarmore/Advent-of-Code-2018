from GetData import get_input
import string
from copy import deepcopy
from time import sleep

def main():
    data = get_input(13)
    parsed_data = []

    for i in data:
        parsed_data.append(list(i.rstrip()))
    p2 = deepcopy(parsed_data)
    print(part_1(parsed_data))
    part_2(p2)




def part_1(data):
    ans=0

    tracks = deepcopy(data)
    carts = {}
    c_num=0
    direction = {"^":0, ">":1, "v":2, "<":3}

    for row in range(len(tracks)):
        for col in range(len(tracks[row])):
            if tracks[row][col] in "<>v^":
                carts[string.ascii_uppercase[c_num]] = [[col,row], 0]
                #print(col,row)
                if tracks[row-1][col] in "\\/|+" and tracks[row][col-1] in "\\/-+":
                    tracks[row][col] = "+"
                if tracks[row-1][col] in "\\/|+" and tracks[row+1][col] in "\\/|+":
                    tracks[row][col] = "|"
                elif tracks[row][col-1] in "\\/-+" and tracks[row][col+1] in "\\/-+":
                    tracks[row][col] = "-"
                    #print(row,col)
                c_num+=1
    #for i in tracks:
        #print(''.join(i))
    #print("\n\n")

    tick = 0
    while True:
        #print(carts)
        tick+=1
        row = 0
        skip = []
        while row < len(data):
            col = 0
            while col <len(data[row]):
                if (col,row) in skip:
                    col += 1

                    continue
                cur = data[row][col]
                #Right
                if cur == ">":
                    if data[row][col+1] in "v><^":
                        return ((col+1,row),tick)
                    skip.append((col+1,row))
                    if tracks[row][col+1] == "-":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col,row]:
                                carts[i][0][0] += 1
                            data[row][col + 1] = ">"
                    elif tracks[row][col+1] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col,row]:
                                carts[i][0][0]+=1
                            data[row][col+1] = "^"
                    elif tracks[row][col + 1] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] += 1
                            data[row][col + 1] = "v"
                    elif tracks[row][col + 1] == "+":

                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] += 1
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row][col+1] = "^"
                                elif carts[i][1] == 1:
                                    #print("RIGHT")
                                    #print(i, carts[i])
                                    carts[i][1] = 2
                                    data[row][col + 1] = ">"
                                    #print(i, carts[i])
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0
                                    data[row][col + 1] = "v"
                                break
                # DOWN
                elif cur == "v":
                    if data[row+1][col] in "v><^":
                        return ((col,row+1),tick)
                    skip.append((col, row+1))
                    if tracks[row+1][col] == "|":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] += 1
                            data[row + 1][col] = "v"
                    elif tracks[row+1][col] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col,row]:
                                carts[i][0][1]+=1
                            data[row+1][col] = "<"
                    elif tracks[row + 1][col] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] += 1
                            data[row + 1][col] = ">"
                    elif tracks[row + 1][col] == "+":
                        data[row][col] = " "
                        for i in carts:
                            # for x in data:
                            #     print(''.join(x))
                            if carts[i][0] == [col, row]:

                                # for x in data:
                                #     print(''.join(x))
                                carts[i][0][1] += 1
                                #print("INTERSECTION")
                                #print(i, carts[i])
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row+1][col] = ">"
                                elif carts[i][1] == 1:
                                    carts[i][1] = 2
                                    data[row + 1][col] = "v"
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0

                                    data[row + 1][col] = "<"
                                #print(i, carts[i])
                                break
                    else:
                        return ((col,row+1),tick)
                # Left
                elif cur == "<":
                    skip.append((col - 1, row))
                    if data[row][col-1] in "v><^":
                        return ((col-1,row),tick)
                    if tracks[row][col - 1] == "-":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                            data[row][col - 1] = "<"
                    elif tracks[row][col - 1] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                            data[row][col - 1] = "v"
                    elif tracks[row][col - 1] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                            data[row][col - 1] = "^"
                    elif tracks[row][col - 1] == "+":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row][col - 1] = "v"
                                elif carts[i][1] == 1:
                                    carts[i][1] = 2
                                    data[row][col - 1] = "<"
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0
                                    data[row][col - 1] = "^"
                                break
                    else:
                        return ((col-1,row),tick)

                # Up
                elif cur == "^":
                    skip.append((col, row-1))
                    if data[row-1][col] in "v><^":
                        return ((col,row-1),tick)
                    if tracks[row-1][col] == "|":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                            data[row - 1][col] = "^"
                    elif tracks[row-1][col] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col,row]:
                                carts[i][0][1]-=1
                            data[row-1][col] = ">"
                    elif tracks[row - 1][col] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                            data[row - 1][col] = "<"
                    elif tracks[row - 1][col] == "+":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row-1][col] = "<"
                                elif carts[i][1] == 1:
                                    carts[i][1] = 2
                                    data[row - 1][col] = "^"
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0
                                    data[row - 1][col] = ">"
                                break
                    else:
                        return ((col,row-1),tick)
                col+=1
            row+=1
        # for i in data:
        #     print(''.join(i))
        # print(carts["A"])
        # print(carts["B"])
        # print("\n")




def part_2(data):
    ans = 0

    tracks = deepcopy(data)
    carts = {}
    c_num = 0
    direction = {"^": 0, ">": 1, "v": 2, "<": 3}

    for row in range(len(tracks)):
        for col in range(len(tracks[row])):
            if tracks[row][col] in "<>v^":
                carts[string.ascii_uppercase[c_num]] = [[col, row], 0]
                # print(col, row)
                if tracks[row - 1][col] in "\\/|+" and tracks[row][col - 1] in "\\/-+":
                    tracks[row][col] = "+"
                if tracks[row - 1][col] in "\\/|+" and tracks[row + 1][col] in "\\/|+":
                    tracks[row][col] = "|"
                elif tracks[row][col - 1] in "\\/-+" and tracks[row][col + 1] in "\\/-+":
                    tracks[row][col] = "-"
                    # print(row, col)
                c_num += 1
    # for i in tracks:
        # print(''.join(i))
    # print("\n\n")

    tick = 0
    while True:
        # print(carts)
        tick += 1
        row = 0
        skip = []
        while row < len(data):
            col = 0
            while col < len(data[row]):
                to_be_deleted = []
                if (col, row) in skip:
                    col += 1

                    continue
                cur = data[row][col]
                # Right
                if cur == ">":
                    if data[row][col +1] in "v><^":
                        for id,cart in carts.items():
                            if cart[0] == [col,row] or cart[0] == [col+1,row]:
                                to_be_deleted.append(id)
                        for i in to_be_deleted:
                            del(carts[i])
                    skip.append((col + 1, row))
                    if tracks[row][col + 1] == "-":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] += 1
                            data[row][col + 1] = ">"
                    elif tracks[row][col + 1] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] += 1
                            data[row][col + 1] = "^"
                    elif tracks[row][col + 1] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] += 1
                            data[row][col + 1] = "v"
                    elif tracks[row][col + 1] == "+":

                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] += 1
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row][col + 1] = "^"
                                elif carts[i][1] == 1:
                                    # print("RIGHT")
                                    # print(i, carts[i])
                                    carts[i][1] = 2
                                    data[row][col + 1] = ">"
                                    # print(i, carts[i])
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0
                                    data[row][col + 1] = "v"
                                break
                # DOWN
                elif cur == "v":
                    if data[row+1][col] in "v><^":
                        for id,cart in carts.items():
                            if cart[0] == [col,row] or cart[0] == [col,row+1]:
                                to_be_deleted.append(id)
                        for i in to_be_deleted:
                            del(carts[i])
                    skip.append((col, row + 1))
                    if tracks[row + 1][col] == "|":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] += 1
                            data[row + 1][col] = "v"
                    elif tracks[row + 1][col] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] += 1
                            data[row + 1][col] = "<"
                    elif tracks[row + 1][col] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] += 1
                            data[row + 1][col] = ">"
                    elif tracks[row + 1][col] == "+":
                        data[row][col] = " "
                        for i in carts:
                            # for x in data:
                            #     print(''.join(x))
                            if carts[i][0] == [col, row]:

                                # for x in data:
                                #     print(''.join(x))
                                carts[i][0][1] += 1
                                # print("INTERSECTION")
                                # print(i, carts[i])
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row + 1][col] = ">"
                                elif carts[i][1] == 1:
                                    carts[i][1] = 2
                                    data[row + 1][col] = "v"
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0

                                    data[row + 1][col] = "<"
                                # print(i, carts[i])
                                break
                    else:
                        return ((col, row + 1), tick)
                # Left
                elif cur == "<":
                    skip.append((col - 1, row))
                    if data[row][col - 1] in "v><^":
                        for id,cart in carts.items():
                            if cart[0] == [col,row] or cart[0] == [col-1,row]:
                                to_be_deleted.append(id)
                        for i in to_be_deleted:
                            del(carts[i])
                    if tracks[row][col - 1] == "-":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                            data[row][col - 1] = "<"
                    elif tracks[row][col - 1] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                            data[row][col - 1] = "v"
                    elif tracks[row][col - 1] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                            data[row][col - 1] = "^"
                    elif tracks[row][col - 1] == "+":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][0] -= 1
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row][col - 1] = "v"
                                elif carts[i][1] == 1:
                                    carts[i][1] = 2
                                    data[row][col - 1] = "<"
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0
                                    data[row][col - 1] = "^"
                                break
                    else:
                        return ((col - 1, row), tick)

                # Up
                elif cur == "^":
                    skip.append((col, row - 1))
                    if data[row-1][col] in "v><^":
                        for id,cart in carts.items():
                            if cart[0] == [col,row] or cart[0] == [col,row-1]:
                                to_be_deleted.append(id)
                        for i in to_be_deleted:
                            del(carts[i])
                    if tracks[row - 1][col] == "|":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                            data[row - 1][col] = "^"
                    elif tracks[row - 1][col] == "/":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                            data[row - 1][col] = ">"
                    elif tracks[row - 1][col] == "\\":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                            data[row - 1][col] = "<"
                    elif tracks[row - 1][col] == "+":
                        data[row][col] = " "
                        for i in carts:
                            if carts[i][0] == [col, row]:
                                carts[i][0][1] -= 1
                                if carts[i][1] == 0:
                                    carts[i][1] = 1
                                    data[row - 1][col] = "<"
                                elif carts[i][1] == 1:
                                    carts[i][1] = 2
                                    data[row - 1][col] = "^"
                                elif carts[i][1] == 2:
                                    carts[i][1] = 0
                                    data[row - 1][col] = ">"
                                break
                    else:
                        return ((col, row - 1), tick)
                col += 1
            row += 1
        # for i in data:
        #     print(''.join(i))
        # print(carts["A"])
        # print(carts["B"])
        # print("\n")
        if len(carts) == 1:
            print(carts)
            break


if __name__ == "__main__":
    main()
