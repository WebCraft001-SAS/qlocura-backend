# app.py
import os
from flaskr import create_app

app = create_app()

if __name__ == '__main__':
    # Usa el puerto que Render te da, o 5000 localmente
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
