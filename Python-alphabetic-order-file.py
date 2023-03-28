#file is a .txt with 1 word per line

arquivo = 'D:/words.txt'

with open(arquivo, 'r+', encoding='utf8') as f:
    print('Opened file')
    lines = f.read().splitlines()
    lines.sort()
    f.seek(0)
    f.truncate()
    for word in lines:
        f.write(word + '\n')
    print('Saved file')
print('Done')
