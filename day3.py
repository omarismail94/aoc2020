# read input
# create matrix 
# find # of columns
# collapse to one row
# cout 3+ num_col

def readInput(filename, right):
    with open(filename) as f:
        content = f.readlines()
    
    world = [x.split() for x in content]
    num_col = len(world[0][0])
    num_row = len(world)

    multiplier = num_row//(num_col//right)

    world = []
    for x in content:
        listed_row = list(x.split()[0])
        world.extend(listed_row*multiplier)

    return world, num_col*multiplier, num_row

def countTrees(world: list, num_col: int, num_row: int, right: int, down=1):
    count = 0
    i = 0
    while i < len(world) - num_col*down-right:
        if world[i + right + num_col*down] == '#':
            count +=1
        i += right + num_col*down
    return count


if __name__ == "__main__":
    max_right = 7
    world, num_col, num_row = readInput("3.txt",max_right) 
    const = world, num_col, num_row
    print(countTrees(*const, 1)*countTrees(*const, 3)*countTrees(*const, 5)*countTrees(*const, 7)*countTrees(*const,1,2))