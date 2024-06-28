from ext import db, app
from models import Shopin, User

with app.app_context():
    db.drop_all()
    db.create_all()

    admin_user = User(username="Admin", password="yamerooowryyy", role="admin")
    db.session.add(admin_user)
    db.session.commit()