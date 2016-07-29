import argparse
import requests


def parse_args():
    parser = argparse.ArgumentParser(
        description="apt-git is a command line interface for retrieval of projects and information about them from github")
    subparser = parser.add_subparsers(help="subparser help")
    search_parser = subparser.add_parser('search')
    search_parser.add_argument('pattern', help='pattern for search')
    args, unkown = parser.parse_known_args()
    return args


def main():
    # https://developer.github.com/v3/search/
    parser = parse_args()
    pattern = parser.pattern
    request = requests.get("https://api.github.com/search/repositories?q="+pattern+"+in:name&sort=stars&order=desc")
    if request.status_code == 200:
        for r in request.json()['items']:
            print(r['name'] + " - " + r['description'])


if __name__ == '__main__':
    main()