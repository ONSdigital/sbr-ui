from sbr_ui import app
from sbr_ui.views.authentication import login_bp, logout_bp
from sbr_ui.views.errors import error_bp
from sbr_ui.views.unit_pages import search_bp, unit_pages_bp

app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(logout_bp, url_prefix='/')
app.register_blueprint(error_bp, url_prefix='/Error')
app.register_blueprint(search_bp)
app.register_blueprint(unit_pages_bp, url_prefix='/Search')
