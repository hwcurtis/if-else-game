name = input("Hello challenger nice to meet you , what might your name be?")
print(f"Hello {name} , welcome to the  guessing game")

print("""you find yourself in the dark ,unsure how you got here , you hear a low growl and start to run, but
you trip over something, do you pick it up, avoid it, or place a trap""")

choice = input("pick up, avoid, place a trap?").lower()

if choice == "pick up":
    print("you pick up a shiny sword, you wait to see what made the noise ")
