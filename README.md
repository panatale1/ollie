**If on Ubuntu:**
Run `sudo ./initial_setup` to ensure installation of PostgreSQL, Python, and pip.
Then run `./local_setup` to ensure virtualenv and virtualenvwrapper are installed.
From there, run `mkvirtualenv ollie` and `workon ollie`, then `pip install -r requirements.txt`.
*If* `mkvirtualenv ollie` *does not work, run* `source $(which virtualenvwrapper.sh)` *and then try again.*


**If not on Ubuntu:**
Install Python, PostgreSQL, and pip. Then run:
`pip install virtualenv virtualenvwrapper`
followed by `source $(which virtualenvwrapper.sh)`
then `mkvirtualenv ollie` and `workon ollie` followed by `pip install -r requirements.txt`.


After package installation, go to the mid-level ollie folder and run `./manage.py migrate`.
After the migration has run, run `./manage.py runserver` and go to `localhost:8000` in the browser to use the application.
