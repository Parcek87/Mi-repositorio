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
