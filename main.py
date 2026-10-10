import random

def get_secret():
    nums = list(range(10))
    random.shuffle(nums)
    if nums[0] == 0:
        nums[0], nums[1] = nums[1], nums[0]
    return "".join(str(n) for n in nums[:4])

def score_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

def play():
    secret = get_secret()
    tries = 0

    print("Welcome to Bulls and Cows!")
    print("Try to guess the 4-digit number (no repeating digits).")

    while True:
        try:
            guess = input("Your guess: ").strip()
        except (EOFError, OSError):
            print("\nInput stream closed. Exiting game.")
            break

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter 4 unique digits.")
            continue

        tries += 1
        bulls, cows = score_guess(secret, guess)

        if bulls == 4:
            print(f"You got it! The number was {secret}. Took you {tries} tries.")
            break

        print(f"Bulls: {bulls}, Cows: {cows}")

if __name__ == "__main__":
    play()