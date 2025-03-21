import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, phone TEXT, email TEXT, city TEXT, address TEXT)""")

cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    initial_users = [
        ("Ana López", "123456789", "ana@example.com", "Madrid", "Calle Sol 12"),
        ("Juan Pérez", "987654321", "juan@example.com", "Barcelona", "Avenida Mar 45"),
        ("María Gómez", "555666777", "maria@example.com", "Valencia", "Plaza Luna 3"),
        ("Carlos Ruiz", "444333222", "carlos@example.com", "Sevilla", "Calle Río 78"),
        ("Laura Martínez", "111222333", "laura@example.com", "Bilbao", "Paseo Norte 9"),
        ("Pedro Sánchez", "999888777", "pedro@example.com", "Málaga", "Calle Playa 23")
    ]
    cursor.executemany("INSERT INTO users (name, phone, email, city, address) VALUES (?, ?, ?, ?, ?)", initial_users)
    conn.commit()

def create_user(name, phone, email, city, address):
    cursor.execute("INSERT INTO users (name, phone, email, city, address) VALUES (?, ?, ?, ?, ?)", 
                   (name, phone, email, city, address))
    conn.commit()
    print("Usuario creado exitosamente.")

def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Nombre: {user[1]}, Teléfono: {user[2]}, Email: {user[3]}, Ciudad: {user[4]}, Dirección: {user[5]}")

def update_phone(id, phone):
    cursor.execute("UPDATE users SET phone = ? WHERE id = ?", (phone, id))
    conn.commit()
    print("Teléfono actualizado exitosamente.")

def update_email(id, email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, id))
    conn.commit()
    print("Email actualizado exitosamente.")

def update_all(id, phone, email, city, address):
    cursor.execute("UPDATE users SET phone = ?, email = ?, city = ?, address = ? WHERE id = ?", 
                   (phone, email, city, address, id))
    conn.commit()
    print("Datos actualizados exitosamente.")

def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    print("Usuario eliminado exitosamente.")

def menu():
    while True:
        print("\n--- Menú CRUD ---")
        print("1. Crear usuario")
        print("2. Leer todos los usuarios")
        print("3. Actualizar teléfono")
        print("4. Actualizar email")
        print("5. Actualizar todos los datos")
        print("6. Eliminar usuario")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            email = input("Email: ")
            city = input("Ciudad: ")
            address = input("Dirección: ")
            create_user(name, phone, email, city, address)
        
        elif opcion == "2":
            print("\nLista de usuarios:")
            read_users()
        
        elif opcion == "3":
            id = int(input("ID del usuario: "))
            phone = input("Nuevo teléfono: ")
            update_phone(id, phone)
        
        elif opcion == "4":
            id = int(input("ID del usuario: "))
            email = input("Nuevo email: ")
            update_email(id, email)
        
        elif opcion == "5":
            id = int(input("ID del usuario: "))
            phone = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            city = input("Nueva ciudad: ")
            address = input("Nueva dirección: ")
            update_all(id, phone, email, city, address)
        
        elif opcion == "6":
            id = int(input("ID del usuario a eliminar: "))
            delete_user(id)
        
        elif opcion == "7":
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()

conn.close()   