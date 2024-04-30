import mysql.connector
import tkinter as tk

conn = mysql.connector.connect(
    host="localhost",
    database="banking",
    user="root",
    password="eyerusekifle0317")

class BankAccount:
    def __init__(self, name, acc_num, password, balance=0):
        self.name = name
        self.acc_num = acc_num
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.update_balance()
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.update_balance()
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Balance for {self.name}: ${self.balance}")

    def update_balance(self):
        cursor = conn.cursor()
        sql = "UPDATE accounts SET balance = %s WHERE acc_num = %s"
        val = (self.balance, self.acc_num)
        cursor.execute(sql, val)
        conn.commit()

def create_account(name, acc_num, password, balance):
    cursor = conn.cursor()
    sql = "INSERT INTO accounts (name, acc_num, password, balance) VALUES (%s, %s, %s, %s)"
    val = (name, acc_num, password, balance)
    cursor.execute(sql, val)
    conn.commit()
    print("Account created successfully!")

def main_window():
    root = tk.Tk()
    root.title("WorldBank")
    
    label = tk.Label(root, text="Welcome to WorldBank!")
    label.pack()

    name_label = tk.Label(root, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    acc_num_label = tk.Label(root, text="Account Number:")
    acc_num_label.pack()
    acc_num_entry = tk.Entry(root)
    acc_num_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    balance_label = tk.Label(root, text="Initial Balance:")
    balance_label.pack()
    balance_entry = tk.Entry(root)
    balance_entry.pack()

    create_button = tk.Button(root, text="Create Account", command=lambda: create_account(name_entry.get(), acc_num_entry.get(), password_entry.get(), balance_entry.get()))
    create_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main_window()
