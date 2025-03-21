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