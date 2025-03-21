import sqlite3

# Conexión e inicialización de la base de datos
def inicializar_base_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL,
            ciudad TEXT NOT NULL,
            direccion TEXT NOT NULL
        )
    """)
    # Insertar usuarios iniciales
    usuarios_iniciales = [
        ("Juan Pérez", "3001234567", "juan@example.com", "Bogotá", "Cra 1 #12-34"),
        ("Ana Gómez", "3117654321", "ana@example.com", "Medellín", "Calle 45 #67-89"),
        ("Carlos Ruiz", "3229876543", "carlos@example.com", "Cali", "Av 10 #20-30"),
        ("Laura Méndez", "3134567890", "laura@example.com", "Barranquilla", "Calle 50 #60-70"),
        ("Pedro García", "3201239876", "pedro@example.com", "Cartagena", "Cra 9 #15-16"),
        ("María Torres", "3016785432", "maria@example.com", "Bucaramanga", "Calle 100 #25-35")
    ]
    cursor.executemany("""
        INSERT INTO usuarios (nombre, telefono, email, ciudad, direccion)
        VALUES (?, ?, ?, ?, ?)
    """, usuarios_iniciales)
    conexion.commit()
    conexion.close()

# Crear (Create)
def agregar_usuario(nombre, telefono, email, ciudad, direccion):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nombre, telefono, email, ciudad, direccion)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, telefono, email, ciudad, direccion))
    conexion.commit()
    conexion.close()

# Leer (Read)
def obtener_usuarios():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

# Actualizar (Update) - Opciones específicas
def actualizar_telefono(id_usuario, nuevo_telefono):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET telefono = ? WHERE id = ?", (nuevo_telefono, id_usuario))
    conexion.commit()
    conexion.close()

def actualizar_email(id_usuario, nuevo_email):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (nuevo_email, id_usuario))
    conexion.commit()
    conexion.close()

def actualizar_datos(id_usuario, telefono, email, ciudad, direccion):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE usuarios SET telefono = ?, email = ?, ciudad = ?, direccion = ?
        WHERE id = ?
    """, (telefono, email, ciudad, direccion, id_usuario))
    conexion.commit()
    conexion.close()

# Eliminar (Delete)
def eliminar_usuario(id_usuario):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexion.commit()
    conexion.close()

# Menú interactivo
def menu_interactivo():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Actualizar teléfono")
        print("4. Actualizar email")
        print("5. Actualizar todos los datos (excepto ID y nombre)")
        print("6. Eliminar usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            ciudad = input("Ciudad: ")
            direccion = input("Dirección: ")
            agregar_usuario(nombre, telefono, email, ciudad, direccion)
        elif opcion == "2":
            usuarios = obtener_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif opcion == "3":
            id_usuario = int(input("ID del usuario: "))
            nuevo_telefono = input("Nuevo teléfono: ")
            actualizar_telefono(id_usuario, nuevo_telefono)
        elif opcion == "4":
            id_usuario = int(input("ID del usuario: "))
            nuevo_email = input("Nuevo email: ")
            actualizar_email(id_usuario, nuevo_email)
        elif opcion == "5":
            id_usuario = int(input("ID del usuario: "))
            telefono = input("Teléfono: ")
            email = input("Email: ")
            ciudad = input("Ciudad: ")
            direccion = input("Dirección: ")
            actualizar_datos(id_usuario, telefono, email, ciudad, direccion)
        elif opcion == "6":
            id_usuario = int(input("ID del usuario: "))
            eliminar_usuario(id_usuario)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Inicializar la base de datos y ejecutar el programa
if __name__ == "__main__":
    inicializar_base_datos()
    menu_interactivo()
