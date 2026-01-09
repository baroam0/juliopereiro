import sqlite3
import datetime

# Ruta del archivo de texto
archivo_txt = 'proveedores.txt'

# Conexión a la base de datos SQLite (se crea si no existe)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Leer el archivo y procesar cada línea
with open(archivo_txt, 'r', encoding='latin-1') as f:
    for linea in f:
        partes = linea.strip().split(';')
        if len(partes) == 2:
            id_proveedor = int(partes[0])
            descripcion = partes[1].strip('"')
            domicilio = partes[3]
            localidad = partes[4]
            codpostal = partes[5]
            cuit = partes[6]
            telefono = partes[7]
            fax = partes[8]
            provincia = partes[9]
            pais = partes[10]
            observaciones = partes[11]
            email = partes[19]
            try:
                cursor.execute(
                    '''
                    INSERT INTO proveedores_proveedor (
                    codigoaccess,
                    descripcion,
                    domicilio,
                    localidad,
                    codpostal,
                    cuit,
                    telefono,
                    fax,
                    provincia,
                    pais,
                    observaciones,
                    email
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (
                        id_proveedor,
                        descripcion,
                        domicilio,
                        localidad,
                        codpostal,
                        cuit,
                        telefono,
                        fax,
                        provincia,
                        pais,
                        observaciones,
                        email
                    )
                )                
            except:
                pass

conn.commit()
conn.close()

print("Datos importados correctamente a la tabla 'proveedores'.")

