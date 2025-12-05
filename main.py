import os
import shutil
import psutil
import tkinter as tk
from tkinter import ttk, messagebox

def obtener_dispositivos():
    dispositivos = []
    for disk in psutil.disk_partitions():
        if "removable" in disk.opts:
            dispositivos.append(disk.device)
    return dispositivos

def mover_archivos():
    origen = origen_var.get()
    destino = destino_var.get()
    
    if origen and destino:
        mover_archivos_func(origen, destino)
    else:
        messagebox.showerror("Error", "Por favor, selecciona ambos directorios.")

def mover_archivos_func(directorio_origen, directorio_destino):
    # Verificar si los directorios existen
    if not os.path.exists(directorio_origen) or not os.path.exists(directorio_destino):
        messagebox.showerror("Error", "Uno o ambos directorios no existen.")
        return
    
    # Mover cada archivo al directorio de destino
    for archivo in os.listdir(directorio_origen):
        origen_archivo = os.path.join(directorio_origen, archivo)
        destino_archivo = os.path.join(directorio_destino, archivo)
        
        # Verificar si el archivo ya existe en el destino
        if not os.path.exists(destino_archivo):
            try:
                shutil.move(origen_archivo, destino_archivo)
                print(f"Archivo {archivo} movido exitosamente a {destino_archivo}")
            except Exception as e:
                print(f"Error al mover el archivo {archivo}: {e}")
        else:
            print(f"El archivo {archivo} ya existe en el destino.")

def mover_carpeta():
    origen = origen_var.get()
    destino = destino_var.get()
    
    if origen and destino:
        mover_carpeta_func(origen, destino)
    else:
        messagebox.showerror("Error", "Por favor, selecciona ambos directorios.")

def mover_carpeta_func(directorio_origen, directorio_destino):
    if not os.path.exists(directorio_origen) or not os.path.exists(directorio_destino):
        messagebox.showerror("Error", "Uno o ambos directorios no existen.")
        return
    
    # Mover la carpeta entera
    try:
        shutil.move(directorio_origen, directorio_destino)
        print(f"Carpeta {directorio_origen} movida exitosamente a {directorio_destino}")
    except Exception as e:
        print(f"Error al mover la carpeta {directorio_origen}: {e}")

def abrir_interfaz():
    root = tk.Tk()
    root.title("Mover Archivos")

    # Obtener la lista de dispositivos USB
    dispositivos = obtener_dispositivos()
    
    # Crear variables para los directorios
    global origen_var, destino_var
    origen_var = tk.StringVar()
    destino_var = tk.StringVar()

    # Crear la interfaz
    ttk.Label(root, text="Selecciona el directorio de origen:").pack(pady=5)
    origen_entry = ttk.Entry(root, textvariable=origen_var, width=50)
    origen_entry.pack(pady=5)
    
    ttk.Label(root, text="Selecciona el directorio de destino:").pack(pady=5)
    destino_entry = ttk.Entry(root, textvariable=destino_var, width=50)
    destino_entry.pack(pady=5)

    # Crear un combobox para mostrar los dispositivos USB
    dispositivo_combobox = ttk.Combobox(root, textvariable=tk.StringVar(), values=dispositivos, state="readonly")
    dispositivo_combobox.pack(pady=5)
    
    # Botón para mover los archivos
    mover_archivo_button = ttk.Button(root, text="Mover Archivos", command=mover_archivos)
    mover_archivo_button.pack(pady=10)
    
    # Botón para mover la carpeta
    mover_carpeta_button = ttk.Button(root, text="Mover Carpeta", command=mover_carpeta)
    mover_carpeta_button.pack(pady=10)

    root.mainloop()

# Ejecutar la interfaz
abrir_interfaz()