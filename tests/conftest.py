import pytest
import subprocess


@pytest.fixture
def run():
    return lambda *args: subprocess.run(["pushpin"] + [*args])
