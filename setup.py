from setuptools import setup

with open('README.rst', 'r') as f:
  readme = f.read()

def strip_requirement(line):
  if not line or line.startswith('-') or line.startswith('#'):
    return
  return line.strip()

with open('requirements.txt', 'r') as f:
  requirements = [strip_requirement(x) for x in f if strip_requirement(x)]

with open('requirements-dev.txt', 'r') as f:
  test_requirements = [strip_requirement(x) for x in f if strip_requirement(x)]

setup(
  name='handwriting',
  version='0.0.1',
  description='Handwriting.io API client.',
  long_description=readme,
  packages=['handwriting'],
  install_requires=requirements,
  setup_requires=['pytest-runner'],
  tests_require=test_requirements,
)
