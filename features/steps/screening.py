## INFO: using class inheritance

from behave import *


## TODO: import
import sys
# Add the models folder path to the sys.path list
sys.path.append('~/arch2019-test/hr-example-with-peewee')
# Now you can import your module
from models import *



## first
@given(u'the candidate has an experience of {ce:f} year and HR manager has an experience of {hr:f} year')
def step_impl(context, ce, hr):
    context.cand_name = 'J1'
    context.hr1 = HR.create(name='J1', experience=ce)
    context.candidate1 = Candidate.create(reviewed_by=context.hr1, name="C1", experience=hr)
    
##  update this test
@when("scanned by HR manager")
def step_impl(context):
    ## Querying and checking        
    context.scanning_results = context.candidate1.get_candidate_outcome(context.hr1)
    query = Candidate.update(decision=context.scanning_results).where(Candidate.name == context.candidate1.get_name)
    context.rest = query.execute()
    context.rest is not None


## TODO: get results from queries
#ExtraRound
#NoExtraRound
@then("next interview round is {roundstatus}")
def step_impl(context, roundstatus):
    # Print the outcome
    query = (Candidate
             .select(Candidate, HR)
             .join(HR)
             .where(Candidate.name == context.cand_name))

    for item in query:
        context.scanning_results = item.get_candidate_outcome()
        assert (context.scanning_results == roundstatus)


# @then("the canidate should go to additional interview round")
# def step_impl(context):
#     # Print the outcome
#         # Print the outcome
#     query = (Candidate
#              .select(Candidate, HR)
#              .join(HR)
#              .where(Candidate.name == context.cand_name))

#     for item in query:
#         context.scanning_results = item.get_candidate_outcome()
#         assert (context.scanning_results == "additional screening")
