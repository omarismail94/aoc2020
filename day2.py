def reader(filename):
    with open(filename) as f:
        content = f.readlines()
    
    return [x.replace(":","").replace("-"," ").split() for x in content]

def validator(content: list):

    valid = 0
    for x in content:
        occurence_count = x[-1].count(x[-2])
        if occurence_count <= int(x[1]) and occurence_count >= int(x[0]):
            valid +=1

    return valid

def xor(content: list):
    return sum([True for x in content if (x[-1][int(x[0])-1] == x[2]) != (x[-1][int(x[1])-1] == x[2])])

if __name__ == "__main__":
    content = reader("2.txt")
    print(validator(content))
    print(xor(content))