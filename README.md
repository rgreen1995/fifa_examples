Chance_to_shine
=========================================================


Overview
-------------------------


Roles
-------------------------
* Robbie will lead the analysis looking mostly at teacher confidence - see wiki [here](https://github.com/rgreen1995/Chance_to_shine/wiki/Teacher-Confidence) for more info
* Matt will lead on the student participant data in schools - see wiki [here](https://github.com/rgreen1995/Chance_to_shine/wiki/School-Participant) for more info
* Joel will lead on the street participant data - see wiki [here](https://github.com/rgreen1995/Chance_to_shine/wiki/Street-participant) for more info
* Tonicha is lead communicator and so will guide the analysts using her discussions with the charity
* Rhys will PM and ensure that the team is ready for the hackathon day

Repo Structure
-------------------------

Code lives in [shine](https://github.com/rgreen1995/Chance_to_shine/tree/main/src/shine), this can then be used as e.g:

`
from shine import analysis
`

When adding code try to add a test for every function, these live in [tests](https://github.com/rgreen1995/Chance_to_shine/tree/main/tests), to run tests either run 

`
pytest tests/
`

We also have a [tox](https://tox.readthedocs.io/en/latest/) file which will run these tests, as well as check for pep8 via [flake8](https://flake8.pycqa.org/en/latest/) and type hinting via [mypy](https://mypy.readthedocs.io/en/stable/) . To run this, in command line just run 

`
tox
`

We will write the majority of the code in the shine module but we will present results/visualisations using notebooks and we will add these [here](https://github.com/rgreen1995/Chance_to_shine/tree/main/notebooks), notebooks are hard to review. So the peer review will happen mostly on the code via pull requests. See git section below


Meeting notes
-------------------------
[First meeting](https://github.com/rgreen1995/Chance_to_shine/wiki/First-Meeting-(04-11-20))

Trello 
-------------------------
[Planning board](https://trello.com/b/2XCA7WDI/chance-to-shine)

Help
-------------------------
[Git and Branching](https://github.com/rgreen1995/Chance_to_shine/wiki/Git-and-Branching)
