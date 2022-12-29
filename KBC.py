print("\033[95m""\t   ARE you ready")
re = input("do want to play :- ")
if re=="yes":
    print("\twelcome to K.B.C game")
am=0
Qu =["\033[94m""1.Who is the first citizen of India","\033[94m""2.Name the planet known as the Red Planet?","\033[94m""3.How many seconds make one hour?","\033[94m""4.Which is the tallest mountain in the world?","\033[94m""5.Which continent is known as the Dark continent?"]
op= ["\n1.pm\n2.cm\n3.precedent\n4.mla\n5.life line"],["\n1.earth\n2.mars\n3.moon\n4.vinus\n5.life line"],["\n1.3656\n2.3665\n3.3601\n4.3600\n5.life line"],["1.himaliya","2.maunt evrest","3.triund","4.rising star\n5.life line"],["1.south Africa","2.Africa","3.usa","4.uae\n5.life line"]
sol=[3,2,4,2,2,]
life_line=["1.50_50","2.audiance poll","3.phone a friend","4.skip question"]
for i in range(len(Qu)):
    print('\33[m',Qu[i])
    for j in op[i]:
        print('\033[93m',j)
    user = int(input("enter your answer:- "))
    if user==sol[i]:
        print("'\033[92m'correct answer")
        print("you won 1000")
        am = am+1000
        print("your am is ",am)
        continue
    elif user==5:
        for f in life_line:
            print(f)
        demand=int(input("choose your life line "))
        if demand==1:
            print(life_line.pop(0))
        elif demand==2:
            print(life_line.pop(1))
        elif demand==3:
            print(life_line.pop(2))
        else:
            print(life_line.pop(3))
        if demand ==1 :
            print("optiono are:",sol[i],"and 1")
            user = int(input("now choose any one this "))
            if user==sol[i]:
                print("'\033[92m'correct answer")
                print("you are won 1000")
                am = am+1000
                print(am)
            else:
                print("'\033[91m'wrong")
        elif demand == 2:
            print(sol[i],"= 70%,other option = 30%")
            user = int(input("enter choose any option "))
            if user==sol[i]:
                print("'\033[92m'correct answer")
                print("you won 1000")
                am =am+1000
                print(am)
            else:
                print("'\033[91m'wrong")
        elif demand == 3:
            print("your friend suggestion is ",sol[i])
            user = int(input("enter choose any option "))
            if user==sol[i]:
                print("'\033[92m'correct answer")
                print("you won 1000")
                am =am+1000
                print(am)
            else:
                print("'\033[91m'wrong")
        else:
            break
    else:
        print("'\033[91m'wrong answer")
        continue
