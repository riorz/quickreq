# quickreq
Find out all requirements in the form: git+ssh://myproject.git@hashtags#egg=myproject
and update them to the latest commit in master branch.
## Usage
```bash
# check all requirements and update them to latest commit in requirements.txt.
python3 quickreq.py
# use -f, --file to assign file.
python3 quickreq.py [-f  requirements.txt]
```
