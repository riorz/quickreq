from quickreq import quickreq
import argparse
import pathlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-f', '--file',
            help='File to update.',
            default='./requirements.txt')
    args = parser.parse_args()
    req_file = pathlib.Path(args.file)
    quickreq.update_repo(req_file)
