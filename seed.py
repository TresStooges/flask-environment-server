from app import db, models
from models import Property


db.session.query(models.Property).delete()
db.session.commit()

property1 = Property('1062 Delaware St, Denver, CO 80204', 72, db.func.now(),
                     'https://d2tovwv1y8kfyq.cloudfront.net/wp-content/uploads/2015/02/18201559/1062-Delaware-Street-tif-files-002.jpg'
                     )

db.session.add(property1)
db.session.commit()
