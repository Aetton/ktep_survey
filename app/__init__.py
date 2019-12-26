import os

from flask import Flask
from peewee import PostgresqlDatabase


"""Create and configure an instance of the Flask application."""
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.config.from_pyfile('config.py')

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route("/hello")
def hello():
    return "Hello, World!"


db = PostgresqlDatabase(
    app.config.get("DB_NAME"),
    user=app.config.get("DB_USERNAME"),
    password=app.config.get("DB_PASSWORD"),
    host=app.config.get("DB_HOST"),
    port=app.config.get("DB_PORT"),
    autorollback=True)


# apply the blueprints to the app
from app.views import kb
#from app.views import auth


#app.register_blueprint(auth.bp)
app.register_blueprint(kb.bp)

# make url_for('index') == url_for('blog.index')
# in another app, you might define a separate main index here with
# app.route, while giving the blog blueprint a url_prefix, but for
# the tutorial the blog will be the main index
app.add_url_rule("/", endpoint="index")

