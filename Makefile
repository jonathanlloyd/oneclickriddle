# Makefile for ocr_server
all: run

rebuild_venv:
	rm -rf venv
	make venv

venv:
	test -d venv || virtualenv venv
	venv/bin/pip3 install -Ur requirements.txt
	venv/bin/pip3 install -Ur dev_requirements.txt

run: venv
	@echo "Running ocr_server..."
	@./scripts/run

check: test

test: venv
	@venv/bin/python3 -m nose -s

lint: venv
	@venv/bin/python3 -m pylint ./ocr_server/*.py
