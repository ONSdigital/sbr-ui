from sbr_ui import app
from sbr_ui.views.home import home_bp
from sbr_ui.views.login import login_bp
from sbr_ui.views.errors import error_bp


app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(home_bp, url_prefix='/Home')
app.register_blueprint(error_bp, url_prefix='/Error')