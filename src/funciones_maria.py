def convertirdecimal(x): #hacemos este paso para poder trabajar con los porcentajes en floats
    a = x.replace(',','.')
    return float(a[:-1])