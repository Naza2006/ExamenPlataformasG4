# ============================
# PARTE 1 — Autenticación, hashing, privacidad y validación de mensajes
# ============================

import hashlib
import datetime

# ----- Simulación de hash de contraseñas -----
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

# ----- Base de usuarios (editable para agregar más) -----
USERS = {
    "alice":  hash_password("1234"),
    "bob":    hash_password("1234"),
    "carlos": hash_password("5678"),
    "maria":  hash_password("abcd"),
}

# ----- Tablero global -----
board = []

# ----- Lista de palabras ofensivas -----
BAD_WORDS = ["tonto", "idiota", "estúpido", "imbécil"]


# ----- Aviso ético de privacidad -----
def show_privacy_notice():
    print("\n=== AVISO DE PRIVACIDAD ===")
    print("Los datos ingresados se usan solo con fines educativos.")
    print("No compartas información personal o sensible.")
    print("El uso debe ser responsable, respetuoso y ético.\n")


# ----- Filtro de contenido ofensivo -----
def contains_offensive_content(text: str) -> bool:
    text_lower = text.lower()
    return any(bad in text_lower for bad in BAD_WORDS)


# ----- Validación de tarea o mensaje -----
def validate_message(text: str) -> bool:
    if not text.strip():
        print("⚠ El mensaje no puede estar vacío.")
        return False
    if len(text) > 200:
        print("⚠ El mensaje es demasiado largo (máximo 200 caracteres).")
        return False
    if contains_offensive_content(text):
        print("⚠ El mensaje contiene palabras ofensivas.")
        return False
    return True
