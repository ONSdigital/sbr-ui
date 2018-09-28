from sbr_ui import app
from sbr_ui.routes.authentication import authentication_bp
from sbr_ui.routes.api import api_bp

app.register_blueprint(authentication_bp, url_prefix='/auth/')
app.register_blueprint(api_bp, url_prefix='/api/')