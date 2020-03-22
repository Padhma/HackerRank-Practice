
Da, Ma, Ya = map(int,input().split())

De, Me, Ye = map(int,input().split())

if Ya > Ye:
    print(10000)
elif Ya == Ye and Ma > Me:
    print(500 * (Ma - Me))
elif Ma == Me and Ya == Ye and Da > De:
    print(15 * (Da - De))
else:
    print(0)
    