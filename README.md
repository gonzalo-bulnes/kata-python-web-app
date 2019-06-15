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

[![Build Status](https://travis-ci.org/gonzalo-bulnes/kata-python-web-app.svg?branch=master)](https://travis-ci.org/gonzalo-bulnes/kata-python-web-app)
[![Demo](https://img.shields.io/badge/demo-colorsandnumbers-7057C0.svg)](https://numbersandcolors.herokuapp.com)

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

### Deployment to Heroku

#### Manual

```bash
# install the Heroku CLI, then:
heroku login -i

# intitial setup
heroku git:remote -a numbersandcolors # or any name you like

# to deploy:
git push heroku master
# to configure the app:
heroku set:config COLOR=turquoise

# then visit: https://numbersandcolors.herokuapp.com (or https://your-preferred-name.herokuapp.com)
```

#### Automatic

Press the button to deploy this app to your [Heroku](https://heroku.com) account! _A free Heroku account should suffice._

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Notes

- Remember to add any new dependency to `requirements.txt` with `pip freeze`! On Ubuntu (and other Debian systems) `pip freeze > requirements.txt` outputs some undue configuration. If that's the case for you, prefer: `pip freeze | grep -v "pkg-resources" > requirements.txt`.

Credits
-------

The carrot emoji used as logo belongs to Google and [was published under the Apache License v2.0 as part of Noto Emoji](https://github.com/googlei18n/noto-emoji).

License
-------

### Documentation

    Copyright (C) 2019 Gonzalo Bulnes Guilpain

    Permission is granted to copy, distribute and/or modify this document under the terms
    of the GNU Free Documentation License, Version 1.3 or any later version published by
    the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and
    no Back-Cover Texts. A copy of the license can be found at
    <http://www.gnu.org/copyleft/fdl.html>.

### Code

Except for the contents of the [doc/](./doc) directory, this code is in the public domain.
