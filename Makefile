.PHONY: verify

verify:
	python3 verification/verify_category_reconstruction.py
	python3 -O verification/verify_category_reconstruction.py
	python3 -m py_compile verification/verify_category_reconstruction.py
