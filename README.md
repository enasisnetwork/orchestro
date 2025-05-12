# Enasis Network Orchestrations

> :warning: This project has not released its first major version.

Project for executing the Ansible playbooks for system automation.

<a href="https://enasisnetwork.github.io/orchestro/validate/flake8.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/flake8.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/pylint.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/pylint.png"></a><br>
<a href="https://enasisnetwork.github.io/orchestro/validate/ruff.txt"><img src="https://enasisnetwork.github.io/orchestro/badges/ruff.png"></a><br>
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

## Running the Ansible playbooks
Currently this project assumes it is within the directory structure
of [workspace](https://github.com/enasisnetwork/workspace). This will
change sometime in the near future- though it can be overridden now.
- Specify `PYTHON` environment variable when calling `make`.
- Install various collections into the `collections` directory.
  - Replace the symbolic links or remove and place collections.
  - This is where the `Makefile` and `makefile.py` will look.

## Additional Ansible collections
- Utility Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-utility),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/utility)
- Projects Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-projects),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/projects)
- Certificates Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-certauth),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/certauth)
- Provision Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-provision),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/provision)
- Infrastructure Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-domain),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/domain)
- Applications Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-appstack),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/appstack)
- Internal Collection<br>
  [GitHub](https://github.com/enasisnetwork/ansible-internal),
  [Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/internal)


## Version management
> :warning: Ensure that no changes are pending.

1. Rebuild the environment.
   ```
   make -s check-revenv
   ```

1. Update the [version.txt](orchestro/version.txt) file.

1. Push to the `main` branch.

1. Create [repository](https://github.com/enasisnetwork/orchestro) release.
