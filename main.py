import random
from gamedata import game_data

# Globals to hold A, B, and score
a = {}
b = {}
current_score = 0

def print_AB():
    """Print A vs B comparison without revealing scores"""
    print(f"\nA: {a['name']}, a {a['profession']} from {a['country']} (Score: ???)")
    print("VS")
    print(f"B: {b['name']}, a {b['profession']} from {b['country']} (Score: ???)")

def guess_compare():
    global current_score, a, b
    guess = input("Who is higher? (type 'a' or 'b'): ").lower().strip()
    
    if guess not in ["a", "b"]:
        print("❌ Invalid input. Please type 'a' or 'b'.")
        return True  # Let them retry

    # Determine if guess is correct
    correct = (guess == "b" and b["score"] > a["score"]) or \
              (guess == "a" and a["score"] > b["score"])

    if correct:
        current_score += 1
        print(f"\n✅ Correct!")
        print(f"{a['name'] if guess == 'a' else b['name']} has the higher score.")
        print(f"🎯 Your score: {current_score}")
        a = b  # Promote B to be the new A
        return True
    else:
        print(f"\n❌ Wrong!")
        print(f"You guessed '{guess}', but:")
        print(f"A: {a['name']} — {a['score']}")
        print(f"B: {b['name']} — {b['score']}")
        print(f"🏁 Final score: {current_score}")
        return False  # ← this ends the game loop

def score():
    """Print current score"""
    print(f"🏆 Your final score was: {current_score}")

def game():
    """Main game logic"""
    global a, b, current_score
    current_score = 0
    print("\n🎮 Welcome to Higher or Lower!")
    print("Guess who has the higher score (fame, followers, or worth).")

    a = random.choice(game_data)
    b = random.choice(game_data)
    while b == a:
        b = random.choice(game_data)

    playing = True
    while playing:
        print_AB()
        playing = guess_compare()
        if playing:
            b = random.choice(game_data)
            while b == a:
                b = random.choice(game_data)
    score()

def restart():
    """Ask the user if they want to play again"""
    while True:
        again = input("🔁 Do you want to play again? (Yes/No): ").strip().lower()
        if again == "yes":
            return True
        elif again == "no":
            print("👋 Thanks for playing!")
            return False
        else:
            print("❌ Please type 'Yes' or 'No'.")

def main():
    while True:
        game()
        if not restart():
            break

# Start here
if __name__ == "__main__":
    main()
