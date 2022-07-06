from models import db, Pet
from app import app


db.drop_all()
db.create_all()

Pet.query.delete()


pearl = Pet(name='Pearl', species='cat', age=3, photo_url='https://images.squarespace-cdn.com/content/v1/54783cdfe4b01e4f655402fe/1599738224677-2I1ZO6NJ3VS052FDCD4I/SINGAPORE+SEAL+MITTED+PLAYGROUND+RAGDOLL.JPG',
            notes='Pearl is a female Mitted Ragdoll cat. She is very cuddly')

teddy = Pet(name='Teddy', species='dog', age=5, photo_url='https://s36700.pcdn.co/wp-content/uploads/2019/11/2010_Sheltie_getty172950770.png',
            notes='Teddy is a Sheltie. He will play with you all day if you let him!')


db.session.add_all([pearl, teddy])
db.session.commit()
