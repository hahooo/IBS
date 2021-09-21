a = []
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        reverse_line = line[::-1]
        a.insert(0, reverse_line)

with open('reverse_test.txt', 'w', encoding='utf-8') as rf:
    rf.writelines(a)

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('reverse_test.txt', 'r', encoding='utf-8') as rf:
    print(rf.read())