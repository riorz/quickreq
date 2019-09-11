# Quickreq
Scan a requirements file for repository urls in the form:  
`git+ssh://myproject.git@hashtags#egg=myproject`  
and update them to the latest commit in master branch.

## Usage
```bash
# check all requirements and update requirements file to their latest commit.
quickreq [-f  requirements.txt]
```
