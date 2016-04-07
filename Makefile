.PHONY: test
test:
	python setup.py test

.PHONY: clean
clean:
	rm -rvf ./*.egg ./*.eggs ./*.egg-info .cache .eggs .tox
	rm -rvf test/*.pyc test/__pycache__ handwritingio/*.pyc
