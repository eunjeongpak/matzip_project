from run import db

class Restaurant(db.Model):
    __table__ = db.Model.metadata.tables['univ_restaurant']

    __mapper_args__ = {
        'primary_key': [__table__.c.index]
    }

    def __repr__(self):
        return f"index : {self.index}, name : {self.name}, category : {self.category}, rating : {self.rating}, review : {self.review}, link : {self.link}, address: {self.addr}, hour: {self.hour}, telephone: {self.tel}, university: {self.univ}"

# class New_restaurant(db.Model):
#     __table__ = db.Model.metadata.tables['univ_new_restaurant']
#
#     __mapper_args__ = {
#         'primary_key': [__table__.c.index]
#     }
#
#     def __repr__(self):
#         return f"name: {self.name}, category: {self.category}, address: {self.addr}, university: {self.univ}"

class New_restaurant(db.Model):
    __tablename__ = "univ_new"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    addr = db.Column(db.String())
    univ = db.Column(db.String())

    def __repr__(self):
        return f"name: {self.name}, category: {self.category}, address: {self.addr}, university: {self.univ}"

# db.create_all()