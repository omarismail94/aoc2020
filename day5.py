
def find_pos(string,back_char, front_char, length): 
    try:
        if string[0] != back_char and string[0] != front_char:
            return int(length[0])
    except IndexError:
        return int(length[0])


    if string[0] == back_char:
        return find_pos(string[1:],back_char,front_char, (length[0],(length[0]+length[1]+1)/2-1))
    else:
        return find_pos(string[1:], back_char,front_char, ((length[0]+length[1]+1)/2,length[1]))

def max_id(content):
    maxy = 0
    for x in content:
        row = find_pos(x, "F", "B", (0,127))
        col = find_pos(x[-3:], "L", "R", (0,7))
        if row *8+col >= maxy:
            maxy = row*8+col
    
    return maxy 

def who_id(content):

    ids = set()
    for x in content:
        row = find_pos(x, "F", "B", (0,127))
        col = find_pos(x[-3:], "L", "R", (0,7))
        ids.add(row*8+col)


    for i in range(min(ids),max(ids),1):
        if not {i,i+1,i+2}.issubset(ids):
            return i+2

    return 0 


if __name__ == "__main__":
    with open("5.txt") as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]    
    print(max_id(content))
    print(who_id(content))
    


