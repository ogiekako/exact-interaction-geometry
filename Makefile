.PHONY: verify

PYTHON ?= python3

VERIFIERS := \
	verification/verify_source_pair_augmentation.py \
	verification/verify_operational_codescent.py \
	verification/verify_no_choice.py \
	verification/verify_phase_v_vii_finite_core.py

verify:
	@set -e; \
	for f in $(VERIFIERS); do \
		echo "== $$f"; \
		$(PYTHON) $$f; \
		$(PYTHON) -O $$f; \
		$(PYTHON) -m py_compile $$f; \
	done
