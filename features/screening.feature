Feature: hire or not to hire (inheritance)
  In order to reduce specialist workload on job interviews without sacrificing quality,
  I want to schedule additional interviews automatically based on experience of candidates and HR managers
  
  Scenario: Weak candidate and unexperienced HR
    Given the candidate has an experience of 0.5 year and HR manager has an experience of 0.4 year
     When scanned by HR manager
     Then next interview round is ExtraRound
  
  Scenario: Strong candidate and unexperienced HR
    Given the candidate has an experience of 1.5 year and HR manager has an experience of 0.4 year
     When scanned by HR manager
     Then next interview round is NoExtraRound

  Scenario: Strong candidate and experienced HR
    Given the candidate has an experience of 2.5 year and HR manager has an experience of 2.4 year
     When scanned by HR manager
     Then next interview round is NoExtraRound

 