import argparse
import requests
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(
        description="apt-git is a command line interface for retrieval of projects and information about them from github")
    subparser = parser.add_subparsers(dest="command", help="commands")
    search_parser = subparser.add_parser('search')
    search_parser.add_argument('pattern', help='pattern for search')
    clone_parser = subparser.add_parser('install')
    clone_parser.add_argument('repo', help='repo to clone in format ":owner/:repo_name"')
    args, unkown = parser.parse_known_args()
    return args


def main():
    # https://developer.github.com/v3/search/
    parser = parse_args()
    command = parser.command
    commands[command](parser)


def install(parser):
    repository = parser.repo
    request = requests.get("https://api.github.com/repos/" + repository)
    if request.status_code == 200:
        clone_url = request.json()['clone_url']
        subprocess.call(["git", "clone", clone_url])
    elif request.status_code == 404:
        print("Repository not found.")
    else:
        print("An error occuried while trying access remote GitHub API, please try again.")


def search(pattern):
    request = requests.get("https://api.github.com/search/repositories?q=" + pattern + "+in:name&sort=stars&order=desc")
    if request.status_code == 200:
        for r in request.json()['items']:
            print(r['name'] + " - " + r['description'])
    else:
        print("An error occuried while trying access remote GitHub API, please try again.")

commands = {
    'search': search,
    'install': install
}

if __name__ == '__main__':
    main()
