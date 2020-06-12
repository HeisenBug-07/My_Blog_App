from myproject import db


class Posts(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.Integer, nullable=False)
    heading = db.Column(db.String, nullable=False)
    sub_heading = db.Column(db.String, nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.String, nullable=False)

    def __init__(self, heading, sub_heading, content, date, slug):
        self.heading = heading
        self.sub_heading = sub_heading
        self.content = content
        self.date = date
        self.slug = slug


class Contacts(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    feedback = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    def __init__(self, name, email, feedback, date):
        self.name = name
        self.email = email
        self.feedback = feedback
        self.date = date
