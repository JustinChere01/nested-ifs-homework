place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action. Please choose 'climb a tree' or 'cross a river'.")

elif place == "cave":
    print("You find a hidden treasure!")

else:
    print("Invalid place. Please choose 'forest' or 'cave'.")

if place == "cave":
    choice = input("You find a cave. Do you want to light a torch or proceed in the dark? ")

    if choice == "light a torch":
        print("You light a torch and explore deeper into the cave.")
        # Add more outcomes or scenes here.
    elif choice == "proceed in the dark":
        print("You cautiously move forward in the darkness.")
        # Add more outcomes or scenes here.
    else:
        print("Invalid choice. Please select 'light a torch' or 'proceed in the dark'.")


attendees = int(input("Enter number of attendees: "))  # Convert input to an integer
venue = "large hall" if attendees > 100 else "conference room"  # Use shorthand if-else
print(venue)
