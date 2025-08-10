import random

def is_valid(guess):
    if len(guess)==4:
        if len(guess)==len(set(guess)):
            return True
    return False

def calculate(secret, guess):
    bull=0
    for i in range(len(guess)):
        if secret[i]==guess[i]:
            bull+=1

    cow=0
    for i in guess:
        if i in secret:
            cow+=1
    cow=cow-bull
    return [bull,cow]

l=['1','2','3','4','5','6','7','8','9','0']
#secret=''.join(random.sample(l,4))
secret='1549'
while True:
    guess=int(input("Enter your 4 digit number: "))
    
    if not is_valid(str(guess)):
        print("Invalid number: Try Again\n")
        continue

    bull_cow=calculate(str(secret), str(guess))
    if bull_cow[0]==4:
        print(f"!!You win!!\nThe secret number: {secret}")
        break
    else:
        print(f"Bulls: {bull_cow[0]}\nCows: {bull_cow[1]}\n")
        
