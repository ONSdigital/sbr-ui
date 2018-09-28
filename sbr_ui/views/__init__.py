from sbr_ui import app
from sbr_ui.views.home import home_bp
from sbr_ui.views.login import login_bp
from sbr_ui.views.errors import error_bp
from sbr_ui.views.unit_pages import ent_bp, leu_bp, ch_bp, paye_bp, vat_bp


app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(home_bp, url_prefix='/Home')
app.register_blueprint(error_bp, url_prefix='/Error')
app.register_blueprint(leu_bp, url_prefix='/LEU')
app.register_blueprint(ent_bp, url_prefix='/ENT')
app.register_blueprint(vat_bp, url_prefix='/VAT')
app.register_blueprint(ch_bp, url_prefix='/CH')
app.register_blueprint(paye_bp, url_prefix='/PAYE')