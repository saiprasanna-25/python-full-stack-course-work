'''1
dict={'rice':60,'wheat':45,'sugar':40}
list=['rice','wheat','sugar']
l=list()1
for i in range(3):
    l=l.append(int(input()))
for j in l:
    if(j==0):
        sum=+dict['rice']
    elif(j==1):
        sum+=dict['wheat']
    else:
        sum+=dict['sugar']
'''
'''
store={
    1:{"rice",60},
    2:{"wheat",45},
    3:{"sugar",40}}
print(store)
print("enter the product indexes you want to buy")
l=list()
while True:
    user=input()
    if(user=='done'):
        break
    else:
        l.append(int(user))
sum=0
for i in l:
    sum+=store[i][1]
print(sum)
print('index'.ljust(6),'products'.ljust(15),'price'.ljust(6))
'''
'''
products=['rice','sugar','wheat','milk','eggs']
prices=[60,45,40,20,70]
print("------welcome to grocery store------")
print("Here are the available products:\n")
print('index'.ljust(6,' '),'products'.ljust(15,' '),'price'.ljust(6,' '))
for i in range(5):
    print(str(i+1).ljust(6,' '),products[i].ljust(15,' '),str(prices[i]).ljust(6,' '))
items=list(map(int,input("enter the indexes:").split()))
print("selected items")
total_amount=0
for item in items:
    print(products[item-1],prices[item-1])
total_amount+=prices[item-1]
print("total amount to pay ",total_amount," thank you for visiting")
'''
'''
uses of functions:reuse,reduce code,debug,read,module,collab,effective,abstract,flexibility,duplication reduce
function is a reusable block of code instead of writing same code we use functions

'''
'''
def wish(name):
    print(f' hello {name}, wlecome to "python 100 days of program"')
wish('teju')
wish('akhi')
wish('prassu')
'''
def display(username,email,password):
    print("username:",username)
    print("email",email)
    print("password",password)
display('prasanna','prasanna@gmail.com','s@1536')#position arguments
display(email='prasanna@gmail.com',password='s@1536',username='prasanna')#keyword arguments
