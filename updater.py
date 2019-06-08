import pathlib
from shutil import copyfile
import subprocess
import re
from collections import namedtuple
import fileinput

Repo = namedtuple('Repository', ['name', 'url', 'hash', 'remote_hash'])

def gen_url(repo):
    return f'git+{repo.url}@{repo.remote_hash}#egg={repo.name}'


def check_update(url, hash, name):
    """ check url for update """
    check_update = subprocess.run(
            ('git', 'ls-remote', url, 'master'),
             encoding='utf-8',
             stdout=subprocess.PIPE).stdout
    remote_hash = check_update.split()[0]
    if not remote_hash == hash:
        return Repo(name, url, hash, remote_hash)


def read_requirements(req_file):
    """ read requirement and check updates. """
    if not req_file.exists():
        print('Cannot find requirements.txt')
        return

    backup = f'{req_file.stem}.bak'
    copyfile(req_file, pathlib.Path(backup))
    with fileinput.input(files=[str(req_file)], inplace=True) as f:
        for line in f:
            r = re.findall('^git\+(ssh.+\.git)@(\w+)#egg=(\w+)', line)
            if r:
                repo = check_update(*r[0])
                if repo:
                    line = gen_url(repo) + '\n'
            print(line, end='')


def main():
    req_file = pathlib.Path('./requirements.txt')
    requirement = read_requirements(req_file)


if __name__ == '__main__':
    main()
