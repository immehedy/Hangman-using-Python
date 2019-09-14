import random

word=["apple", "man", "good"]
turn=0
alphabet="abcdefghijklmnopqrst"
guess=[]
letter=[]

name=input("Enter Your Name:")

while name =="":
    name = input("Enter Your Name please:")

selected_word=random.choice(word)

length=len(selected_word)




for x in range(length):
    guess.append("_")

print("The word has length of ", length)
print(guess)
while turn<5:
    guess_word=input("Guess a word, one character each time:").lower()
    if guess_word in alphabet:
        if guess_word in letter:
            print("you have already guessed that")
        else:
            letter.append(guess_word)
            for y in range(0, length):
                if guess_word== selected_word[y]:
                    guess[y]=guess_word

            if guess_word in guess:
                print("you guessed right")
            else:
                print("guess again")
            print(guess)
            if not '_' in guess:
                print("you won!!!")
                break;


    else:
        print("guess an alphabet")

    turn+=1

if '_' in guess:
    print("Game Over")
    print("You loose")





