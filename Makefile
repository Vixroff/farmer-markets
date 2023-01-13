run:
	python3 -m controller.app

init:
	python3 -m model.mysql.db

upload:
	python3 -m ETL.main

lint:
	flake8 controller ETL model views