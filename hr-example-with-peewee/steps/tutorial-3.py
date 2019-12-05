## INFO: using class inheritance

from behave import *


## TODO: import
import sys
# Add the models folder path to the sys.path list
sys.path.append('~/arch2019-test/hr-example-with-peewee')
# Now you can import your module
from models import *

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
