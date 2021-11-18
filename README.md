# python-flusk

### Prerequisities

1. Install Python: https://www.python.org/downloads/. Or use Homebrew: 

```
brew install python
python --version # Check version
```

[optional] You can create an alias on your .bash_profile

```
# .bash_profile

alias python=python3
```

2. (If you have problem installing pip) Install pip:

```
python -m ensurepip --upgrade

```

Upgrading pip:

```
python -m pip install --upgrade pip
```

pip documentation: https://pip.pypa.io/en/stable/installation/

2. Install virtual env:

```
pip install virtualenv
```

- To create a virtualenv:

```
cd project/
virtualenv venv
```

- Activate virtualenv

```
source venv/bin/activate
```

Now you can install all your module without conflicts with other project.


- Deactivate virtualenv

```
deactivate
```

3. [optional] install Virtualenvwrapper:

virtualenvwrapper keeps all the virtual environments in ~/.virtualenv while virtualenv keeps them in the project directory.

```
pip install virtualenvwrapper
```

4. Install setuptools:

```
python3 -m pip install --upgrade pip setuptools wheel
```

5. [optional] Directory will be treated as a package, (-e means editable):

```
pip install -e .

```

###### NOTE:

When setting a Python project you should have a requirements.txt. If it doesn't exist:

```
pip freeze # list all require dependencies
pip freeze > requirements.txt # save dependencies in a file.
```

### Getting started

Install project dependencies:

```
pip install -r requirements.txt
```

### Create Server

Initialise the server:

```
python server.py
```

### Run test

```
pytest -p no:warnings
```