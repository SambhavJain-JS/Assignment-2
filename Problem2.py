def choccolets(n):
    print('|',end='')
    for i in range(n):
        print("\U0001F36C",end='')

    print('|')
    print('|',end='')
    for i in range(n):
        print('__',end='')

    print('|')
    print()

def Player_1(n):
    if n!=0:
        x=int(input("how many chocolates you want to remove player_1:"))
        if x==1 or x==2:
            n=n-x
            print('Chocklet Left: ',n)
            choccolets(n)
            return Player_2(n)
    else:
        print("player 2 wins",end='')  
        print("\U0001F389")

def Player_2(n):    
    if n!=0:    
        if n%2==0:
            n=n-2
            print("player 2 took 2 chocolates")
            print('Chocklet Left: ',n)
            choccolets(n)
            return Player_1(n)
        else:
            n=n-1
            print("player 2 took 1 chocolates")
            print('Chocklet Left: ',n)
            choccolets(n)
            return Player_1(n) 
    else:
        print("player 1 wins",end='')
        print("\U0001F389")

quantity=int(input('Enter Quantity: '))
choccolets(quantity)
Player_1(quantity)
