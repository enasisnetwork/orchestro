# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: enhomie-overview
enhomie-overview:
	@## Dump relevant information about hosts
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-overview<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=overview \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-install
enhomie-install:
	@## Install and configure related package
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-install<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=install \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-reinstall
enhomie-reinstall:
	@## Remove existing venv and then install
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-reinstall<c0>)
	@#
	@$(VENVP)/bin/python -Bc 'if 1:\
		confirm = input(\
			"Are you sure? [y/N] ");\
		assert confirm == "y";'
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=reinstall \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-configure
enhomie-configure:
	@## Bypass install and configure package
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>enhomie-configure<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=configure \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)



.PHONY: enhomie-state
enhomie-state:
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
		<cD>make <cL>enhomie-state<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible_gather="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="state-$(state)" \
			orchestro/playbooks/enhomie/default.yml; \
		deactivate)
