#gestor de contraseñas por terminal 

#abecedario para generar contraseñas mediante random de caracteres
import string
import random
#libreria para encriptar contraseñas
import hashlib
#libreria para guardar contraseñas en fichero
import pickle
#libreria para encriptar fichero
from cryptography.fernet import Fernet
#libreria para leer fichero
from pathlib import Path
#libreria para borrar fichero
import os
#libreria para crear fichero
import pathlib
#libreria para crear carpetas
import shutil
import sys
import time
import getpass
import re
import pyperclip
import pyfiglet
import termcolor
from termcolor import colored
from colorama import Fore, Style
from colorama import init

#funcion para generar contraseñas
def generate_password(length):
    # Combine all the character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password of specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Dictionary to store site information
site_info = {}

# Function to store site URL
def store_url(site_name, url):
    if site_name not in site_info:
        site_info[site_name] = {}
    site_info[site_name]['url'] = url

# Function to store password
def store_password(site_name, password):
    if site_name not in site_info:
        site_info[site_name] = {}
    site_info[site_name]['password'] = password

# Function to store registration email
def store_email(site_name, email):
    if site_name not in site_info:
        site_info[site_name] = {}
    site_info[site_name]['email'] = email

def save_to_file():
    with open('site_info.bin', 'wb') as f:
        pickle.dump(site_info, f)

def load_from_file():
    if os.path.exists('site_info.bin'):
        with open('site_info.bin', 'rb') as f:
            return pickle.load(f)
    else:
        return {}

site_info = load_from_file()

def print_all_passwords():
    for site, info in site_info.items():
        print(f"Site: {site}, URL: {info.get('url', 'No URL stored')}, Email: {info.get('email', 'No email stored')}, Password: {info.get('password', 'No password stored')}")

def interface():
    while True:
        print("\nPassword Manager")
        print("1. Store new site information")
        print("2. Retrieve a password")
        print("3. Print all stored passwords")
        print("4. Delete site information")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            site_name = input("Enter site name: ")
            url = input("Enter site URL: ")
            email = input("Enter registration email: ")
            password = generate_password(12)
            print("Generated password: ", password)
            store_url(site_name, url)
            store_email(site_name, email)
            store_password(site_name, password)
            print("Site information stored successfully.")
            save_to_file()
        elif choice == '2':
            site_name = input("Enter site name: ")
            if site_name in site_info:
                print("URL: ", site_info[site_name].get('url', 'No URL stored'))
                print("Email: ", site_info[site_name].get('email', 'No email stored'))
                print("Password: ", site_info[site_name].get('password', 'No password stored'))
            else:
                print("No information found for this site.")
        elif choice == '3':
            print_all_passwords()
        elif choice == '4':
            site_name = input("Enter site name: ")
            if site_name in site_info:
                del site_info[site_name]
                print("Site information deleted successfully.")
                save_to_file()
            else:
                print("No information found for this site.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the interface
interface()