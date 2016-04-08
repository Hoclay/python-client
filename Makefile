IMAGE_NAME = handwriting-python
API_URL = http://$(shell docker-machine ip $(DOCKER_MACHINE_NAME)):3000

.PHONY: test
test: image
	docker run --rm -e API_URL=$(API_URL) $(IMAGE_NAME) python setup.py test

.PHONY: image
image:
	docker build -t $(IMAGE_NAME) .

.PHONY: clean
clean:
	rm -rvf ./*.egg ./*.eggs ./*.egg-info .cache .eggs .tox
	rm -rvf test/*.pyc test/__pycache__ handwritingio/*.pyc
