print("Hello Git!")
a=5
b=10
print(a+b)
import random

def guess_number_game():
    # Generálj egy véletlenszámot 1 és 100 között
    random_number = random.randint(1, 100)
    
    print("Találd ki a számot 1 és 100 között!")
    
    while True:
        # Kérd be a felhasználó tippjét
        user_guess = int(input("Add meg a tipped: "))
        
        # Számítsd ki a különbséget a tipp és a véletlenszám között
        difference = abs(random_number - user_guess)
        
        if user_guess == random_number:
            print("Gratulálok! Eltaláltad a számot.")
            break
        elif difference <= 10:
            print("Nagyon közel! Próbáld újra.")
        elif difference <= 20:
            print("Közel! Próbáld újra.")
        else:
            print("Messze van! Próbáld újra.")

# Indítsd el a játékot
guess_number_game()