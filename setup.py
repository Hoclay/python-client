from setuptools import setup

with open('requirements.txt', 'r') as f:
  requirements = [x.strip() for x in f if x.strip()]

setup(
  name='handwriting',
  version='0.0.1',
  description='Handwriting.io API client.',
  packages=['handwriting'],
  install_requires=requirements,
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
)
