import signal

import mysql.connector
from prettytable import PrettyTable
import sys

configs = [
    {'host': 'Host', 'username': 'user', 'password': 'pass', 'database': 'db'}
]

connections = []

def close_connections():
    for connection in connections:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


def signal_handler(sig, frame):
    print("\nReceived Ctrl+C. Exiting gracefully.")
    close_connections()
    sys.exit(0)


# Register the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)


def printoutput(cursor):
    if user_input.lower().startswith('select') or user_input.lower().startswith('show'):
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        table = PrettyTable(columns)
        table.add_rows(results)
        print(table)


try:
    for config in configs:
        try:
            print(f"\nConnecting to MySQL host: {config}")
            connection = mysql.connector.connect(
                host=config['host'],
                user=config['username'],
                password=config['password'],
                database=config['database']
            )
            print(f"Connected to MySQL database: {config['database']} on host: {config['host']}")
            connections.append(connection)
        except Exception as e:
            print(f"Error: {e}")
    while True:
        commands_input = input("Enter MySQL commands (separate commands with semicolon, or 'exit' to quit):\n")
        if commands_input.lower() == 'exit':
            break
        for connection in connections:
            print(f"\nChecking connection on MySQL host: {connection.server_host}")
            try:
                if connection.is_connected():
                    print(f"Running on MySQL database: {connection.database} on host: {connection.server_host}")
                    cursor = connection.cursor()
                    commands = [cmd.strip() for cmd in commands_input.split(';') if cmd.strip()]
                    try:
                        for user_input in commands:
                            cursor.execute(user_input)
                            printoutput(cursor)
                        connection.commit()

                    except mysql.connector.Error as e:
                        print(f"Error: {e}")
            except mysql.connector.Error as e:
                print(f"Error: {e}")
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    close_connections()
