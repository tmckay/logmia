test :
		docker build --tag logmia .
		docker run logmia /bin/bash -c "pytest -vv; mypy logmia; pylint logmia"
