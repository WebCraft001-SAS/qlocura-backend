# flaskr/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
import os

from .modelos.modelo import db, RolesEnum, EstadoPedidoEnum
from .modelos import Usuarios, Roles
from .vistas.vistas import (
    VistaSignin,
    VistalogIn,
    UsuariosResource,
    ProductosResource,
    PedidoResource,
    ReportePedidoResource,
    PedidoPorUsuarioYEstadoResource,
    PerfilUsuario
)
#pp
def create_app(config_name='default'):
    app = Flask(__name__)
    print("DATABASE_URL en runtime:", os.environ.get('DATABASE_URL'))

    # Configuración de la base de datos PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neondb_owner:npg_rX7lAiN2TYWt@ep-nameless-sound-a8womhp2-pooler.eastus2.azure.neon.tech/qlocura?sslmode=require'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    # Inicializar extensiones
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    CORS(app)

    # Configuración de la API RESTful
    api = Api(app,
            version='1.0',
            title='API de Qlocura',
            description='Documentación de la API RESTful para el sistema de pedidos Qlocura',
            doc='/docs')

    # Rutas públicas
    api.add_resource(VistaSignin, '/signin')
    api.add_resource(VistalogIn, '/login')
#jsdfdd
    # Rutas protegidas / administrativas
    api.add_resource(UsuariosResource, '/usuarios', '/usuarios/<int:id>')
    api.add_resource(ProductosResource, '/productos', '/productos/<int:id>')
    api.add_resource(PedidoResource, '/pedidos', '/pedidos/<int:id>')
    api.add_resource(ReportePedidoResource, '/reportes_pedidos', '/reportes_pedidos/<int:id>')
    api.add_resource(PerfilUsuario, '/perfil')

    # Rutas con filtros por estado
    api.add_resource(PedidoPorUsuarioYEstadoResource, '/pedidos/estado/<string:estado>')
    api.add_resource(PedidoPorUsuarioYEstadoResource, '/pedidos/usuario/estado/<string:estado>')
    api.add_resource(PedidoPorUsuarioYEstadoResource, '/pedidos/usuario/estado/<string:estado>/<int:id>')

    return app
app = create_app()
