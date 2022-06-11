def test_add(run):
    run('install')
    run('add pre-commit "isort ."')
    run('add pre-commit "black ."')
    run('add pre-commit "pytest"')
    run('add pre-commit "pylint --fail-under=8 ."')
