from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome,prontuario,instituicao):
    return render_template('identificacao.html', nome=nome, prontuario=prontuario,instituicao=instituicao )


@app.route('/contextorequisicao/<nome>')
def contextoReq(nome):
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    domain = request.url_root
    return render_template("contextoreq.html", nome=nome, useragent=user_agent, ip=ip, host=domain)
