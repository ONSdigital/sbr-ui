from sbr_ui import app
from sbr_ui.routes.authentication import authentication_bp
from sbr_ui.routes.errors import error_bp
from sbr_ui.routes.unit_pages import search_bp, unit_pages_bp

app.register_blueprint(authentication_bp, url_prefix='/')
app.register_blueprint(error_bp, url_prefix='/Error')
app.register_blueprint(search_bp)
app.register_blueprint(unit_pages_bp, url_prefix='/Search')
