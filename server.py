from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nostros():
    return render_template("sobrenosotros.html")

@app.route('/services')
def services():
    return render_template ("services.html")

@app.route('/nuestros_vehiculos')
def Nuestros_vehiculos():
    return render_template ("nuestrovehiculos.html")

@app.route('/novedades')
def novedades():
    return render_template ("novedades.html")

@app.route('/contactanos')
def contactanos():
    return render_template ("contactanos.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
 