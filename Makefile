.PHONY: build test demo

build:
	docker build --tag logmia .

test: | build
	docker run logmia /bin/bash -c "pytest -vv; mypy logmia; pylint logmia"

demo: | build
	docker run logmia /bin/bash -c "python -m logmia"

