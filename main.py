import tkinter as tk

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Bank")

        self.accounts = {}

        # Create GUI elements
        self.label_name = tk.Label(root, text="Account Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_balance = tk.Label(root, text="Initial Balance:")
        self.label_balance.grid(row=1, column=0, padx=5, pady=5)
        self.entry_balance = tk.Entry(root)
        self.entry_balance.grid(row=1, column=1, padx=5, pady=5)

        self.button_create = tk.Button(root, text="Create Account", command=self.create_account)
        self.button_create.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.label_action = tk.Label(root, text="Action:")
        self.label_action.grid(row=3, column=0, padx=5, pady=5)
        self.action_var = tk.StringVar(root)
        self.action_var.set("Deposit")
        self.action_menu = tk.OptionMenu(root, self.action_var, "Deposit", "Withdraw", "Check Balance")
        self.action_menu.grid(row=3, column=1, padx=5, pady=5)

        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.grid(row=4, column=0, padx=5, pady=5)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row=4, column=1, padx=5, pady=5)

        self.button_submit = tk.Button(root, text="Submit", command=self.perform_action)
        self.button_submit.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def create_account(self):
        name = self.entry_name.get()
        balance = float(self.entry_balance.get())
        if name in self.accounts:
            self.output_text.insert(tk.END, "Account already exists.\n")
            return
        if balance < 0:
            self.output_text.insert(tk.END, "Initial balance must be non-negative.\n")
            return
        self.accounts[name] = balance
        self.output_text.insert(tk.END, f"Account created for {name} with initial balance ${balance:.2f}\n")

    def perform_action(self):
        name = self.entry_name.get()
        action = self.action_var.get()
        amount = float(self.entry_amount.get())

        if action == "Deposit":
            if name not in self.accounts:
                self.output_text.insert(tk.END, "Account does not exist.\n")
                return
            if amount <= 0:
                self.output_text.insert(tk.END, "Deposit amount must be positive.\n")
                return
            self.accounts[name] += amount
            self.output_text.insert(tk.END, f"${amount:.2f} deposited into {name} account. New balance: ${self.accounts[name]:.2f}\n")

        elif action == "Withdraw":
            if name not in self.accounts:
                self.output_text.insert(tk.END, "Account does not exist.\n")
                return
            if amount <= 0:
                self.output_text.insert(tk.END, "Withdrawal amount must be positive.\n")
                return
            if self.accounts[name] < amount:
                self.output_text.insert(tk.END, "Insufficient funds.\n")
                return
            self.accounts[name] -= amount
            self.output_text.insert(tk.END, f"${amount:.2f} withdrawn from {name} account. New balance: ${self.accounts[name]:.2f}\n")

        elif action == "Check Balance":
            if name not in self.accounts:
                self.output_text.insert(tk.END, "Account does not exist.\n")
                return
            self.output_text.insert(tk.END, f"Balance for {name} account: ${self.accounts[name]:.2f}\n")


def main():
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
