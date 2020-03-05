def course_elephants0(n, l, v, p):
    mn = float(float(l - p[0]) / float(v[0]))
    pos = int(0)
    for i in range(1, len(v)):
        temp = float(float(l - p[i]) / float(v[i]))
        if (temp < mn):
            mn = temp
            pos = i
    print(pos)


n = int(input())
l = int(input())
v = list(map(int, input().split()))
p = list(map(int, input().split()))
course_elephants0(n, l, v, p)
