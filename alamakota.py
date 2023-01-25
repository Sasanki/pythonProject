with open('file.txt', encoding="utf-8") as f:
    for line in f:
        print(line)

with open('file.txt',encoding="utf-8") as f:
    lines = f.readlines()
    for line in f:
        print(line)
