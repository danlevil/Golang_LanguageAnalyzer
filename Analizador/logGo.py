#Ronald Gaibor

import logging
import subprocess
from datetime import datetime

# Usuario de Git
def get_git_username():
    try:
        username = subprocess.check_output(
            ['git', 'config', '--get', 'user.name'], universal_newlines=True
        ).strip()
        return username
    except subprocess.CalledProcessError:
        return 'unknown_user'  # Nombre de usuario no encontrado

# Fecha y Hora
def get_current_datetime():
    return datetime.now().strftime("%d%m%Y-%Hh%M-")

# Nombre de archivo
git_username = get_git_username()
current_datetime = get_current_datetime()
log_filename = f"lexico-{git_username}-{current_datetime}.txt"

# Configuración para logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"../logs/{log_filename}"),  # Salida a directorio logs
        logging.StreamHandler()                    # Salida por consola
    ]
)

# Ejemplos
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
