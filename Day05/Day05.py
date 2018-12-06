import re
from GetData import get_input
import string

def main():
    data = get_input(5)
    #parsed= map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
    #for _ in parsed:
    #    pass

    part_1(data)
    part_2(data)


def part_1(data):
    destroyed = True
    data = list(data[0].rstrip())
    for fafa in range(10):
        #print(fafa)
        while destroyed:
            length = len(data)-1
            i = 0
            destroyed = False
            while i < length:
                if data[i].lower() == data[i+1].lower() and data[i] != data[i+1]:
                    #print(data[i],data[i+1])
                    data.pop(i)
                    data.pop(i)
                    length -=2
                    destroyed=True
                    i-=1
                else:
                    i+=1

    print(len(data), data)




def part_2(data):
    destroyed = True
    lens = []
    data = data[0]
    for removed_polymer in string.ascii_lowercase:
        data2 = []
        for i in data.rstrip():
            if i.lower() != removed_polymer:
                data2.append(i)

        length = len(data2)-1
        i = 0
        while i < length:
            #print(data2[i - 1:i + 3],"\n")
            if data2[i].lower() == data2[i + 1].lower() and data2[i] != data2[i + 1]:
                # print(data[i],data[i+1])
                #print(data2[i - 1:i + 3])
                data2.pop(i)
                data2.pop(i)
                length -= 2


                i -= 1
                #print(data2[i - 1:i + 3])
            else:
                i += 1

        lens.append(len(data2))
    print(min(lens))

if __name__ == "__main__":
    main()
