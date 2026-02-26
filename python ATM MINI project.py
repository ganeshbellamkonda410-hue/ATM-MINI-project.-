balance = int(input("Enter your balance: "))

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Updated balance:", balance)

elif choice == 3:
    amount = int(input("Enter withdrawal amount: "))
    
    if amount <= balance:
        balance = balance - amount
        print("Updated balance:", balance)
    else:
        print("Insufficient balance")

else:
    print("Invalid choice")