Feature: hire or not to hire (inheritance)
  In order to hire only qualified stuff,
  As a head of HR manager
  I want my candidates to be qualified enough
  based on their experience
  
  Scenario: Weak candidate and unexperienced HR
    Given the candidate has an experience less than one year and HR manager has an experience less than one year
     When scanned by HR manager
     Then the canidate should go to additional interview round
  
  Scenario: Strong candidate and unexperienced HR
    Given the candidate has an experience more than one year and HR manager has an experience less than one year
     When scanned by HR manager
     Then the candidate will be definetely hired

  Scenario: Strong candidate and experienced HR
    Given the candidate has an experience more than one year and HR manager is experienced
     When scanned by HR manager
     Then the canidate should go to additional interview round

 