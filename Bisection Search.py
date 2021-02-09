
high = 100
low = 0
guess = (high + low) / 2 #gerizekali neden?
status = ""

print("Please think of a number between 0 and 100!")

while status != "c":
    print("Is your secret number", guess, "?")
    status = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
# data updates everytime user asks for a second one
    if status == "h".lower():
        high = guess
        guess = int((high + low) / 2)
    elif status == "l".lower():
        low = guess
        guess = int((high + low) / 2)
    elif status == "c".lower():
        break
    else:
        print("Try again.")
        continue
        
print("GG WP. Your secret number was: ", guess)