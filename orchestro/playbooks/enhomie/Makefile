# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: enhomie-overview
enhomie-overview: \
	.check-limit .check-stage
	@## Dump relevant information about hosts
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=overview \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-install
enhomie-install: \
	.check-limit .check-stage
	@## Install and configure related package
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-install<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=install \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-reinstall
enhomie-reinstall: \
	.check-limit .check-stage
	@## Remove existing venv and then install
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-reinstall<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		orche_ensured="yes" \
		orche_confirm="yes" \
		ansible_gather="yes" \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=reinstall \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-configure
enhomie-configure: \
	.check-limit .check-stage
	@## Bypass install and configure package
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-configure<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=configure \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-state
enhomie-state: \
	.check-limit .check-stage
	@## Control the state of package service
	@#
ifndef state
	$(error state not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-state<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="state-$(state)" \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)
