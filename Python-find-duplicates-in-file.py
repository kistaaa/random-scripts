#input is a .txt file with 1 word per line

with open('D:/words.txt') as file:
    
    lines = (line.rstrip() for line in file) # All lines including the blank ones
    lines = (line for line in lines if line) # Non-blank lines
    
    seen = set()
    duplis = set()
    for word in lines:
        if word in seen:
            duplis.add(word)
        else:
            seen.add(word)
    for word in duplis:
        print(word + ' is duplicate')
