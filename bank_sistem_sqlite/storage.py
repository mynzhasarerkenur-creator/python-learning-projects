import sqlite3
from models import BankAccount

DB_PATH = "bank_sistem_sqlite/bank2.db"


def create_table():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY,
    owner TEXT,
    balance REAL
    )           
    """)
    connection.commit()
    connection.close()


def save_account(account: BankAccount):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        """
    INSERT INTO accounts (owner, balance)
    VALUES (?, ?)
    """,
        (account.owner, account.balance),
    )
    connection.commit()
    connection.close()


def get_account():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""SELECT owner, balance FROM accounts""")
    accounts = cursor.fetchall()
    connection.close()
    return accounts


def deposit_account(owner_input, amount):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT balance FROM accounts WHERE owner = ?""",
        (owner_input,),
    )

    result = cursor.fetchone()

    if result is None:
        connection.close()
        return False, None, None
    old_balance = result[0]
    new_balance = old_balance + amount
    cursor.execute(
        "UPDATE accounts SET balance = ? WHERE owner = ?", (new_balance, owner_input)
    )
    connection.commit()
    connection.close()
    return True, old_balance, new_balance


def withdraw_account(owner_input, amount):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT balance FROM accounts WHERE owner = ? ",
        (owner_input,),
    )
    result = cursor.fetchone()

    if result is None:
        connection.close()
        return "not_found", None, None

    old_balance = result[0]

    if old_balance < amount:
        connection.close()
        return "not_enough_money", old_balance, old_balance

    new_balance = old_balance - amount
    cursor.execute(
        "UPDATE accounts SET balance = ? WHERE owner = ?", (new_balance, owner_input)
    )
    connection.commit()
    connection.close()
    return "success", old_balance, new_balance
