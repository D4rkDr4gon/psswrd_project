import tkinter as tk
from tkinter import messagebox
import string
import random
import os
import pickle

# Abecedario para generar contraseñas mediante random de caracteres
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Diccionario para almacenar información del sitio
site_info = {}

# Función para almacenar la URL del sitio
def store_url(site_name, url):
    site_info[site_name] = {'url': url}

# Función para almacenar la contraseña
def store_password(site_name, password):
    site_info[site_name]['password'] = password

# Función para almacenar el correo de registro
def store_email(site_name, email):
    site_info[site_name]['email'] = email

# Función para almacenar la fecha de registro
def store_registration_date(site_name, registration_date):
    site_info[site_name]['registration_date'] = registration_date

# Función para guardar la información en un archivo binario
def save_to_file():
    with open('site_info.bin', 'wb') as f:
        pickle.dump(site_info, f)

# Función para cargar la información desde un archivo binario
def load_from_file():
    if os.path.exists('site_info.bin'):
        with open('site_info.bin', 'rb') as f:
            return pickle.load(f)
    else:
        return {}

# Cargar la información del archivo al inicio
site_info = load_from_file()

# Función para imprimir todas las contraseñas almacenadas
def print_all_passwords():
    for site, info in site_info.items():
        print(f"Site: {site}, URL: {info.get('url', 'No URL stored')}, "
              f"Email: {info.get('email', 'No email stored')}, "
              f"Password: {info.get('password', 'No password stored')}, "
              f"Registration Date: {info.get('registration_date', 'No registration date stored')}")

# Función para eliminar la información de un sitio
def delete_site_info(site_name):
    if site_name in site_info:
        del site_info[site_name]
        print("Site information deleted successfully.")
        save_to_file()
    else:
        print("No information found for this site.")

# Funciones para las interfaces gráficas

# Función principal para almacenar una nueva contraseña
def gui_store_password():
    site_name = site_name_entry.get()
    url = url_entry.get()
    email = email_entry.get()
    registration_date = registration_date_entry.get()

    if not site_name or not url or not email:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    password = generate_password(12)
    store_url(site_name, url)
    store_email(site_name, email)
    store_password(site_name, password)
    store_registration_date(site_name, registration_date)
    save_to_file()

    password_info = f"URL: {url}\nEmail: {email}\nPassword: {password}\nRegistration Date: {registration_date}"
    messagebox.showinfo("Contraseña generada", password_info)

    site_name_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    registration_date_entry.delete(0, tk.END)

# Función para imprimir todas las contraseñas almacenadas en la interfaz gráfica
def gui_print_all_passwords():
    password_info = ""
    for site, info in site_info.items():
        password_info += f"Site: {site}, URL: {info.get('url', 'No URL stored')}, " \
                          f"Email: {info.get('email', 'No email stored')}, " \
                          f"Password: {info.get('password', 'No password stored')}, " \
                          f"Registration Date: {info.get('registration_date', 'No registration date stored')}\n"
    if password_info:
        messagebox.showinfo("Todas las contraseñas", password_info)
    else:
        messagebox.showinfo("No hay contraseñas", "No hay información de contraseñas almacenada.")

# Función para eliminar la información de un sitio en la interfaz gráfica
def gui_delete_site_info():
    site_name = site_name_entry.get()
    delete_site_info(site_name)
    site_name_entry.delete(0, tk.END)

# Función para la interfaz gráfica principal
def gui_interface():
    # Declarar las variables como globales
    global site_name_entry, url_entry, email_entry, registration_date_entry

    root = tk.Tk()
    root.title("Gestor de Contraseñas")

    # Etiquetas y campos de entrada
    site_name_label = tk.Label(root, text="Nombre del Sitio:")
    site_name_entry = tk.Entry(root)

    url_label = tk.Label(root, text="URL del Sitio:")
    url_entry = tk.Entry(root)

    email_label = tk.Label(root, text="Correo de Registro:")
    email_entry = tk.Entry(root)

    registration_date_label = tk.Label(root, text="Fecha de Registro:")
    registration_date_entry = tk.Entry(root)

    site_name_label.grid(row=0, column=0, padx=10, pady=10)
    site_name_entry.grid(row=0, column=1, padx=10, pady=10)

    url_label.grid(row=1, column=0, padx=10, pady=10)
    url_entry.grid(row=1, column=1, padx=10, pady=10)

    email_label.grid(row=2, column=0, padx=10, pady=10)
    email_entry.grid(row=2, column=1, padx=10, pady=10)

    registration_date_label.grid(row=3, column=0, padx=10, pady=10)
    registration_date_entry.grid(row=3, column=1, padx=10, pady=10)

    # Botones
    store_button = tk.Button(root, text="Guardar Contraseña", command=gui_store_password)
    store_button.grid(row=4, column=0, columnspan=2, pady=10)

    print_passwords_button = tk.Button(root, text="Imprimir Contraseñas", command=gui_print_all_passwords)
    print_passwords_button.grid(row=5, column=0, columnspan=2, pady=10)

    delete_site_button = tk.Button(root, text="Eliminar Información del Sitio", command=gui_delete_site_info)
    delete_site_button.grid(row=6, column=0, columnspan=2, pady=10)


# Llamar a la interfaz gráfica
gui_interface()
