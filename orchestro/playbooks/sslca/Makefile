# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: sslca-overview
sslca-overview: \
	.check-limit .check-stage
	@## Dump relevant information about hosts
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>sslca-overview<c0>)
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
			orchestro/playbooks/sslca/default.yml; \
		deactivate)



.PHONY: sslca-authority-build
sslca-authority-build: \
	.check-limit .check-stage
	@## Build the bootable installation image
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>sslca-authority-build<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=authority-build \
			orchestro/playbooks/sslca/default.yml; \
		deactivate)



.PHONY: sslca-certificate-build
sslca-certificate-build: \
	.check-limit .check-stage
	@## Build the bootable installation image
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>sslca-certificate-build<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] && set -a && . ./orchestro.env && set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=$(ORCHE_ROOT) \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=certificate-build \
			orchestro/playbooks/sslca/default.yml; \
		deactivate)
