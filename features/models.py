from peewee import *
from playhouse.hybrid import *

## INFO: using peewee ORM

db_hr = SqliteDatabase('hr_2.db')
db_hr.connect()

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

