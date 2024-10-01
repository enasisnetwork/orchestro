# Enasis Network Orchestrations

> :warning: This project has not released its first major version.

Project for executing the Ansible playbooks for system automation.

<a href="https://enasisnetwork.github.io/orchestro/validate/flake8.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/flake8.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/pylint.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/pylint.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/mypy.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/mypy.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/yamllint.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/yamllint.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/ansblint.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/ansblint.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/pytest.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/pytest.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/coverage.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/coverage.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/sphinx.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/sphinx.png"></a><br>

## Documentation
Read [project documentation](https://enasisnetwork.github.io/orchestro/sphinx)
built using the [Sphinx](https://www.sphinx-doc.org/) project.
Should you venture into the sections below you will be able to use the
`sphinx` recipe to build documention in the `sphinx/html` directory.

## Quick start for local development
Start by cloning the repository to your local machine.
```
git clone https://github.com/enasisnetwork/orchestro.git
```
Set up the Python virtual environments expected by the Makefile.
```
make -s venv-create
```

### Execute the linters and tests
The comprehensive approach is to use the `check` recipe. This will stop on
any failure that is encountered.
```
make -s check
```
However you can run the linters in a non-blocking mode.
```
make -s linters-pass
```
And finally run the various tests to validate the code and produce coverage
information found in the `htmlcov` folder in the root of the project.
```
make -s pytest
```

## Version management
> :warning: Ensure that no changes are pending.

1. Rebuild the environment.
   ```
   make -s check-revenv
   ```

1. Update the [version.txt](orchestro/version.txt) file.

1. Push to the `main` branch.

1. Create [repository](https://github.com/enasisnetwork/orchestro) release.
