from GetData import get_input
import string
import collections
import re
import time
import array
from copy import deepcopy
def main():
    data = get_input(10)
    parsed_data = []

    parsed = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

    i = 1
    xl=[]
    yl=[]
    for x, y,v1,v2 in parsed:
        parsed_data.append(([x, y],(v1,v2)))
        xl.append(x)
        yl.append(y)
        i += 1

    part_1(parsed_data)
    part_2(parsed_data)



def part_1(data):
    file = open("TEST.txt", 'w')
    points = []
    for i in data:
        points.append(i[0])
    ranges_y = []
    ranges_x = []
    for second in range(20000):
        x_list = []
        y_list =[]

        for point in range(len(points)):

            x_list.append(points[point][0] +data[point][1][0]*second)

            y_list.append(points[point][1] + data[point][1][1]*second)
        ranges_y.append(max(y_list)-min(y_list))
        ranges_x.append(max(x_list)- min(x_list))


    x= ranges_x.index(min(ranges_x))
    print(x)
    x_list = []
    y_list = []
    for point in range(len(points)):
        x_list.append(points[point][0] + data[point][1][0] * x)
        points[point][0] =points[point][0] + data[point][1][0] * x
        y_list.append(points[point][1] + data[point][1][1] * x)
        points[point][1] =points[point][1] + data[point][1][1] * x

    for i in range(min(y_list),max(y_list)+1):
        for j in range(min(x_list),max(x_list)+1):
            if([j,i] in points):
                print("#",end='')
            else:
                print(' ',end='')
        print()






def part_2(data):
    ans = 0
    print("Part 2:", ans)


if __name__ == "__main__":
    main()
