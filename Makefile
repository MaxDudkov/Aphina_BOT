default: env

.PHONY: env
env:
	python3 -m venv .env && .env/bin/pip3 install -r requirements.txt