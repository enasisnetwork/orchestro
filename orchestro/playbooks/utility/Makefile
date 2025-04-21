# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: utility-overview
utility-overview: \
	.check-limit .check-stage
	@## Dump relevant information about hosts
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			--tags=overview \
			orchestro/playbooks/utility/default.yml; \
		deactivate)



.PHONY: utility-ping
utility-ping: \
	.check-limit .check-stage
	@## Dump relevant information about hosts
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-ping<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			--tags=ping \
			orchestro/playbooks/utility/default.yml; \
		deactivate)



.PHONY: utility-encrypt
utility-encrypt: \
	.check-stage
	@## Encrypt information with Ansible Vault
	@#
ifndef vault
	$(error vault not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-encrypt<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible-vault \
			encrypt_string \
			--encrypt-vault-id $(vault); \
		deactivate)



.PHONY: utility-decrypt
utility-decrypt: \
	.check-stage
	@## Encrypt information with Ansible Vault
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-decrypt<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible-vault decrypt; \
		deactivate)



.PHONY: utility-inventory
utility-inventory: \
	.check-stage
	@## Dump the Ansible inventory information
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-inventory<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-inventory --graph \
		$(ansible_args); \
		deactivate)



.PHONY: utility-custom
utility-custom: \
	.check-limit .check-stage
	@## Dump relevant information about hosts
	@#
ifndef ansible_module_name
	$(error ansible_module_name not defined)
endif
ifndef ansible_module_args
	$(error ansible_module_args not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-custom<c0>)
	@#
	@printf '    \033[91mansible_module_name:\033[0m %s'
	echo $(ansible_module_name)
	@printf '    \033[91mansible_module_args:\033[0m %s'
	echo $(ansible_module_args)
	@#
	@sleep 2
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ANSIBLE_CONFIG=ansible.cfg \
		ansible \
			"!localhost,$(limit)" $(ansible_args) \
			-m "$(ansible_module_name)" \
			-a "$(ansible_module_args)"; \
		deactivate)
