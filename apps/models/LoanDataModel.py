from apps.models import Model
from orator.orm import belongs_to
#from apps.models.BorrowerDataModel import Borrower

class Loan(Model):
    __table__ = 'loan'
    __primary_key__ = 'loanid'

    # @belongs_to(foreign_key='cif')
    # def borrower(self):
    #     return Borrower