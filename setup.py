from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in local/__init__.py
from local import __version__ as version

setup(
	name="local",
	version=version,
	description="local",
	author="local",
	author_email="local@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
