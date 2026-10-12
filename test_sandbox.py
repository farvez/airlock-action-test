"""Checks that these tests really ran inside an Airlock sandbox with only PyPI reachable."""
import os
import socket
import urllib.error
import urllib.request

import pytest


def test_runs_in_the_sandbox():
    assert os.getcwd() == "/workspace/repo"


def test_pypi_is_reachable():
    with urllib.request.urlopen("https://pypi.org/simple/pytest/", timeout=15) as response:
        assert response.status == 200


def test_other_sites_are_blocked():
    with pytest.raises(urllib.error.URLError):
        urllib.request.urlopen("https://example.com/", timeout=15)


def test_no_direct_route_out():
    with pytest.raises(OSError):
        socket.create_connection(("1.1.1.1", 443), timeout=5)
