must_keys = {"byr","iyr", "eyr","hgt", "hcl","ecl","pid"}
optional_key = {"cid"}
eye_see = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def reader(filename):
    with open(filename) as f:
        content = f.read()

    out1=[x.split() for x in content.split("\n\n")]
    return [dict([y.split(":") for y in x]) for x in out1]

def checker(entries):
    return sum([must_keys.issubset(set(x.keys())) for x in entries])

def legit_checker(entries):
    y= []
    for x in entries:
        if must_keys.issubset(set(x.keys())):
            if (int(x["byr"]) >= 1920 and int(x["byr"]) <= 2002) and \
               (int(x["iyr"]) >= 2010 and int(x["iyr"]) <= 2020) and \
               (int(x["eyr"]) >= 2020 and int(x["eyr"]) <= 2030) and \
               len(x["hcl"]) == 7 and x["hcl"][0] == "#" and \
               len(x["pid"]) == 9 and \
               (x["ecl"] in eye_see):

                if x["hgt"][-2:] == "cm":
                    if int(x["hgt"][:-2]) >=150 and int(x["hgt"][:-2]) <=193:
                        y.append(True)
                elif x["hgt"][-2:] == "in":
                    if int(x["hgt"][:-2]) >=59 and int(x["hgt"][:-2]) <=76:
                        y.append(True)

    return sum(y)

if __name__ == "__main__":
    entries = reader("4.txt")
    print(checker(entries))
    print(legit_checker(entries))
    