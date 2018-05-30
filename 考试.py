def shu_zi():
    e=0
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                if (a!=b) and (a!=c) and (b!=c):
                    print(a,b,c)
                    e=e+1
    print(e)
shu_zi()

