

from datetime import timedelta
from config import config
from flask_jwt_extended import JWTManager

from flask import Flask, redirect

from models.kategori import Category
from models.news import News

from blueprints.auth_blueprints import authBp
from blueprints.news_blueprint import newsBp
from blueprints.category_blueprints import categoryBp
from blueprints.tag_blueprint import tagBp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = config["jwt_secret"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=5)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
JWTManager(app)


@app.route("/")
def index():
    return redirect("/news")


app.register_blueprint(tagBp)
app.register_blueprint(categoryBp)
app.register_blueprint(authBp)
app.register_blueprint(newsBp)

app.run(debug=True)
