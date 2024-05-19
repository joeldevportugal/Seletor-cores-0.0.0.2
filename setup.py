from cx_Freeze import setup, Executable
import sys

# Inclua bibliotecas adicionais aqui, se necessário
includes = ['tkinter', 'customtkinter', 'pyperclip']

# Exclua bibliotecas que não são necessárias aqui, se necessário
excludes = []

# Defina o caminho das bibliotecas adicionais, se necessário
packages = []

# Defina o caminho dos arquivos adicionais que devem ser incluídos no executável
include_files = []

# Base do executável. No Windows, use "Win32GUI" para uma aplicação GUI
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        "Selector.py",  # Substitua pelo nome do seu arquivo Python
        base=base,
        target_name="Selector0.0.2.exe"  # Nome do executável gerado
    )
]

setup(
    name="Selector Cores",
    version="1.0.0.1",
    description="Selector Para Defenir cores Hexadecila",
    options={
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "packages": packages,
            "include_files": include_files,
        }
    },
    executables=executables
)
