db:
	python3 -m ETL.load

run:
	python3 -m controller.console.controller

init:
	python3 -m model.mysql.db

upload:
	python3 -m ETL.main

