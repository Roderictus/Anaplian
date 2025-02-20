import werkzeug.urls
import urllib.parse

# Agregamos url_quote si no existe (para compatibilidad con versiones recientes de Werkzeug)
if not hasattr(werkzeug.urls, "url_quote"):
    werkzeug.urls.url_quote = urllib.parse.quote

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
