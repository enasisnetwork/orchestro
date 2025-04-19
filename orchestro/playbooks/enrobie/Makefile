# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: enrobie-overview
enrobie-overview:
	@## Dump relevant information about hosts
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enrobie-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=overview \
			orchestro/playbooks/enrobie/default.yml; \
		deactivate)



.PHONY: enrobie-install
enrobie-install:
	@## Install and configure related package
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enrobie-install<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=install \
			orchestro/playbooks/enrobie/default.yml; \
		deactivate)



.PHONY: enrobie-reinstall
enrobie-reinstall:
	@## Remove existing venv and then install
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enrobie-reinstall<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		orche_ensured="yes" \
		orche_confirm="yes" \
		ansible_gather="yes" \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=reinstall \
			orchestro/playbooks/enrobie/default.yml; \
		deactivate)



.PHONY: enrobie-configure
enrobie-configure:
	@## Bypass install and configure package
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enrobie-configure<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=configure \
			orchestro/playbooks/enrobie/default.yml; \
		deactivate)



.PHONY: enrobie-state
enrobie-state:
	@## Control the state of package service
	@#
ifndef limit
	$(error limit not defined)
endif
ifndef state
	$(error state not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enrobie-state<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="state-$(state)" \
			orchestro/playbooks/enrobie/default.yml; \
		deactivate)
