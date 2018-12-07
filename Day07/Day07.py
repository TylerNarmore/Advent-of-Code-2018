from GetData import get_input
import string

# Sorry to whoever is looking at this one
def main():
    data = get_input(7)
    x = []
    for i in data:
        x.append((i.split()[1], i.split()[-3]))

    part_1(x)
    part_2(x)


def part_1(data):
    dict1 = {}
    has_prereq = []
    for i in data:
        if i[0] not in dict1:
            dict1[i[0]] = [i[1]]
        else:
            dict1[i[0]].append(i[1])
        if [i[1]] not in has_prereq:
            has_prereq.append(i[1])

    tiers = []
    tier_rank = 0
    dict1["Y"] = []
    while len(dict1) > 0:
        tiers.append([])
        delete = []

        for i in sorted(dict1.keys()):
            if not (i in has_prereq):
                tiers[tier_rank].append(i)
                delete.append(i)
                break

        for i in delete:
            del (dict1[i])
        has_prereq = []
        for i in dict1:
            for letter in dict1[i]:
                if letter not in has_prereq:
                    has_prereq.append(letter)
        tier_rank += 1
    print("Part 1: ", end='')
    for i in tiers:
        i.sort()
        for l in i:
            print(l, end='')
    print()


def part_2(data):
    dict1 = {}
    has_prereq = []
    for i in data:
        if i[0] not in dict1:
            dict1[i[0]] = [i[1]]
        else:
            dict1[i[0]].append(i[1])
        if [i[1]] not in has_prereq:
            has_prereq.append(i[1])
    dict1["Y"] = []
    task_time = {}
    for i in range(len(string.ascii_uppercase)):
        task_time[string.ascii_uppercase[i]] = i+61

    workers = []

    tiers = []
    tier_rank = 0
    time = 0
    while len(dict1) > 0:
        tiers.append([])

        for i in sorted(dict1.keys()):
            if not (i in has_prereq):
                if len(workers) < 5:
                    flag =True
                    for worker in workers:
                        if i == worker[0]:
                            flag = False
                    if flag:
                        workers.append([i, 0])
                else:
                    break

        # Adds seconds to workers task
        workers = sorted(workers, key=lambda l: task_time[l[0]] - l[1])
        while workers[0][1] < task_time[workers[0][0]]:

            for worker in range(len(workers)):
                workers[worker][1] += 1
            time += 1

        del (dict1[workers[0][0]])
        workers.pop(0)

        has_prereq = []
        for i in dict1:
            for letter in dict1[i]:
                if letter not in has_prereq:
                    has_prereq.append(letter)
        tier_rank += 1
    print("Part 2:", time)

if __name__ == "__main__":
    main()
