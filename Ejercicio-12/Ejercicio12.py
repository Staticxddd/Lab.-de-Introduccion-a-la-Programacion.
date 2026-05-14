from flask import Flask, render_template, jsonify

app = Flask(__name__)

catalogo = [
    {
        "codigo": "A101",
        "nombre": "Teclado",
        "precio": 950,
        "imagen": "https://picsum.photos/200?1"
    },
    {
        "codigo": "B202",
        "nombre": "Mouse",
        "precio": 650,
        "imagen": "https://picsum.photos/200?2"
    },
    {
        "codigo": "C303",
        "nombre": "Monitor",
        "precio": 3200,
        "imagen": "https://picsum.photos/200?3"
    }
]

@app.route("/")
def inicio():
    return render_template("si.html")

@app.route("/api/productos")
def productos():
    return jsonify(catalogo)

@app.route("/api/producto/<codigo>")
def producto(codigo):
    item = next(
        (producto for producto in catalogo
         if producto["codigo"] == codigo),
        None
    )

    if item:
        return jsonify(item)

    return jsonify({
        "mensaje": "No existe el producto"
    }), 404


if __name__ == "__main__":
    app.run(port=5000)