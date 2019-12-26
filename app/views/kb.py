from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.models.article import Article
from app.views._base import build_instance_from_form

bp = Blueprint('kb', __name__)


@bp.route('/')
def index():
    articles = Article.select().order_by(Article.id)
    return render_template('kb/index.jade', articles=articles, title='Список статей')

@bp.route('/articles/new', methods=['GET'])
def new():
    article = Article()
    return render_template("kb/new.jade", article=article, url=url_for('kb.create'), title='Новая статья')

@bp.route('/articles/new', methods=['POST'])
def create():
    article = build_instance_from_form(Article(), request.form)
    article.parent = None
    if article.save():
        return redirect(url_for('kb.index'))
    return render_template("kb/new.jade", url=url_for('kb.create'))


