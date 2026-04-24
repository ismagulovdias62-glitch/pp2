# Reading files

with open("sample.txt", "r", encoding="utf-8") as f:
    print("READ():")
    print(f.read())

with open("sample.txt", "r", encoding="utf-8") as f:
    print("READLINE():")
    print(f.readline())

with open("sample.txt", "r", encoding="utf-8") as f:
    print("READLINES():")
    print(f.readlines())