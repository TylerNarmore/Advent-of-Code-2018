from GetData import get_input
import string
import collections
import re

def main():
    data = get_input(12)
    parsed_data = []
    initial = data[0].split()[2]
    rules = []
    del (data[1])
    for i in range(1,len(data)):
        parsed_data.append((data[i].rstrip().split()[0],data[i].rstrip().split()[2]))
    for i in parsed_data:
        print(i)

    part_1(initial, parsed_data)
    part_2(initial, parsed_data)



def part_1(initial1, rules):
    #ans=initial1.count('#')
    initial = ['.'] *300
    x=0
    for i in range(100,100+len(initial1)):
        initial[i] = initial1[x]
        x+=1
    ans = initial.count('#')
    for i in range(20):
        print(i, ''.join(initial),sep=": ")

        next_gen =["."]*300
        for pos in range(2, len(initial)-3):

            flag = False
            string = ''.join(initial[pos - 2:pos + 3])
            for rule in rules:


                if string == rule[0]:
                    #print(string, rule[0])
                    next_gen[pos] = rule[1]
                    flag = True
            if not flag:
                next_gen[pos] = '.'

        initial = next_gen+[]

        #ans+=initial.count("#")
    ans = 0
    for i in range(len(initial)):
        if initial[i] == '#':
            ans += i-100


    print("Part 1:", ans)





def part_2(initial1, rules):
    fuck = 0
    # ans=initial1.count('#')
    sides = 500
    mid=250
    initial = ['.'] * sides
    loop_start_index = 0
    for i in range(mid, mid + len(initial1)):
        initial[i] = initial1[loop_start_index]
        loop_start_index += 1
    ans = initial.count('#')
    seen = [''.join(initial).strip('.')]
    count = 0
    while i not in seen:
        print(count, ''.join(initial).rstrip('.').lstrip('.'), initial.count('#'), sep=": ")

        next_gen = ["."] * sides
        for pos in range(2, len(initial) - 3):

            flag = False
            string = ''.join(initial[pos - 2:pos + 3])
            for rule in rules:

                if string == rule[0]:
                    # print(string, rule[0])
                    next_gen[pos] = rule[1]
                    flag = True
            if not flag:
                next_gen[pos] = '.'

        initial = next_gen + []
        if ''.join(initial).strip('.') in seen:
            print(count, ''.join(initial), initial.count('#'), sep=": ")
            loop_start_index = initial.index('#')-mid
            if fuck < 5:
                ans = 0
                for i in range(len(initial)):
                    if initial[i] == '#':
                        ans += i - mid
                print(ans)
            else:
                break
            fuck +=1

            break
        else:
            seen.append(''.join(initial).strip('.'))
        count+=1
    print(loop_start_index,count)
    ans = 0
    a = loop_start_index
    adds = ((50000000000 - 121)*42)+5510
    print(adds)


# TOO LOW: 2,099,999,994,960
# TOO HIGH 2100000012650

    print("Part 2:", ans)

if __name__ == "__main__":
    main()