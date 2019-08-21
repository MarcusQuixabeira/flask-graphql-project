import graphene
from graphene_mongo import MongoengineObjectType
from models.models import LoanModel

class Loan(MongoengineObjectType):
    class Meta:
        model = LoanModel

class Query(graphene.ObjectType):
    loans = graphene.List(Loan)

    def resolve_loans(self, info):
        return list(LoanModel.objects.all())