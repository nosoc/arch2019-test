## INFO: using class inheritance

from behave import *

## INFO: using class inheritance

class person_inheritance:

    # Define initialization method
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    # getter for experience
    def get_experience(self):
        return(self.experience)


class hr(person_inheritance):
    def __init__(self, name, experience):
        super().__init__(name, experience)

    # Define get outcome for candidate
    # given information about HR who
    # is reviewing the candidate 
    def get_candidate_outcome(self, candidate_instance):
        if ((self.get_experience() < 1) & (candidate_instance.get_experience() < 1) ):
            decision = "additional screening"
        elif ((self.get_experience() < 1) & (candidate_instance.get_experience() > 1) ):
            decision = "hired"
        else:
            decision = "additional screening"
        # Return an outcome of the screening
        return(decision)


class candidate(person_inheritance):
    def __init__(self, name, experience):
        super().__init__(name, experience)


candidate_instance = candidate("Jonh", .6)
hr_junior = hr("Julia", .7)
hr_junior.get_candidate_outcome(candidate_instance)
            

## first
@given("the candidate has an experience less than one year")
def step_impl(context):
    # Instantiate candidate instance
    # with an experience given as integer
    # in years
    context.candidate_instance = candidate("Jonh", .6)
    context.hr_junior = hr("Julia", .7)


## first
@given("the candidate has an experience less than one year and HR manager has an experience less than one year")
def step_impl(context):
    context.candidate_instance = candidate("Jonh", .4)
    context.hr_junior = hr("Julia", .7)

    
## second
@given("the candidate has an experience more than one year and HR manager has an experience less than one year")
def step_impl(context):
    context.candidate_instance = candidate("Jonh", 1.4)
    context.hr_junior = hr("Julia", .7)
    
## third
@given("the candidate has an experience more than one year and HR manager is experienced")
def step_impl(context):
    context.candidate_instance = candidate("Jonh", 1.6)
    context.hr_junior = hr("Julia", 2.7)


@when("scanned by HR manager")
def step_impl(context):
    context.scanning_results = context.hr_junior.get_candidate_outcome(context.candidate_instance)
    context.scanning_results is not None
    
@then("the candidate will be definetely hired")
def step_impl(context):
    # Print the outcome
    assert (context.scanning_results == "hired")


@then("the canidate should go to additional interview round")
def step_impl(context):
    # Print the outcome
    assert (context.scanning_results == "additional screening")
