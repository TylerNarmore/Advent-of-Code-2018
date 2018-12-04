import re
import datetime
from GetData import get_input


def main():
    data = get_input(4)
    x = []
    #parsed= map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
    #for _ in parsed:

    part_1(data)
    part_2(data)


def part_1(x):
    cur_guard = None
    guards = {}
    times = {}
    for i in x:
        sp = i.split('] ')
        time = sp[0][1:]
        action = sp[1]
        time = (datetime.datetime.strptime(time, "%Y-%m-%d %H:%M"))
        times[time] = action
    for time in sorted(times.keys()):
        # print(time, times[time])
        action = times[time]
        if action.split()[0] == "Guard":
            cur_guard = int(action.split()[1][1:])
            if cur_guard not in guards:
                guards[cur_guard] = [0] * 60

        if action.split()[0] == "falls":
            sleep_start = time
        if action.split()[0] == "wakes":
            time1 = sleep_start
            for min in range(sleep_start.minute, time.minute):
                guards[cur_guard][min] += 1
            # print(sleep_start, time)
            # print(time1)
    max_minute = 0
    worst_guard = 0
    for i in guards:
        if max_minute < sum(guards[i]):
            worst_guard = i
            max_minute = sum(guards[i])

    print(worst_guard * guards[worst_guard].index(max(guards[worst_guard])))


def part_2(x):
    cur_guard = None
    guards = {}
    times = {}
    for i in x:
        sp = i .split('] ')
        time = sp[0][1:]
        action = sp[1]
        time = (datetime.datetime.strptime(time,"%Y-%m-%d %H:%M"))
        times[time] = action
    for time in sorted(times.keys()):
        #print(time, times[time])
        action = times[time]
        if action.split()[0] == "Guard":
            cur_guard = int(action.split()[1][1:])
            if cur_guard not in guards:
                guards[cur_guard] = [0] * 60


        if action.split()[0] == "falls":
            sleep_start = time
        if action.split()[0] == "wakes":
            time1 = sleep_start
            for min in range(sleep_start.minute, time.minute):
                guards[cur_guard][min] += 1
            #print(sleep_start, time)
            #print(time1)
    max_minute = 0
    worst_guard = 0
    for i in guards:
        if max_minute < max(guards[i]):
            worst_guard = i
            max_minute = max(guards[i])

    print(worst_guard*guards[worst_guard].index(max_minute))





if __name__ == "__main__":
    main()
