from GetData import get_input
import string

def main():
    data = get_input(8)
    parsed_data = []

    for i in data:
        parsed_data = list(map(int,i.split()))

    part_1(parsed_data)
    part_2(parsed_data)


def get_node_info(data):
    children = data[0]
    num_metadata = data[1]
    meta_sum = 0
    off_set = 2
    if children != 0:
        i=0
        while i < children:
            temp_meta,temp_offset = get_node_info(data[off_set:])
            off_set +=temp_offset
            meta_sum += temp_meta
            i+=1



    for i in range(num_metadata):
        meta_sum += data[i + off_set]
    off_set = num_metadata + off_set

    return meta_sum, off_set


def part_1(data):
    print("Part 1:", get_node_info(data)[0])


def get_node_value(data):
    children = data[0]
    num_metadata = data[1]

    children_vals = [0] * data[0]

    meta_sum = 0
    off_set = 2
    if children != 0:
        i = 0
        while i < children:
            temp_value, temp_offset = get_node_value(data[off_set:])
            off_set += temp_offset
            children_vals[i] = temp_value
            i += 1
    value = 0
    if children > 0:
        for i in range(num_metadata):
            if data[i + off_set]>children:
                pass
            else:

                value += children_vals[data[i + off_set]-1]
    else:
        value = get_node_info(data)[0]
    off_set = num_metadata + off_set
    return value, off_set


def part_2(data):
    print("Part 2:", get_node_value(data)[0])


if __name__ == "__main__":
    main()
