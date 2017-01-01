c = [1,2,3]
d= [3,4,5]

for i in c:
    if i in d:
        print("볼입니다")

        while True:
            d = goguess()
            if c[0] == d[0]:
                pp = pp + 1
                print("{}스트라이크입니다.".format(pp))
            elif c[0] in d:
                ap = ap + 1
                print("{}볼입니다".format(ap))
            else:
                print("{}스트라이크{}볼 입니다".format(pp, ap))