from GetData import get_input
import string
from collections import deque

def main():
    #data = get_input(9).rstrip()
    # parsed_data = []
    # worth=70950
    # for i in data:
    #     players =int(i.split()[0])

    part_1()
    part_2()


def part_1():
    ans = 0
    num_players =431
    elves = [0] * num_players
    elf_turn = 0
    marbles = [0]
    pos = 0
    worth = 70950
    i =1
    while i <= worth:
        if (i % 10000) == 0:
            print(i, pos)
        if i%23 == 0:
            elves[elf_turn] += i
            pos -= 7
            pos = pos%len(marbles)
            elves[elf_turn] += marbles.pop(pos)
            #print(marbles[pos])
        else:
            #print(pos)
            pos = (pos+1) % len(marbles)+1
            #print(pos)
            marbles.insert(pos, i)
            #print('\t'.join(map(str, marbles)))
            #print()
        #print("[%d] " % (elf_turn+1) + '\t'.join(map(str, marbles)))
        elf_turn = (elf_turn+1)%num_players
        i+=1
    print("Part 1:", max(elves))



def part_2():
    ans = 0
    num_players = 431
    elves = [0] * num_players
    elf_turn = 0
    marbles = deque([0])
    pos = 0
    worth = 7095000
    i = 1
    while i <= worth:
        if (i % 10000) == 0:
            print(i, pos)
        if i % 23 == 0:
            elves[elf_turn] += i
            marbles.rotate(7)
            # print(marbles)
            elves[elf_turn] += marbles.pop()
            marbles.rotate(-1)
            # print(marbles[pos])
        else:
            # print(pos)
            # print(pos)
            marbles.rotate(-1)
            marbles.append(i)
        # print(marbles)
        # print('\t'.join(map(str, marbles)))
        # print()
        # print("[%d] " % (elf_turn+1) + '\t'.join(map(str, marbles)))

        elf_turn = (elf_turn + 1) % num_players
        i += 1

    print("Part 1:", max(elves))


if __name__ == "__main__":
    main()
