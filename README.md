# Enasis Network Orchestrations

> :warning: This project has not released its first major version.

Project for executing the Ansible playbooks for system automation.

[![](https://img.shields.io/github/actions/workflow/status/enasisnetwork/orchestro/build.yml?style=flat-square&label=GitHub%20actions)](https://github.com/enasisnetwork/orchestro/actions)<br>
[![codecov](https://img.shields.io/codecov/c/github/enasisnetwork/orchestro?token=7PGOXKJU0E&style=flat-square&logoColor=FFFFFF&label=Coverage)](https://codecov.io/gh/enasisnetwork/orchestro)<br>
[![](https://img.shields.io/readthedocs/orchestro?style=flat-square&label=Read%20the%20Docs)](https://orchestro.readthedocs.io)<br>

## Documentation
Documentation is on [Read the Docs](https://orchestro.readthedocs.io).
Should you venture into the sections below you will be able to use the
`sphinx` recipe to build documention in the `docs/html` directory.

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

1. Update [Read the Docs](https://orchestro.readthedocs.io) documentation.
