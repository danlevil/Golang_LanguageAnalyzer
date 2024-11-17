# Ronald Gaibor

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
    return datetime.now().strftime("%d%m%Y-%Hh%M")

# Nombre del archivo
def set_file_name(module):
    git_username = get_git_username()
    current_datetime = get_current_datetime()
    log_filename = f"{module}-{git_username}-{current_datetime}.txt"
    return log_filename

# Logger para cada módulo
def setup_module_logger(module):
    log_filename = set_file_name(module)
    formatter = logging.Formatter('%(levelname)s - %(message)s')

    file_handler = logging.FileHandler(f"../logs/{module}/{log_filename}")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()

    logger = logging.getLogger(module)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.propagate = False

# Creación de loggers para cada módulo
# setup_module_logger("__lexico__")
# setup_module_logger("__main__")

# Funciones de logging
def log_warning(module, message):
    logger = logging.getLogger(module)
    logger.warning(message)

def log_info(module, message):
    logger = logging.getLogger(module)
    logger.info(message)

# Configuración para logs
'''logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"../logs/{log_filename}"),  # Salida a directorio logs
        logging.StreamHandler()                    # Salida por consola
    ]   
)
'''
# Ejemplos
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
