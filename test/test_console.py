import os
import unittest
from io import StringIO
from unittest.mock import patch
from unittest.mock import MagicMock

import requests
from httmock import urlmatch, HTTMock

from apt_git import console

SEARCH_RESPONSE = os.path.join(os.path.dirname(__file__), 'fixtures/mocked_search_response.json')
INSTALL_RESPONSE = os.path.join(os.path.dirname(__file__), 'fixtures/mocked_install_response.json')


# define matcher:
@urlmatch(netloc=r'(.*\.)?github\.com$')
def github_fail_mock(url, request):
    response = requests.Response()
    response.status_code = 404
    return response


@urlmatch(netloc=r'(.*\.)?github\.com$')
def github_install_mock(url, request):
    return open(INSTALL_RESPONSE).read()


@urlmatch(netloc=r'(.*\.)?github\.com$')
def github_search_mock(url, request):
    return open(SEARCH_RESPONSE).read()


class TestConsole(unittest.TestCase):
    # should run nosetests with --nocapture
    @patch('sys.stdout', new_callable=StringIO)
    def test_should_search_for_repo(self, mock_stdout):
        expected = "java-design-patterns - Design patterns implemented in Java DesignPatternsPHP - sample code for several design patterns in PHP"
        with HTTMock(github_search_mock):
            console.main(['search', 'python'])
            output = " ".join(mock_stdout.getvalue().split())
            self.assertEqual(output, expected)

    @patch('subprocess.call', new_callable=MagicMock())
    def test_should_install_repo(self, mocked_subprocess):
        with HTTMock(github_install_mock):
            console.main(['install', 'alexrochas/apt-git'])
            mocked_subprocess.assert_called_with(['git', 'clone', 'https://github.com/alexrochas/apt-git.git'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_should_fail_install_when_repo_not_exist(self, mock_stdout):
        expected = 'Repository not found.\n'
        with HTTMock(github_fail_mock):
            console.main(['install', 'fakeowner/fakerepo'])
            self.assertEqual(mock_stdout.getvalue(), expected)
