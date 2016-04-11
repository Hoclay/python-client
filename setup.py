from setuptools import setup
from setuptools.command.test import test as TestCommand

with open('README.rst', 'r') as f:
  readme = f.read()

def strip_requirement(line):
  # skip blank lines or comments
  if not line or line.startswith('#'):
    return
  return line.strip()

with open('requirements.txt', 'r') as f:
  requirements = [strip_requirement(x) for x in f if strip_requirement(x)]

with open('requirements-dev.txt', 'r') as f:
  test_requirements = [strip_requirement(x) for x in f if strip_requirement(x)]


class Tox(TestCommand):
  user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

  def initialize_options(self):
    TestCommand.initialize_options(self)
    self.tox_args = None

  def finalize_options(self):
    TestCommand.finalize_options(self)
    self.test_args = []
    self.test_suite = True

  def run_tests(self):
    # import here, cause outside the eggs aren't loaded
    import tox
    import shlex
    args = self.tox_args
    if args:
        args = shlex.split(self.tox_args)
    errno = tox.cmdline(args=args)
    sys.exit(errno)


setup(
  name='handwritingio',
  version='0.0.1',
  description='Handwriting.io API client.',
  long_description=readme,
  author='Handwriting.io',
  author_email='support@handwriting.io',
  url='https://github.com/handwritingio/python-client',
  packages=['handwritingio'],
  install_requires=requirements,
  tests_require=['tox'],
  cmdclass = {'test': Tox},
)
