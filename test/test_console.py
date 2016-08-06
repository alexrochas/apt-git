import os
import unittest
from io import StringIO
from unittest.mock import patch

from httmock import urlmatch, HTTMock

from apt_git import console

SEARCH_RESPONSE = os.path.join(os.path.dirname(__file__), 'fixtures/mocked_search_response.json')


# define matcher:
@urlmatch(netloc=r'(.*\.)?github\.com$')
def github_mock(url, request):
    return open(SEARCH_RESPONSE).read()


class TestConsole(unittest.TestCase):
    # should run nosetests with --nocapture
    @patch('sys.stdout', new_callable=StringIO)
    def test_should_search_for_repo(self, mock_stdout):
        expected = "java-design-patterns - Design patterns implemented in Java DesignPatternsPHP - sample code for several design patterns in PHP"
        with HTTMock(github_mock):
            console.main(['search', 'python'])
            output = " ".join(mock_stdout.getvalue().split())
            self.assertEqual(output, expected)
