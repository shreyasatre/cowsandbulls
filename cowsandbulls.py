import random

# Four digit code with no repeating digits.
def get_code():
    n = 0
    while len(set(list(str(n)))) != 4:
        n = random.randint(1000, 9999)
    return n
# ---

# Main.
def main():    
    code = get_code()
    used_codes = set()
    used_codes.add(code)
    guess = "0000"
    tries = 0

    # Get unused code.
    while code not in used_codes:
        code = get_code()

    print("Cows and Bulls - Guess the Four Digits")

    while True:
        cow, bull = 0, 0
        guess = input(" ")
        tries += 1
        
        if guess == "reveal":
            print(f"Code was {code}")
            break

        if len(set(list(str(guess)))) != 4:
            print("guess must have four unique digits")
        elif int(guess) < 1000:
            print("guess must be between 1000 and 9999")        
        else:
            if guess == str(code):
                print(f"Correct in {tries} tries!")
                break
            
            for i in range(4):
                # Check if each digit in the guess is in the right place
                if str(guess[i]) == str(code)[i]:
                    bull += 1
                # If not the right place, check if digit is elsewhere.
                elif str(guess[i]) in str(code):
                    cow += 1
            
            print(f"{cow} cow(s), {bull} bull(s)")
# ---
            
if __name__ == "__main__":
    main()
# ===