class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.name)


class NewChar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charname = db.Column(db.String(120))
    charrace = db.Column(db.String(32))
    charlevel = db.Column(db.Integer(2))
    charalign = db.Column(db.String(32), nullable=True)
    charclass = db.Column(db.String(32))
    charbkgrd = db.Column(db.String(32), nullable=True)

    def __repr__(self):
        return '<NewChar {}>'.format(self.name)
