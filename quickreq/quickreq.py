import subprocess
import re
from collections import namedtuple
import fileinput

Repo = namedtuple('Repository', ['name', 'url', 'commit', 'remote_commit'])

def gen_url(repo):
    return f'git+{repo.url}@{repo.remote_commit}#egg={repo.name}'


def check_update(url, commit, name):
    """ check url for update """
    check_update = subprocess.run(
            ('git', 'ls-remote', url, 'master'),
             encoding='utf-8',
             stdout=subprocess.PIPE).stdout
    remote_commit = check_update.split()[0]
    if not remote_commit == commit:
        return Repo(name, url, commit, remote_commit)


def update_repo(req_file):
    """ read requirement and check updates. """
    if not req_file.exists():
        print('Cannot find requirements.txt')
        return

    with fileinput.input(files=[str(req_file)], inplace=True, backup='.bak') as f:
        for line in f:
            r = re.findall('^git\+(ssh.+\.git)@(\w+)#egg=(\w+)', line)
            if r:
                repo = check_update(*r[0])
                if repo:
                    line = gen_url(repo) + '\n'
            print(line, end='')
