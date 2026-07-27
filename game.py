print("=" * 40)
print("🏰 TERMINAL ADVENTURE")
print("=" * 40)

name = input("What is your name? ")

print()
print(f"Welcome, {name}!")
print("You wake up inside a dark cave.")
print("There are two tunnels.")

print()
print("1. Left Tunnel")
print("2. Right Tunnel")

choice = input("Choose (1 or 2): ")

print()

if choice == "1":
    print("💰 You found treasure!")

elif choice == "2":
    print("🐉 The dragon becomes your best friend!")
    print("🍕 It gives you free pizza.")

else:
    print("❌ That wasn't a valid choice.")
    print("Version 2 🚀")