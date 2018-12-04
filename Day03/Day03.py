from GetData import get_input


def main():
    f=get_input(3)

    x = {}
    
    for i in f:
        claim = i.rstrip()[1:].split()
        x[int(claim[0])] = (list(map(int,claim[2][:-1].split(','))), list(map(int,claim[3].split('x'))))
        #print((list(map(int,claim[2][:-1].split(','))), list(map(int,claim[3].split('x')))))

    part_1(x)
    part_2(x)

def part_1(x):
    two_or_more = {}
    fabric_squares = {}
    for claim in x:
        for i in range(x[claim][0][0],x[claim][0][0]+x[claim][1][0]):
            for j in range(x[claim][0][1],x[claim][0][1]+x[claim][1][1]):
                if (i,j) in fabric_squares:
                    if (i,j) not in two_or_more:
                        two_or_more[(i,j)] = True
                else:
                    fabric_squares[(i,j)] = True
            
    print(len(two_or_more))

def part_2(x):
    two_or_more = {}
    fabric_squares = {}
    no_overlap = {}
    for claim in x:
        for i in range(x[claim][0][0],x[claim][0][0]+x[claim][1][0]):
            for j in range(x[claim][0][1],x[claim][0][1]+x[claim][1][1]):
                if (i,j) in fabric_squares:
                    if (i,j) not in two_or_more:
                        two_or_more[(i,j)] = True
                    fabric_squares[(i,j)] += 1
                        
                else:
                    fabric_squares[(i,j)] = 1
                    
    for claim in x:
        test =True
        for i in range(x[claim][0][0],x[claim][0][0]+x[claim][1][0]):
            for j in range(x[claim][0][1],x[claim][0][1]+x[claim][1][1]):
                if fabric_squares[(i,j)] == 1:
                    continue
                else:
                    test = False
                    break
            if not test:
                break
        if test:
            print(claim)
            break
        
if __name__ == "__main__":
    main()
    
