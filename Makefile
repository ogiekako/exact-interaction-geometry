.PHONY: verify paper clean-paper

PYTHON ?= python3
PDFLATEX ?= pdflatex

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

paper:
	@set -e; \
	cd papers/source-pair-augmentation; \
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error paper.tex; \
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error paper.tex; \
	echo "built papers/source-pair-augmentation/paper.pdf"

clean-paper:
	rm -f papers/source-pair-augmentation/paper.aux \
	      papers/source-pair-augmentation/paper.log \
	      papers/source-pair-augmentation/paper.out \
	      papers/source-pair-augmentation/paper.pdf
