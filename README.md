Chance to shine
=========================================================


Overview
-------------------------
This repository contains some of the code that was used to train my team during the CDT's data aid initiative, all confidentital code and data have been removed, instead we show some of the code using the open source fifa10 dataset
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

If you are failing on flake8 errors a good starting point that will fix lots of them is to run [black](https://github.com/psf/black). This will automatically fix lots of formatting such as spaces, bad commas ect.

`
black something.py
`

Also see similar one for notebooks called  [nb-black](https://pypi.org/project/nb-black/). At the top of your notebook add 

`
%load_ext nb_black
`


We will write the majority of the code in the shine module but we will present results/visualisations using notebooks and we will add these [here](https://github.com/rgreen1995/Chance_to_shine/tree/main/notebooks), notebooks are hard to review. So the peer review will happen mostly on the code via pull requests. See git section below

Help
-------------------------
Follow the steps below to set up the repo 

[Setting up repo](https://github.com/rgreen1995/Chance_to_shine/wiki/Setting-up-repository)

[Environments](https://github.com/rgreen1995/Chance_to_shine/wiki/Environments)

[Git and Branching](https://github.com/rgreen1995/Chance_to_shine/wiki/Git-and-Branching)

**Please remember to run tox before submiting any changes, and to submit all changes via a pull request in a new branch**

Trello 
-------------------------
[Planning board](https://trello.com/b/2XCA7WDI/chance-to-shine)

Meeting notes
-------------------------
[First meeting](https://github.com/rgreen1995/Chance_to_shine/wiki/First-Meeting-(04-11-20))




