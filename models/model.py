from run import db

class Restaurant(db.Model):
    __table__ = db.Model.metadata.tables['univ_restaurant']

    __mapper_args__ = {
        'primary_key': [__table__.c.index]
    }

    def __repr__(self):
        return f"index : {self.index}, name : {self.name}, category : {self.category}, rating : {self.rating}, review : {self.review}, link : {self.link}, address: {self.addr}, hour: {self.hour}, telephone: {self.tel}, university: {self.univ}"
