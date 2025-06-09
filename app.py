# app.py
from flaskr import create_app

# Crea la instancia de la app usando la fábrica definida en flaskr/__init__.py
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
