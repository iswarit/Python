import random
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print "Too Low"
        guess = int(raw_input("Enter No. Between 1 and 99: "))
    elif guess > n:
        print "Too high"
        guess = int(raw_input("Enter No. Between 1 and 99: "))
    else:
        print "Correct"
        break
    print
