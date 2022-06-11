def test_add(run):
    run("install")
    run('add .pushpin/pre-commit "isort ."')
    run('add .pushpin/pre-commit "black ."')
    run('add .pushpin/pre-commit "pytest"')
    run('add .pushpin/pre-commit "pylint --fail-under=8 ."')
