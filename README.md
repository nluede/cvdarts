# cvDarts
Darts score perception using openCv

## Installation
First you need to make sure pip is installed. Check this with the following command:
```
pip --version
```
If no pip installation is discovered, follow the [installation instructions for pip](https://pip.pypa.io/en/stable/installing/)
If you installed pip using apt (as default in Ubuntu Linux), you should try to update pip using:
```
sudo -H pip3 install --upgrade pip
```

You can setup and run *cvdarts* using pipenv which installs you all dependencies in a virtualenv. [See pipenv project page](https://github.com/pypa/pipenv#pipenv-python-development-workflow-for-humans) Using pip you can install pipenv with the following command to install pipenv:
```
pip install --user pipenv
```
With pipenv installed you can run cvdarts with:
```
pipenv install
pipenv run python main.py 0
```

## Running the application
The application takes multiple arguments. First of all it takes the web cam ids as multiple arguments. The ids start 
with 0 and increment as you connect more web cams to your computer. If your computer has a integrated web cam, this is 
usually device `0`. Connect two more external web cams and those will have the ids `1` and `2`. 

To configure those external cams from the example above type:
```
pipenv run python main.py --config 1 2
```

Afterwards you can run the program with those 2 cameras:
```
pipenv run python main.py 1 2
```
