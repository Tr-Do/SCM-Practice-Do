import sqlite3
import os

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'" 
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def execute_command(user_input):
    os.system(f"echo {user_input}") 

if __name__ == "__main__":
    user_input = input("Enter username: ")
    print(get_user_data(user_input))

    filename = input("Enter filename to read: ")
    print(read_file(filename))

    command = input("Enter a command: ")
    execute_command(command)