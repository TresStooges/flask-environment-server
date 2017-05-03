from app import db, models
from models import Property


db.session.query(models.Property).delete()
db.session.commit()

property1 = Property(1, 'Classroom', 72,
                     'amazon.com/images'
                     )


#   '\xe7\xe9' add this to property

db.session.add(property1)
db.session.commit()
