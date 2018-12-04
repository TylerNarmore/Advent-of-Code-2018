def main():
    f = open("input.txt", 'r')

    x = []
    
    for i in f:
        x.append(i)

    part_1(x)
    part_2(x)


def part_1(x):
    linesdict = {}
    for line in x:
        counts = {}
        for letter in line:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        two =  0
        three = 0
        for letter in counts:
            if counts[letter] == 2:
                two = 1
            if counts[letter] == 3:
                three = 1
        linesdict[line] = [two, three]
    twos=0
    threes=0
    for line in linesdict:
        twos += linesdict[line][0]
        threes+=linesdict[line][1]
    print(twos*threes)

def part_2(x):
    x.sort()
    for i in range(len(x)-1):
        diff = 0
        for char in range(len(x[i])):
            if x[i][char] != x[i+1][char]:
                diff += 1
            if diff >= 2:
                continue
        if diff ==1:
            print(x[i], x[i+1],sep="")
            
        
if __name__ == "__main__":
    main()
