from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thinerp/__init__.py
from thinerp import __version__ as version

setup(
	name="thinerp",
	version=version,
	description="Thinpc Technology Custom App",
	author="Ravi Modi",
	author_email="ravimodi@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
