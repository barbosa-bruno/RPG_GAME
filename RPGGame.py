import random

# Get protagonist's name
characterName = input("What is your brave protagonist's name? ")

# Initialize character health
health = 100

def check_health():
    """Check the protagonist's current health."""
    print(f"\n{characterName}'s current health: {health} HP")
    if health <= 0:
        print(f"{characterName} has fallen in battle. The journey ends here.")
        return False
    return True

print("Paths of Destiny: The Rise of the Black King")
print()

print("Prologue: A Shadow Stirs")
print("In the kingdom of Argathor, peace has reigned for centuries, but whispers of a long-forgotten prophecy have begun to stir. A dark force, known only as the Black King, is rumored to be rising once again, bent on conquering the world.")
print(f"The protagonist, {characterName}, an orphan raised by the kingdom's greatest warriors, embarks on a journey to uncover the truth behind these dark whispers and protect the realm from destruction.")

print(f"{characterName} discovers that an ancient artifact—the Soulstone—has been unearthed by the Black King's minions, granting him unnatural powers.")
print("The protagonist must find the Soulstone before the Black King does, but a deep moral conflict brews: Should they use its power to defeat the Black King, or destroy it to prevent its corruption?")

# Path selection loop
while True:
    pickPath = input("What path would you like to follow? (light, shadow, neutral) ").lower()
    if pickPath in ["light", "shadow", "neutral"]:
        print(f"You have chosen the {pickPath} path!")
        pathChosen = pickPath  # Store the chosen path
        break
    else:
        print("Invalid choice. Please type 'light', 'shadow', or 'neutral'.")

print()
print()
print()

# Act I: The Journey Begins
print("Act I: The Journey Begins")
print(f"{characterName} sets off toward the mountains where the Soulstone is believed to be hidden.")
print("Along the way, they encounter a mysterious hermit who offers them a choice: take the enchanted map to the Soulstone's location, or walk without guidance, relying on their own instincts.")
print("What do you choose?")

while True:
    mapChoice = input("Do you take the map? (yes or no) ").lower()
    if mapChoice == "yes":
        print(f"{characterName} takes the map, which leads them safely through treacherous lands, avoiding many dangers.")
        mapTaken = True
        break
    elif mapChoice == "no":
        print(f"{characterName} decides to rely on their instincts, facing many challenges along the way but learning valuable survival skills.")
        mapTaken = False
        break
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")

# New Side Quest: The Bandits in the Forest
print("\nWhile traveling through a dense forest, {characterName} encounters a group of bandits blocking the path. The bandits demand a toll to pass.")
print("Do you fight them or try to negotiate with them?")

while True:
    banditChoice = input("Do you fight or negotiate? (fight/negotiat) ").lower()
    if banditChoice == "fight":
        print(f"{characterName} draws their sword and engages in a fierce battle with the bandits, eventually defeating them.")
        health -= 10  # Lost some health in the battle
        break
    elif banditChoice == "negotiate":
        print(f"{characterName} tries to talk their way through. The bandits are convinced by their charm and allow safe passage.")
        break
    else:
        print("Invalid choice. Please type 'fight' or 'negotiate'.")

# Act II: The Soulstone's Power
print("\nAct II: The Soulstone's Power")
print(f"{characterName} reaches the ruins of the ancient temple where the Soulstone is said to be hidden. Inside, they encounter strange magical forces and remnants of ancient guardians who once protected the artifact.")
print("As the protagonist ventures deeper, they must decide how to approach the Soulstone.")
print("Do you attempt to take it for yourself, seek its destruction, or leave it untouched, fearing its power?")

while True:
    soulstoneChoice = input("What do you do with the Soulstone? (take, destroy, leave) ").lower()
    if soulstoneChoice == "take":
        print(f"{characterName} takes the Soulstone, feeling an immense surge of power. However, they begin to feel the darkness creeping into their soul.")
        soulstoneTaken = True
        break
    elif soulstoneChoice == "destroy":
        print(f"{characterName} destroys the Soulstone, knowing that such power should never fall into the wrong hands. The temple begins to collapse as a result.")
        soulstoneTaken = False
        break
    elif soulstoneChoice == "leave":
        print(f"{characterName} leaves the Soulstone, fearing its power. However, their journey becomes more difficult without it.")
        soulstoneTaken = False
        break
    else:
        print("Invalid choice. Please type 'take', 'destroy', or 'leave'.")

# New Quest: The Merchant's Offer
print("\nWhile passing through a nearby village, {characterName} encounters a merchant selling rare artifacts. He offers to sell you a powerful talisman that will aid in your journey, but it comes at a steep price.")
print("Do you accept the merchant's offer or refuse it?")

while True:
    merchantChoice = input("Do you accept the merchant's offer? (yes/no) ").lower()
    if merchantChoice == "yes":
        print(f"{characterName} agrees to purchase the talisman, using all their savings. The talisman grants them enhanced strength and defense.")
        health += 20  # Talisman heals the protagonist
        break
    elif merchantChoice == "no":
        print(f"{characterName} decides not to buy the talisman, choosing to rely on their own abilities.")
        break
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")

# Act III: The Final Confrontation
print("\nAct III: The Final Confrontation")
print(f"{characterName} arrives at the Black King's fortress, ready to face their greatest challenge yet. The Black King awaits in his throne room, empowered by the Soulstone. A fierce battle is imminent.")
print("As you approach, the Black King speaks: 'I knew you would come, {characterName}. But the time for hope is over. Only darkness remains.'")

# The Final Fight
print("\nThe Black King challenges you: 'Only one can survive this battle. To defeat me, you must match my mind and my will. Choose wisely, for your life hangs in the balance.'")
print("You must guess a number between 1 and 10. If you guess correctly, you will defeat the Black King. If you fail, you will fall in battle.")
print("You have two chances to get it right. Choose your number wisely!")

# Number guessing game (two attempts)
blackKingNumber = random.randint(1, 10)  # The Black King's secret number

attempts = 3
while attempts > 0:
    guess = int(input(f"Attempt {3 - attempts}: Choose a number between 1 and 10: "))
    
    if guess == blackKingNumber:
        print(f"Correct! You guessed the number {guess} and defeat the Black King!")
        print(f"{characterName} has saved the world from the Black King's tyranny.")
        print("With the Soulstone's power destroyed or contained, peace is restored to the realm.")
        break
    else:
        print(f"Incorrect. The number was {blackKingNumber}.")
        attempts -= 1

    if attempts == 0:
        print(f"{characterName} failed to guess the number. The Black King strikes with all his power, and you fall in battle.")
        print("Game Over. The world succumbs to darkness.")
        break

# Final message
if attempts > 0:
    print("\nThe world is saved, but the future remains uncertain. Thank you for playing *The Rise of the Black King*!")
