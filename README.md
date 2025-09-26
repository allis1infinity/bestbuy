# 💻 Simple Python Store App

This is a basic **console application** built with Python. It simulates a small store where you can check inventory and process customer orders. It's a great example of using Object-Oriented Programming (OOP) in a practical way!

---

## ✨ Features (What it can do)

* **View Stock:** See a list of all products currently available.
* **Check Totals:** Quickly check the total number of items in the store.
* **Place Orders:** Buy items, and the app will check if there's enough stock and calculate the total cost.
* **Safety Checks:** Includes basic checks to prevent users from ordering negative amounts or items that are out of stock.

---

## 🚀 How to Run the App

1.  **Get the code:** Download all files (`main.py`, `products.py`, `store.py`) from this repository.
2.  **Open your terminal** (Command Prompt/PowerShell/Terminal) and go to the folder where you saved the files.
3.  **Start the program:**
    ```bash
    python main.py
    ```

---

## 📂 Code Structure (How it works)

* `products.py`: Defines the **Product** object (name, price, quantity).
* `store.py`: Defines the **Store** object, which manages the entire inventory and handles the main `order` logic.
* `main.py`: Contains the **interactive menu** and runs the program.