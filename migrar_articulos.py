
import sqlite3
import datetime

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def limpiar_numero_str(s):
    if s is None:
        return None
    s = s.strip()
    if s == '':
        return None
    # Maneja formatos tipo "1.234,56" y "1234,56"
    if s.count(',') == 1 and s.count('.') > 0:
        s = s.replace('.', '').replace(',', '.')
    else:
        s = s.replace(',', '.')
    return s


def str_a_decimal(s, decimal_places=2, default=None):
    s_clean = limpiar_numero_str(s)
    if s_clean is None:
        return default
    try:
        d = Decimal(s_clean)
        quant = Decimal('1').scaleb(-decimal_places)  # e.g. Decimal('0.01') para 2 decimales
        return d.quantize(quant, rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError):
        return default



def formatear_fecha(fecha_ddmmyyyy):
    """
    Recibe una fecha en formato dd/mm/aaaa y la devuelve en formato aaaa/mm/dd.

    Args:
        fecha_ddmmyyyy (str): La fecha en formato "dd/mm/aaaa" (por ejemplo, "16/09/2025").

    Returns:
        str: La fecha formateada en formato "aaaa/mm/dd" (por ejemplo, "2025/09/16").
             Devuelve None si el formato de entrada es incorrecto.
    """
    try:
        dia, mes, anio = fecha_ddmmyyyy.split('/')
        return f"{anio}-{mes}-{dia}"
    except ValueError:
        print("Error: Formato de fecha incorrecto.  Debe ser dd/mm/aaaa.")
        return None


archivo_txt = 'articulos.txt'

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

with open(archivo_txt, 'r', encoding='utf-8') as f:
    for linea in f:
        partes = linea.strip().split(';')
        if len(partes) >= 29:
            codigoaccess = partes[0]
            descripcion = partes[1]
            iva = partes[3]
            iva_decimal = str_a_decimal(iva, decimal_places=2, default=Decimal('0.00'))
            marca = partes[4]            
            pventa1 = partes[6]
            codigobarra = ""
            fechaprecio = formatear_fecha(partes[25]) 
            codigoproducto = partes[26]
            proveedor = partes[27]

            print(partes)

            try:
                print("Insertando....")
                cursor.execute(
                    '''
                    INSERT INTO articulos_articulo (
                    codigoaccess,
	                descripcion,
                    iva
                    ) VALUES (?,?,?)
                    ''',
                    (
                        codigoaccess,
                        descripcion,
                        iva_decimal
                    )
                )
                print("Insertado")                
            except Exception as e:
                print(str(e))

conn.commit()
conn.close()

