#####KON BANEGA CAROPATI 
question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["four", "nine", "seven", "eight"],
    #second question ke liye options
    ["chandigarh", "bhopal", "chennai", "delhi"],
    #third question ke liye options
    ["software engineering", "counseling", 
    "tourism", "agriculture"]]
s1=[3,4,1]
c1=1
n,u,tr=0,0,0
u1=0
for i in question_list:
    print(i)
    c2=1
    s2=s1[u1]
    for j in options_list:
        if c1==c2:
            g=1
            for k in j:
                print(g,k)
                g+=1
            a=input("do you want 50/50 life line YES or NO \n enter your answer  ")
            if a=="yes" and u==0:
                b=int(input("select one of them ["+str(s2)+"  "+str(c1)+"] enter number  "))
                u=1
                if s1[u1]==b:
                    print("you win")
                else:
                    print("you lost")
                    n=1 
            elif a=="no":
                b=int(input("enter number  "))
                if b==s1[u1]:
                    print("you win")
                else:
                    print("you lost")
                    n=1
            else:
                print("you already used this lifeline")
                b=int(input("enter number  "))
                if s1[u1]==b:
                    print("you win")
                else:
                    print("you lost")
                    n=1 
        c2+=1
    if n==1 :
        break
    c1+=1
    u1+=1