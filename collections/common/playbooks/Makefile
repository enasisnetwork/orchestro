# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: common-overview
common-overview: \
	.check-stage .check-limit
	@## Dump information related to operation
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>common-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			enasisnetwork.common.overview; \
		deactivate)



.PHONY: common-validate
common-validate: \
	.check-stage .check-limit
	@## Login to the host and report reachable
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>common-validate<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			enasisnetwork.common.validate; \
		deactivate)



.PHONY: common-encrypt
common-encrypt: \
	.check-stage
	@## Encrypt information with Ansible Vault
	@#
ifndef vault
	$(error vault not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>common-encrypt<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible-vault \
			encrypt_string \
			--encrypt-vault-id $(vault); \
		deactivate)



.PHONY: common-decrypt
common-decrypt: \
	.check-stage
	@## Decrypt information with Ansible Vault
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>common-decrypt<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		ansible-vault decrypt; \
		deactivate)



.PHONY: common-inventory
common-inventory: \
	.check-stage
	@## Dump the Ansible inventory information
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>common-inventory<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible-inventory --graph \
		$(ansible_args); \
		deactivate)



.PHONY: common-custom
common-custom: \
	.check-stage .check-limit
	@## Run Ansible module with given arguments
	@#
ifndef ansible_module_name
	$(error ansible_module_name not defined)
endif
ifndef ansible_module_args
	$(error ansible_module_args not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>common-custom<c0>)
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
