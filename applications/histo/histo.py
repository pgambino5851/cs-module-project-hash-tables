def word_count(s):
    tr = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(tr).lower()
    words = s.split()
    counts = {}
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1
    return counts

with open("robin.txt") as f:
    d = f.read()

counts = list(word_count(d).items())

max_len = 0
for c in counts:
    ln = len(c[0])
    if ln > max_len:
        max_len = ln

counts.sort(key=lambda e: (-e[1], e[0]))

for c in counts:
    print(f'{c[0]:{max_len}}  ', end='')
    for _ in range(c[1]):
        print(f'#', end='')
    print()