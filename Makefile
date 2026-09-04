.PHONY: check

check:
	python3 checks/check_two_state_maxplus.py
	python3 -O checks/check_two_state_maxplus.py
	python3 -m py_compile checks/check_two_state_maxplus.py
