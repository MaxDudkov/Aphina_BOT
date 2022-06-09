default: env

.PHONY: env
env:
	python3 -m venv .env && .env/bin/pip3 install -r requirements.txt

deploy:
	ssh max@takserver.ru "rm -rf ~/bot1; mkdir bot1"
	scp *.py max@takserver.ru:~/bot1/
	scp config.yml max@takserver.ru:~/bot1/
	scp -r img max@takserver.ru:~/bot1/
	scp -r courses max@takserver.ru:~/bot1/
