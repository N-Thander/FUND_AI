from . import db

class UserData(db.Model):
    __tablename__ = 'userdata'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email_id = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.BigInteger, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    @staticmethod
    def gererate_user_id():
        last_user = db.session.query(UserData).order_by(UserData.user_id.desc()).first()
        last_id_number = None
        if last_user:
            last_id_number = int(last_user.user_id.split('_')[1])
        else:
            last_id_number = 0
        new_id_number = last_id_number + 1
        new_user_id = f"USER_{new_id_number:%06d}"
        return new_user_id
        
