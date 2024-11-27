import tkinter as tk
from tkinter import Scrollbar, Text
from PIL import Image, ImageTk   # "pip install pillow"   Instalar pillow para manejar el logo de imgs.

# Ruta del logo
logo_path = "imgs/golanglogo2.png"

# DEFINICION DE FUNCIONES A UTILIZAR DENTRO DEL "SHELL"

def capitalize_string(input_text):
    """Transforma el texto a mayúsculas."""
    return input_text.upper()

def run_function():
    input_text = input_text_widget.get("1.0", tk.END).strip()
    if input_text:
        result = capitalize_string(input_text)  # FUNCION DE PROCESAMIENTO DE TEXTO SIENDO UTILIZADA
        output_text_widget.config(state=tk.NORMAL)
        output_text_widget.insert(tk.END, result + "\n")
        output_text_widget.config(state=tk.DISABLED)

def reset_output():
    # Limpia el cuadro de texto de entrada
    input_text_widget.delete("1.0", tk.END)
    # Limpia el cuadro de texto de salida
    output_text_widget.config(state=tk.NORMAL)
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.config(state=tk.DISABLED)

# Crear ventana principal
root = tk.Tk()
root.title("Golang Language Analyzer")
root.geometry("800x600")  # Tamaño fijo
root.resizable(False, False)

# Crear el encabezado con el logo
header_frame = tk.Frame(root, bg="#87CEEB", height=100)
header_frame.pack(fill=tk.X)

logo_image = Image.open(logo_path)
logo_image = logo_image.resize((100, 100), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(header_frame, image=logo, bg="#87CEEB")
logo_label.pack(pady=10)

# Crear el área de texto para entrada y salida
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Cuadro de entrada de texto
input_text_widget = Text(main_frame, wrap=tk.WORD, height=20, width=40, bg="#D3D3D3")
input_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

# Cuadro de salida de texto con scrollbar
output_frame = tk.Frame(main_frame)
output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

output_text_widget = Text(output_frame, wrap=tk.WORD, height=20, width=40, bg="#000", fg="#FFF", state=tk.DISABLED)
output_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_scrollbar = Scrollbar(output_frame, command=output_text_widget.yview)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text_widget["yscrollcommand"] = output_scrollbar.set

# Botones de ejecución y reset
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, pady=10)

run_button = tk.Button(button_frame, text="Run", command=run_function, bg="#32CD32", fg="#FFF", width=10)
run_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_output, bg="#FF4500", fg="#FFF", width=10)
reset_button.pack(side=tk.RIGHT, padx=10)

# Iniciar bucle principal
root.mainloop()
