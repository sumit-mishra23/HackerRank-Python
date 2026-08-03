import re

if __name__ == "__main__":
    S = input().strip()
    k = input().strip()

    pos = 0
    found = False

    while True:
        m = re.search(k, S[pos:])
        if not m:
            break

        found = True

        start, end = m.span()
        start += pos
        end += pos - 1   

        print((start, end))

        pos = start + 1 

    if not found:
        print((-1, -1))
