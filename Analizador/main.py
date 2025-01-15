import tkinter as tk
from tkinter import Scrollbar, Text
from PIL import Image, ImageTk   # "pip install pillow"   Instalar pillow para manejar el logo de imgs.
import lexico as lexical
import syntaxAnalyzer as syntax
import ply.yacc as yacc
import logGo as log

# Ruta del logo
logo_path = "imgs/golanglogo2.png"

# DEFINICION DE FUNCIONES A UTILIZAR DENTRO DEL "SHELL"

def run_function():
    """Ejecuta el análisis léxico y sintáctico."""
    input_text = input_text_widget.get("1.0", tk.END).strip()
    if not input_text:
        return
    
    # Limpiar el output antes de ejecutar
    output_text_widget.config(state=tk.NORMAL)
    output_text_widget.delete("1.0", tk.END)

    # Análisis léxico
    try:
        lexical.lexer.input(input_text)
        output_text_widget.insert(tk.END, "== Resultado del análisis léxico ==\n")
        for tok in lexical.lexer:
            output_text_widget.insert(tk.END, f"{tok}\n")
    except Exception as e:
        output_text_widget.insert(tk.END, f"Error en el análisis léxico: {str(e)}\n")
        output_text_widget.config(state=tk.DISABLED)
        return
    
    # Análisis sintáctico
    try:
        syntax.parser.parse(input_text)
        output_text_widget.insert(tk.END, "\n== Resultado del análisis sintáctico ==\n")
        output_text_widget.insert(tk.END, "Análisis sintáctico completado sin errores.\n")
    except Exception as e:
        output_text_widget.insert(tk.END, f"Error en el análisis sintáctico: {str(e)}\n")
    
    output_text_widget.config(state=tk.DISABLED)

def reset_output():
    """Limpia el cuadro de entrada y salida."""
    input_text_widget.delete("1.0", tk.END)
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
