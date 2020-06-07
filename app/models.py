from app import db


class Icon(db.Model):
    icon_id = db.Column(db.String(255), index=True, primary_key=True)
    name = db.Column(db.String(64))
    base64 = db.Column(db.String(), unique=True)

    def __repr__(self):
        return f"<Icon {self.name}> {self.icon_id}"