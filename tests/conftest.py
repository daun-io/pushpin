import subprocess

import pytest


@pytest.fixture
def run():
    return lambda *args: subprocess.run(["pushpin"] + [*args])
