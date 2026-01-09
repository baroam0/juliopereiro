
import datetime

from marcas.models import Marca
from proveedores.models import Proveedor
from articulos.models import Articulo

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def limpiar_numero_str(s):
    if s is None:
        return None
    s = s.strip()
    if s == '':
        return None
    # Si hay separadores de miles estilo "1,234.56" o "1.234,56"
    # Detecta el patrón más probable; adapta si tu CSV es consistente.
    if s.count(',') == 1 and s.count('.') > 0 and s.find('.') < s.find(','):
        # ejemplo "1.234,56" -> "1234.56"
        s = s.replace('.', '').replace(',', '.')
    else:
        # convierte comas a punto (ej "1234,56" -> "1234.56")
        s = s.replace(',', '.')
    return s

def str_a_decimal(s, decimal_places=2, default=None):
    s_clean = limpiar_numero_str(s)
    if s_clean is None:
        return default
    try:
        d = Decimal(s_clean)
    except InvalidOperation:
        return default
    # asegurar número de decimales como en el DecimalField
    quant = Decimal('1').scaleb(-decimal_places)  # ejemplo Decimal('0.01')
    return d.quantize(quant, rounding=ROUND_HALF_UP)

archivo_txt = 'articulos.txt'

c = 0

with open(archivo_txt, 'r', encoding='utf-8') as f:
    for linea in f:
        partes = linea.strip().split(';')
        if len(partes) >= 29:
            codigoaccess = partes[0]
            descripcion = partes[1]
            #iva = str(partes[3])
            #iva = iva.replace(',','.')
            #iva = float(iva)
            iva = str_a_decimal(partes[3], decimal_places=2, default=Decimal('0.00'))
            marcaid = partes[4]
            #pventa1 = partes[6]
            pventa1 = str_a_decimal(partes[6], decimal_places=2, default=Decimal('0.00'))
            codigobarra = ""
            #fechaprecio = formatear_fecha(partes[25]) 
            fechaprecio = partes[25]
            codigoproducto = partes[26]
            proveedor = partes[27]

            try:
                marca = Marca.objects.get(codigoaccess=int(marcaid))
                proveedor = Proveedor.objects.get(codigoaccess=int(proveedor))

                articulo = Articulo(
                    codigoaccess=codigoaccess,
                    descripcion=descripcion,
                    iva=iva,
                    marca=marca,
                    proveedor=proveedor
                )
                articulo.iva=iva
                articulo.save()

                t=(codigoaccess,descripcion,iva,marca,proveedor)
                print(t)

                c = c +1
            except Exception as e:
                print(str(e))
                print("Errores....")
                print(str(codigoaccess))
                print("---")
                print(descripcion)
                print("---")
                print(iva)
                print("---")
                print(marca)
                print("---")
                print(proveedor)
                
                
                
                
                
                
print(c)
