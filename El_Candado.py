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
    "Nazario":  hash_password("1234"),
    "Joshua":    hash_password("xyz"),
    "Manuel": hash_password("5678"),
    "Alejandro":  hash_password("abcd"),
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


# ============================
# PARTE 2 — Funciones de login, agregar mensajes y mostrar tablero
# ============================

# ----- Autenticación básica -----
def login():
    print("=== LOGIN ===")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    if username not in USERS:
        print("Usuario inexistente.")
        return None

    hashed_input = hash_password(password)
    if USERS[username] != hashed_input:
        print("Contraseña incorrecta.")
        return None

    print(f"Bienvenido, {username}!")
    return username


# ----- Agregar mensaje al tablero -----
def add_message(current_user: str):
    print("\n=== NUEVO MENSAJE / TAREA ===")
    text = input("Escribe el mensaje: ")

    if not validate_message(text):
        return

    board.append({
        "autor": current_user,
        "mensaje": text.strip(),
        "fecha": datetime.datetime.now()
    })

    print("Mensaje agregado exitosamente.\n")


# ----- Mostrar mensajes -----
def show_board():
    print("\n=== TABLERO DE MENSAJES ===")
    if not board:
        print("No hay mensajes disponibles.\n")
        return

    for i, msg in enumerate(board, start=1):
        fecha = msg["fecha"].strftime("%Y-%m-%d %H:%M")
        print(f"{i}. [{fecha}] {msg['autor']}: {msg['mensaje']}")
    print()
    
# ============================
# PARTE 3 — Menú principal y ejecución del programa
# ============================

# ----- Menú general para usuario autenticado -----
def user_menu(current_user: str):
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1) Publicar mensaje")
        print("2) Ver tablero")
        print("3) Cerrar sesión")
        print("4) Salir")

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            add_message(current_user)
        elif option == "2":
            show_board()
        elif option == "3":
            print("Sesión cerrada.\n")
            break
        elif option == "4":
            print("Saliendo... ¡Hasta luego!")
            exit(0)
        else:
            print("Opción inválida.\n")


# ----- Función principal -----
def main():
    show_privacy_notice()

    while True:
        user = login()
        if user:
            user_menu(user)
        else:
            retry = input("¿Intentar de nuevo? (s/n): ").lower()
            if retry != "s":
                print("Aplicación finalizada.")
                break


# ----- Ejecutar todo -----
if __name__ == "__main__":
    main()

