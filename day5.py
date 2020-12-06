def converter(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.replace("F","0").replace("B","1").replace("R","1").replace("L","0").strip() for x in content]  
    return {int(x[:7], 2)*8 + int(x[-3:], 2) for x in content}
 

if __name__ == "__main__":
    content = converter("5.txt")
    print(max(content))
    print(set(range(min(content),max(content))) - content)
    


