def reader(filename):
    with open(filename) as f:
        content = f.readlines()
    
    return {x.strip():None for x in content}

def summer(content: dict) -> int:
    for x in content:
        remainder = str(2020-int(x))
        if remainder in content:
            print(x, remainder)
            return int(x)*(2020 - int(x))


def threesummer(content: dict) -> int:
    for x in content:
        remainder = 2020-int(x)
        for y in content:
            second_rem = str(remainder-int(y))

            if second_rem in content:
                 print(x, y, second_rem)
                 return int(x)*int(y)*int(second_rem)


if __name__ == "__main__":
    content = reader("1.txt")
    print(summer(content))
    print(threesummer(content))

# a+b = remainder
