## INFO: using class inheritance

from behave import *
from peewee import *
from playhouse.hybrid import *

db_hr = SqliteDatabase('hr_2.db')
db_hr.connect()

## INFO: using peewee ORM

class HR(Model):
    
    name = CharField()
    experience = IntegerField()
    
    # getter for experience
    @hybrid_method
    def get_experience(self):
        return(self.experience)
            
    class Meta:
        database = db_hr # This model uses the "people.db" database.


## update values
## before doing that, create candidates
## with status like "pending"

class Candidate(Model):
    
    reviewed_by = ForeignKeyField(HR, backref='candidates')
    
    name = CharField()
    experience = IntegerField()
    decision = CharField(default="pending")
    
    @hybrid_property
    def get_name(self):
        return(self.name)
    
    # getter for experience
    # FIXME: rewrite using props
    @hybrid_method
    def get_experience(self):
        return(self.experience)

    # Define get outcome for candidate
    # given information about HR who
    # is reviewing the candidate 
    @hybrid_method
    def get_candidate_outcome(self, hr_person):
        if ((hr_person.get_experience() < 1) & (self.get_experience() < 1) ):
            self.decision = "additional screening"
        elif ((hr_person.get_experience() < 1) & (self.get_experience() > 1) ):
            self.decision = "hired"
        else:
            self.decision = "additional screening"
            # Return an outcome of the screening
        return(self.decision)
    
    class Meta:
        database = db_hr # This model uses the "people.db" database.


db_hr.create_tables([HR, Candidate])

# hr1 = HR.create(name='J1', experience=0.6)
# hr2 = HR.create(name='J2', experience=0.7)

# candidate1 = Candidate.create(reviewed_by=hr1, name="C1", experience=0.6)
# candidate2 = Candidate.create(reviewed_by=hr2, name="C2", experience=1.6)

## FIXME: rewrite withiut using context global


## first
# @given("the candidate has an experience less than one year")
# def step_impl(context):
#     # Instantiate candidate instance
#     # with an experience given as integer
#     # in years
#     # context.hr1 = HR.create(name='J1', experience=0.6)
#     # context.candidate1 = Candidate.create(reviewed_by=context.hr1, name="C1", experience=0.6)
#     hr1 = HR.create(name='J1', experience=0.6)
#     candidate1 = Candidate.create(reviewed_by=context.hr1, name="C1", experience=0.6)


## first
@given("the candidate has an experience less than one year and HR manager has an experience less than one year")
def step_impl(context):
    context.cand_name = "J1"
    context.hr1 = HR.create(name='J1', experience=0.6)
    context.candidate1 = Candidate.create(reviewed_by=context.hr1, name="C1", experience=0.6)
    # hr1 = HR.create(name='hr junior', experience=0.6)
    # candidate1 = Candidate.create(reviewed_by=context.hr1, name="candidate junior", experience=0.6)

    
## second
@given("the candidate has an experience more than one year and HR manager has an experience less than one year")
def step_impl(context):
    context.cand_name = "J2"
    context.hr1 = HR.create(name='J2', experience=2)
    context.candidate1 = Candidate.create(reviewed_by=context.hr1, name="C2", experience=0.6)
    # hr1 = HR.create(name='hr experienced', experience=1.6)
    # candidate1 = Candidate.create(reviewed_by=context.hr1, name="candidate junior", experience=0.6)
    
## third
@given("the candidate has an experience more than one year and HR manager is experienced")
def step_impl(context):
    context.cand_name = "J3"
    context.hr1 = HR.create(name='J3', experience=2)
    context.candidate1 = Candidate.create(reviewed_by=context.hr1, name="C3", experience=2)
    # hr1 = HR.create(name='hr experienced', experience=1.6)
    # candidate1 = Candidate.create(reviewed_by=context.hr1, name="candidate experienced", experience=2.6)



## TODO: update this test
@when("scanned by HR manager")
def step_impl(context):
    ## Querying and checking        
    context.scanning_results = context.candidate1.get_candidate_outcome(context.hr1)
    query = Candidate.update(decision=context.scanning_results).where(Candidate.name == context.candidate1.get_name)
    context.rest = query.execute()
    context.rest is not None


## TODO: get results from queries
@then("the candidate will be definetely hired")
def step_impl(context):
    # Print the outcome
    query = (Candidate
             .select(Candidate, HR)
             .join(HR)
             .where(Candidate.name == context.cand_name))

    for item in query:
        context.scanning_results = item.get_candidate_outcome()
        assert (context.scanning_results == "hired")


@then("the canidate should go to additional interview round")
def step_impl(context):
    # Print the outcome
        # Print the outcome
    query = (Candidate
             .select(Candidate, HR)
             .join(HR)
             .where(Candidate.name == context.cand_name))

    for item in query:
        context.scanning_results = item.get_candidate_outcome()
        assert (context.scanning_results == "additional screening")
