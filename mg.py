import random
 
 

num = random.randrange(1000, 10000)
 
n = int(input("Guess the 4 digit number:"))
 

if (n == num):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    count = 0
    while (n != num):
        count += 1
        attemps = 0
        n = str(n)
        num = str(num)
        correct = ['X']*4
        for i in range(0, 4):
            if (n[i] == num[i]):
                attemps += 1
                correct[i] = n[i]
            else:
                continue
        if (attemps < 4) and (attemps != 0):
            print("Not quite the number. But you did get ",
                  attemps, " digit(s) correct!")
          
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=' ')
            print('\n')
            print('\n')
            n = int(input("Enter your next choice of numbers: "))
        elif (attemps == 0):
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))
    if n == num:
        count+=1
        print("the actual number is", num)
        print("It took you only", count,"tries.")