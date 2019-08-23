from mongoengine import Document
from mongoengine.fields import StringField, LongField, FloatField, ObjectIdField

class Loan(Document):
    meta = {
      'collection': 'loans',
      'strict': False,
    }
    _id = ObjectIdField()
    borrower_id = ObjectIdField()
    loan_category = StringField()
    city = StringField()
    state = StringField()
    zip_code = StringField()
    stage = StringField()
    number = StringField()
    value = FloatField()