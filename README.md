# cafepy(Python3 scripts)
These scripts are for analyzing CafeMol outputs.

## Requirements
- python3 >= 3.5.1

* Install virtualenv. (RECOMMEND:for protecting your Home environment.)
```bash
python3 -m pip install -U pip setuptools
python3 -m pip install virtualenv
# or
pip3 install virtualenv
```
* activate virtualenv
```bash
virtualenv -p python3 venv
source venv/bin/activate
# Removing virtual environment
# (venv) deactivate 
```

## Set Up
```bash
python3 -m pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```
## build & install
```
cd cafepy
python3 setup.py build
python3 setup.py install
```

## Example:
```bash
python3 -m cafepy com -f filename.dcd -o output.file

```