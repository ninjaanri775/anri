from flask import  render_template, redirect, request
from flask_login import login_user, logout_user, login_required, current_user

from models import Shopin, User
from os import path

from ext import app,db

from form import loginform, productform, registerform
products = [
    {
        "price": "Free",
        "name": "Free",
        "com": "Limited features",
        "button": "Cancel plan",
        "id": 0,
        "description1": "Basic Design Templates",
        "description2": "Basic AI Design Assistance",
        "description3": "Limited Design Elements",
        "description4": "Community Support",
        "description5": "Good resolution"
    },
    {
        "price": "8.99$",
        "name": "Pro",
        "com": "Best we got",
        "button": "Update Now",
        "id": 1,
        "description1": "Premium Design Templates",
        "description2": "Personalized  AI Design Assistance",
        "description3": "Full acces  Design Elements",
        "description4": "Community  Support",
        "description5": "Best resolution"
    },
    {
        "price": "4.99$",
        "name": "Plus",
        "com": "Better than free",
        "button": "Update Now",    
        "id": 2,
        "description1": "Premium  Design Templates",
        "description2": "Personalized   AI Design Assistance",
        "description3": " Full Access to Design Elements",
        "description4": "24/7 Priority Support",
        "description5": "No Watermarked Downloads"
    }
]

profiles = []



@app.route("/create", methods=("GET", "POST"))
def create():
    form = productform()
    if form.validate_on_submit():
        newproduct = Shopin(name=form.name.data, price=form.price.data)

        image = form.img.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)

        newproduct.img = image.filename

        db.session.add(newproduct)
        db.session.commit()

        return redirect("/shop")

    print(form.errors)
    return render_template("create.html", form=form)

@app.route("/shop/<int:shop_id>")
def view_shop(shop_id):
    shop = Shopin.query.get_or_404(shop_id)
    return render_template("items.html", shop=shop)

@app.route("/shop/delete/<int:shop_id>", methods=["POST"])
@login_required  
def delete_shop(shop_id):
    shop = Shopin.query.get_or_404(shop_id)
    db.session.delete(shop)
    db.session.commit()
    shops = Shopin.query.all()
    return render_template("shop.html", shops=shops, role="Admin")



@app.route('/update')
def update():
    products = Shopin.query.all()
    return render_template('update.html', products=products)

@app.route('/update_price', methods=['POST'])
def update_price():
    product_id = request.form.get('product_id')
    new_price = request.form.get('price')
    
    if product_id and new_price:
        try:
            new_price = int(new_price)
            product = Shopin.query.get(product_id)
            if product:
                product.price = new_price
                db.session.commit()
        except ValueError:
            pass

    return render_template("index.html")

@app.route("/subscriptions")
@login_required
def subscriptions():
    return render_template("subscriptions.html", products=products)

@app.route("/product/<int:product_id>")
@login_required
def product(product_id):
    return render_template("products.html", product=products[product_id])




@app.route("/")
def home():
    return render_template("index.html", )


@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/shop")
@login_required
def shop():
    shops = Shopin.query.all()
    return render_template("shop.html", shops=shops,)


@app.route("/resources" )
def resources():
    return render_template("resources.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginform()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            login_user(user, remember=True)

        return redirect("/")
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = registerform()
    if form.validate_on_submit():
        new_user= User(username=form.username.data, password=form.password.data)


        db.session.add(new_user)
        db.session.commit()

        return redirect("/")
    print(form.errors)
    return render_template("register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
