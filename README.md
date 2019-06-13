Python Web App
==============

A proof of concept for a deployable web app in Python.

Goals
-----

- learn what it takes to deploy a small we app to [Heroku](https://www.heroku.com)
- get a feeling of how its files could be organized in Python
- give a try to [Flask](https://github.com/pallets/flask)

Usage
-----

- the application is configured with a given color
- every time you visit the web page you get a different number and the color that was chosen

Development
-----------

```bash
# create a virtual environment (optional)
python -m venv venv # using Python 3, search for virtualenv for Python 2
# activate the virtual environment
./venv/bin/activate

# install the dependencies
pip install -r requirements.txt

# run the test suite
python test_numbersandcolors.py

# pick a color, configure the application to use it
export COLOR=turquoise

# run the application locally
FLASK_APP=numbersandcolors.py python -m flask run # then visit http://127.0.0.1:5000

# make changes, contribute ideas, have fun!
```
