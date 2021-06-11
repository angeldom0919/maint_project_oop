#!/usr/bin/env python3
import sys
import pymysql
from maint_oop_module import *


def display_menu():
    print("The Product Table Maintenance ")
    print()
    print("COMMAND MENU")
    print("product - show a product info")
    print("show   - Show all products info")
    print("add    - insert a Product")
    print("update - update a Product")
    print("del    - Delete a product")
    print("exit   - Exit program")


def main():
    p1 = product()
    conn_list = p1.mysql_connect()
    conn = conn_list[0]
    stmt = conn_list[1]

    display_menu()

    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            p1.show_products(conn, stmt)
        elif command == "product":
            p1.show_product(conn, stmt)
        elif command == "add":
            p1.insert_products(conn, stmt)
        elif command == "update":
            p1.update_products(conn, stmt)
        elif command == "del":
            p1.delete_products(conn, stmt)
        elif command == "exit":
            p1.mysql_disconnect(conn, stmt)
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
