def main():
    f = open("input.txt", 'r')

    x = []
    
    for i in f:
        x.append(i)

    part_1(x)
    part_2(x)
    
        

def part_1(x):
    c=0
    for i in x:
        c+=int(i)
    print(c)

def part_2(x):
    c=0
    y={0:True}
    a=False
    while True:
        for i in x:
            c+=int(i)
            if c in y:
                a=True
                print(c)
                break
            else:
                y[c] = True
        if a:
            break
        
if __name__ == "__main__":
    main()
