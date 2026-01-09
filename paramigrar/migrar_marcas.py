import sqlite3
import datetime

# Ruta del archivo de texto
archivo_txt = 'Marcas.txt'

# Conexión a la base de datos SQLite (se crea si no existe)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


# Leer el archivo y procesar cada línea
with open(archivo_txt, 'r', encoding='utf-8') as f:
    for linea in f:
        partes = linea.strip().split(';')
        if len(partes) == 2:
            id_marca = int(partes[0])
            nombre_marca = partes[1].strip('"')
            fecha = datetime.date.today()
            try:
                cursor.execute('INSERT INTO marcas_marca (codigoaccess, descripcion,fecha) VALUES (?, ?, ?)', (id_marca, nombre_marca, fecha))
            except:
                pass

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Datos importados correctamente a la tabla 'marcas'.")
