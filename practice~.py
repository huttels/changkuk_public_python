money = 10
coffee = 2
coin = 0
while money > 0:
    money = money - 1
    coin = coin + 1
    print("동전을 넣었습니당.")

    if coin == 3 :             #왜 == 써야됨?? ㅅㅂ?? 문자 랑 숫자라?
        coffee = coffee - 1
        coin == 0
        print("커피가 나왔습니당.")
    elif coffee <= 0 :
        print("장사끝났어염 뿌우")
        break