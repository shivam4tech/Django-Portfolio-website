from collections import Counter
import random


def name(got_name):
    got_name = got_name.lower()
    file = open("mysite/static/mysite/names_file/indian_men")

    l = file.readlines()
    s = [0]*len(l)
    for i in range(len(l)):
        s[i] = l[i].split(' ')[0]

    counts = Counter(s)
    # print(len(counts))

    file.close()
    file1 = open("mysite/static/mysite/names_file/indian_female")
    l1 = file1.readlines()
    s1 = [0] * len(l1)
    for i in range(len(l1)):
        s1[i] = l1[i].split(' ')[0]

    counts1 = Counter(s1)
    file1.close()
    c = counts + counts1
    # print(counts)
    res = (c[got_name] / len(c)) * 125000000
    if res >= 10000:
        return str(int(res))
    elif res == 0.0:
        for i in range(len(c)):
            y = list(c.elements())[i]
            a = lcs(got_name, y, len(got_name), len(y))
            if a >= len(got_name) - 1:
                res = (c[y] / len(c)) * 125000000
                return str(int(res))
    res = random.randint(5000, 10000)
    return str(int(res))


def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1);
    else:
        return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n));