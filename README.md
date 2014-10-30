Introduction
============

MedChecker by Fivium is currently conceptual demo based on open source software as part of the OPENeP project that aims to create software for the NHS. As it currently stands the software is in a demonstration state only and demonstrates UI concepts rather than a fully working system.

This project has been written in Python using the Django framework.


Setup Instructions
==================

Required Software
-----------------

The following software is required to carry out development, no insturctions are given for installing this software
- [Python 2.7](https://www.python.org/downloads/)
- [pip](https://pypi.python.org/pypi/pip)
- [virtualenv](http://virtualenv.readthedocs.org/en/latest/) (can be installed via `pip install virtualenv`)
- [PostgreSQL Database (9.3)](http://www.postgresql.org/download/) (it is not recommended that you use sqlite)
- [node.js](http://nodejs.org/download/) & npm
- [bower](h ttp://bower.io/#install-bower) (can be installed via `npm install bower`)


Getting the Source Code
-----------------------

Once you have all the rquired software, simply clone this repository.


Virtualenv Setup
----------------

The best way to run this project is using pythons virtualenv. This isolates your deployment and helps ensure that project dependencies are working correctly. Read more about it [here](http://virtualenv.readthedocs.org/en/latest/).

1. Navigate to the cloned repository and run `virtualenv .` to instantiate the current directory as a virtualenv.
5. To activate your virtualenv run:

    __*nix:__    `source bin/activate` or __Windows:__ `Scripts\activate.bat`

6. You should now see that your command prompt has changed indicate the current virtualenv running. Any python packges you install within this sandboxed environment will be installed for this virtualenv only and only be available if the virtualenv is active.


Development
-----------

1. Ensure that your virtualenv is activated
2. Navigate to the directory containing this cloned repository and run `pip install -r requirements/local.py` to install the python dependencies.
3. Install the web dependancies using bower with `bower install`
3. Create a database using postgres (the easiest method is via the pgadmin tool).
4. Verify that the settings in medchecker/medchecker/settings/local.py are correct.
4. Change directory to medchecker.
5. Setup the database using the django tools `./manage.py migrate`.
6. Run the server with `./manage.py runserver`
7. Point your browser to `http://localhost:8000`
