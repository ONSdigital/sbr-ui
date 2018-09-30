from sbr_ui import app
from sbr_ui.routes.authentication import authentication_bp

app.register_blueprint(authentication_bp, url_prefix='/auth/')
