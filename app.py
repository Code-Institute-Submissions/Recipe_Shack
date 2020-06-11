import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("NONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/catergories")
def catergories():
    return render_template("catergories.html")

@app.route("/catergories/breakfast")
def breakfast():
    recipes = mongo.db.recipes.find()
    print(recipes)
    return render_template("breakfast.html", recipes = recipes)
   

@app.route("/recipe/<id>")
def recipe(id=None):
    print(id)
    return render_template("recipe.html", recipes = mongo.db.recipes.find())

@app.route("/add-recipe")
def addrecipe():
    categories = mongo.db.Categories.find()
    return render_template("add-recipe.html", categories = categories)

@app.route("/test")
def test():
    recipes = mongo.db.recipes.find()
    print(recipes)
    return render_template("test.html", recipes = recipes)

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)