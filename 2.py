print( '''
     Write a python program that computes the net amount of a bank account based a transaction log from console input. 
    The transaction log format is shown as following: 
    D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program: 
    D 300 , D 300 , W 200 , D 100 ,
    Then, the output should be: 500
   ''')

def deposit(num):
    global balance
    balance =balance+num

def withdrawal(num):
    global balance
    if(balance >0):
        balance=balance-num
    else:
        print("Withdraw not possible because balance is less.")



list1 = []

balance=0
while True:
    data = input("Please enter the transaction details:")
    if ('Exit' == data):
        break
    list1.append(data.split())
print(list1)

for var in list1:
    if(var[0]=='D'):
        deposit(int(var[1]))
    elif (var[0]=='W'):
        withdrawal(int(var[1]))


print("Balance =",balance)
