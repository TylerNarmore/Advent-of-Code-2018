import re
from GetData import get_input
import string
from pprint import *

def main():
    data = get_input(6)

    parsed = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
    cords = {}
    i = 1
    for x,y in parsed:
        cords[i] = (x,y)
        i+=1

    part_1(cords)
    part_2(cords)


def part_1(data):
    global xlist
    global ylist
    xlist = []
    ylist = []
    scores = {}
    for point,cords in data.items():
        x = cords[0]
        y=cords[1]
        xlist.append(x)
        ylist.append(y)
        scores[point] = 0

    row = [0] * (max(xlist) + 1)
    grid = []
    maxed_out = {}
    for _ in range(max(ylist) + 1):
        grid.append(row + [])
    for point, cords in data.items():
        grid[cords[1]][cords[0]] = point

    for row in range(max(ylist)+1):
        for column in range(max(xlist)+1):
            shortest = 9999999
            shortest_point = None
            tiedFlag=False
            for point, cords in data.items():
                x,y = cords
                distance = abs(x-column)+abs(y-row)
                if distance == shortest:
                    # print(shortest_point,point)
                    tiedFlag = True
                if distance<shortest:
                    # print(shortest_point, point,"\n\n")
                    shortest = distance
                    shortest_point = point
                    tiedFlag = False
                #print(shortest_point)


            # print(tiedFlag)
            if tiedFlag:
                #print(scores[shortest_point])
                grid[row][column] = "."

            else:
                grid[row][column] = shortest_point
                scores[shortest_point] = scores[shortest_point] + 1
            # for i in grid:
            #     print('\t'.join(map(str, i)))
            # print("\n\n\n")
        biggest = 0

    for i in grid:
        if i[-1] in scores:
            scores[i[-1]] = 0
        if i[0] in scores:
            scores[i[0]] = 0
    for i in grid[-1]:
        if i in scores:
            scores[i] = 0
    for i in grid[0]:
        if i in scores:
            scores[i] = 0
    for point, score in scores.items():
        if score > biggest:
            biggest = score
            bp = point
    print(biggest)

    # for i in grid:
    #     print('\t'.join(map(str,i)))





def part_2(data):
    region_size = 0

    for row in range(max(ylist)):
        for column in range(max(xlist)):
            shortest_point = None
            total= 0
            for point, cords in data.items():
                x,y = cords
                distance = abs(x-column)+abs(y-row)
                total+= distance
                if total>10000:
                    break
            if total<10000:
                region_size += 1
    print(region_size)


if __name__ == "__main__":
    main()
