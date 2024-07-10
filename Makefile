publish:
	poetry run python python_gcp_pub_sub_interactor/publisher.py

subscribe:
	poetry run python python_gcp_pub_sub_interactor/subscriber.py

black:
	poetry run black python_gcp_pub_sub_interactor/

mypy:
	poetry run mypy python_gcp_pub_sub_interactor/

pylint:
	poetry run pylint python_gcp_pub_sub_interactor/

test:
	poetry run pytest -vvs tests/

checks: black mypy pylint test
