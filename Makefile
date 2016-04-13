IMAGE_NAME = handwritingio-python-client
API_URL = http://$(shell docker-machine ip $(DOCKER_MACHINE_NAME)):3000
API_KEY = dev
API_SECRET = dev
RUN_ENV = -e API_URL=$(API_URL) -e API_KEY=$(API_KEY) -e API_SECRET=$(API_SECRET)

.PHONY: test
test: image
	docker run --rm $(RUN_ENV) $(IMAGE_NAME) tox

.PHONY: image
image:
	docker build -t $(IMAGE_NAME) .

.PHONY: clean
clean:
	rm -rvf ./*.egg ./*.eggs ./*.egg-info .cache .eggs .tox dist
	rm -rvf test/*.pyc test/__pycache__ handwritingio/*.pyc
