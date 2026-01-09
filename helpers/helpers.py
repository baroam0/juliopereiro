

def es_numerico(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False