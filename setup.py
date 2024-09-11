from setuptools import setup, find_packages

def parse_requirements(filename):
  with open(filename, 'r') as file:
    return [line.strip() for line in file if line and not line.startswith('#')]

setup(
  name='crypto_algorithms',
  version='0.1',
  description='A library for cryptographic algorithms',
  packages=find_packages(where='src'),
  package_dir={'': 'src'},
  install_requires=parse_requirements('requirements.txt'),
  test_suite='unittest'
)
