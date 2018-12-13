from GetData import get_input
import string
import collections
import re

def main():


    part_1(4151)
    part_2(4151)



def part_1(data):
    ans=0
    x=[0]*301
    grid = []
    for i in range(301):
        grid.append(x+[])
    three = {}
    for y in range(1,301):
        for x in range(1,301):
            rackid=x+10
            power = rackid
            power*=y
            power += data
            power *= rackid
            print(power)
            if power >= 100:
                power = int(str(power)[-3])
            else:
                power = 0
            print(power, "\n\n")
            power -= 5
            grid[y][x] = power
    largest = 0
    bigboi = None
    for size in range(300):
        print(size,bigboi)
        for y in range(301-size):
            for x in range(301-size):

                count =0
                for i in range(size):
                    for j in range(size):
                        count+=grid[y+i][x+j]
                if count > largest:
                    largest = count
                    bigboi = (x,y,size)
    list1=[]
    print(grid[44][34])
    list1= list(reversed(sorted(list1)))
    print(list1)

    print(bigboi, largest)

    print("Part 1:", ans)





def part_2(data):
    ans = 0
    print("Part 2:", ans)


if __name__ == "__main__":
    main()