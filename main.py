from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Bobbie")
    print(f"Welcome to my new pet, {my_pet.name}!")

    # Demonstrate basic actions
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    
    # Train some tricks
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.train("jump")
    my_pet.train("sit")
    my_pet.train("fetch")
    my_pet.train("shake hands")
    my_pet.train("spin")
    my_pet.train("speak")
    my_pet.train("high five")
    my_pet.train("play bow")
    my_pet.train("dance with Almando")
    my_pet.train("eat")
    
    # Show all tricks
    my_pet.show_tricks()
    
    # Final status
    my_pet.get_status()

if __name__ == "__main__":
    main()
