x = input()
y = len(x)
l = []
for i in range(len(x)):
    if x[i].isalnum() and x[i-1] == x[i]:
        l.append(x[i])
if len(l) != 0:
    print(l[0])
else:
    print(-1) 
