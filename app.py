from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    noticias = [
        {'titulo': 'Partido Destacado', 'contenido': 'Resumen del último partido del equipo y resultados.'},
        # Agrega más noticias según sea necesario
    ]

    eventos = [
        {'nombre': 'Próximo partido', 'fecha': 'Fecha', 'hora': 'Hora'},
        # Agrega más eventos según sea necesario
    ]

    contacto = {
        'direccion': 'Dirección del Club de Fútbol',
        'telefono': 'xxx-xxx-xxxx',
        'email': 'info@clubdefutbol.com',
    }

    galeria_imagenes = [
        'imagen1.jpg',
        'imagen2.jpg',
        'imagen3.jpg',
        # Agrega más imágenes según sea necesario
    ]

    return render_template('index.html', noticias=noticias, eventos=eventos, contacto=contacto, galeria_imagenes=galeria_imagenes)

if __name__ == '__main__':
    app.run(debug=True)

