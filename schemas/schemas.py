import graphene
from graphene_mongo import MongoengineObjectType
from models.models import Loan

class LoanType(MongoengineObjectType):
    class Meta:
        model = Loan

class Query(graphene.ObjectType):
    loans = graphene.List(LoanType)
    loan = graphene.Field(LoanType, _id=graphene.String())
    borrower_loans = graphene.List(LoanType, borrower_id=graphene.String())

    def resolve_loans(self, info, **kwargs):
        return list(Loan.objects.all())
    
    def resolve_loan(self, info, _id):
        return Loan.objects.get(_id=_id)
    
    def resolve_borrower_loans(self, info, borrower_id):
        return list(Loan.objects(borrower_id=borrower_id))