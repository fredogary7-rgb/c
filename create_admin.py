from app import app, db, User
from werkzeug.security import generate_password_hash

ADMINS = [
    {"username": "adAmine", "email": "admin@example.com", "phone": "0000000000", "password": "LuMinA123"},
    {"username": "testroot", "email": "testroot@example.com", "phone": "0000000001", "password": "TestRoot@2026"},
]

with app.app_context():
    for a in ADMINS:
        user = User.query.filter_by(username=a["username"]).first()
        if user is None:
            user = User(
                username=a["username"],
                email=a["email"],
                phone=a["phone"],
                password=generate_password_hash(a["password"]),
                is_admin=True,
            )
            db.session.add(user)
            db.session.commit()
            print(f"Admin '{a['username']}' créé avec succès !")
        else:
            if not getattr(user, "is_admin", False):
                user.is_admin = True
                db.session.commit()
                print(f"'{a['username']}' promu au rang admin.")
            else:
                print(f"Admin '{a['username']}' déjà présent.")


