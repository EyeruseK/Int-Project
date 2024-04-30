import mysql.connector
import tkinter as tk
root = tk.Tk()

conn = mysql.connector.connect(
    host="localhost",
    database="banking",
    user="root",
    password="eyerusekifle0317" )

class BankAccount:
    def __init__(self, name, acc_num, password, balance=0):
        self.name = name
        self.acc_num = acc_num
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Balance for {self.name}: ${self.balance}")

def create_account():
    print("Welcome to WORLDBANK!")
    name = input("Name: ")
    acc_num = input("Account Number: ")
    password = input("Password: ")
    balance = input('Initial Balance: ')
    cursor = conn.cursor()
    sql = "INSERT INTO accounts (name, acc_num, password, balance) VALUES (%s, %s, %s, %s)"
    val = (name, acc_num, password, balance)
    cursor.execute(sql, val)
    conn.commit()
    print("Account created successfully!")


def main():
    label = tk.Label(root, text="Welcome to WorldBank!")
    label.pack()
    name = input("Name: ")
    acc_num = input("Account Number: ")
    password = input("Password: ")
    account = BankAccount(name, acc_num, password)
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
          create_account()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            account.get_balance()
        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")



if __name__ == "__main__":
    main()