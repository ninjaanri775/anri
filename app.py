
from ext import app

if __name__ == "__main__":
    from routes import subscriptions, home, features, shop, resources, login, product
    app.run(debug=True)