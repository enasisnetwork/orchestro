# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: utility-overview
utility-overview:
	@## Dump relevant information about hosts
	@#
ifndef limit
	$(error limit not defined)
endif
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-overview<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			--tags=overview \
			orchestro/playbooks/utility/default.yml; \
		deactivate)



.PHONY: utility-encrypt
utility-encrypt:
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
		. $(VENVP)/bin/activate; \
		ansible-vault \
			encrypt_string \
			--encrypt-vault-id $(vault); \
		deactivate)



.PHONY: utility-decrypt
utility-decrypt:
	@## Encrypt information with Ansible Vault
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-decrypt<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible-vault decrypt; \
		deactivate)



.PHONY: utility-inventory
utility-inventory:
	@## Dump the Ansible inventory information
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-inventory<c0>)
	@#
	@( \
		set -e; \
		. $(VENVP)/bin/activate; \
		ansible-inventory --graph; \
		deactivate)



.PHONY: utility-custom
utility-custom:
	@## Dump relevant information about hosts
	@#
ifndef limit
	$(error limit not defined)
endif
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
		. $(VENVP)/bin/activate; \
		ANSIBLE_CONFIG=ansible.cfg \
		ansible \
			"$(limit)" $(ansible_args) \
			-m "$(ansible_module_name)" \
			-a "$(ansible_module_args)"; \
		deactivate)
