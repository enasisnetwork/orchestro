# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: utility-overview
utility-overview:
	@## Dump relevant information about hosts
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
ifndef vault
	$(error vault variable is not defined)
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
		ansible-vault \
			decrypt; \
		deactivate)
