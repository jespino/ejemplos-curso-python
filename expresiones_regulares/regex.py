import re

telefonos = ["+34 654654654", "0034 678678678"]
emails = ["usuario@gmail.com", "prueba@midominio.com"]

pattern = re.compile("^(\+|00)(\d{2})\ (\d{9})$")

for telefono in telefonos:
    matches = re.match(pattern, telefono)
    print "Codigo de pais: %s" % matches.group(2)
    print "Telefono: %s" % matches.group(3)

email_pattern = re.compile("^([^@]+)@([^@]+)$")
for email in emails:
    matches = re.match(email_pattern, email)
    print "Usuario: %s" % matches.group(1)
    print "Dominio: %s" % matches.group(2)
