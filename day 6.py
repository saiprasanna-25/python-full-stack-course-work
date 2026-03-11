'''
# continue,break,pass
i=20
while i<=30:
    if(i==25):
        pass
    print(i)
    i+=1
i=20
while i<=30:
    if(i==27):
        continue
    print(i)
    i+=1
i=20
while i<=30:
    if(i==25):
        break
    print(i)
    i+=1
# bullets game
bullets = int(input())
while(bullets!=0):
    print(f'{bullets} bullets are left, you can shoot!')
    bullets-=1
else:
    print("game over")
# candy crush Game
moves = int(input())
winning_point=24
while(moves>0):
    if(moves==winning_point):
        print("you win the game")
        break
    print(f'{moves} moves are left, you continue the game')
    moves-=1
else:
    print("game over")
# students attendance system
data = {}
user=int(input("enter no.of students: "))
for i in range(1,user+1,1):
    name=input("enter name: ")
    data[name] = False
print(data)
for name in data:
    print(name)
    status = int(input(f"enter the {name}  status(0-absent,1-Present): "))
    data[name] = bool(status)
print(data)
'''
#Strings
#declaration of strings
#s='python'
s="python"
s+"Language"
print(s)
print(s*10)
print('$'*20)
print(s[4])#o
print(s[-3])#h
names = 'sai prasanna teja kiran ram'
print(names[0])
print(names[-3])
print(names[:13])
print(names[4:13])
print(names[13:18])
print(names[24:])
print(names[-13:-6])
print(names[-9:])
print(names[-1:-4:-1])
print(names[::2])
print('sai' in names)
print(len(s))
print(max(s))
print(chr(95))
print(ord('y'))
print(sorted(names))
print(min(names))
names.replace('teja','teju')
print(names)
print(names)
names.split()
print(names)
s1 = "python programming"
print(s1.center(30,'*'))

print(s1.ljust(40,'&'))
#print(s1)
print(s1.rjust(35,'#'))
#print(s1)
s2 = "          python programming       "
print(s2.strip())
#print(s2)
print(s2.rstrip())
#print(s2)
print(s2.lstrip(s2))
#print(s2)
