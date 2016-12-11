from jinja2 import Template
template = Template(open("plantilla_simple.jinja").read())
html = template.render({
    "title": "Mi titulo",
    "posts": [{
        "title": "Ejemplo de titulo 1",
        "body": "Ejemplo de cuerpo 1"
    }, {
        "title": "Ejemplo de titulo 2",
        "body": "Ejemplo de cuerpo 2"
    }, {
        "title": "Ejemplo de titulo 3",
        "body": "Ejemplo de cuerpo 3"
    }]
})
print html
