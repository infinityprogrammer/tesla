from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tesla/__init__.py
from tesla import __version__ as version

setup(
	name="tesla",
	version=version,
	description="Tesla Modification",
	author="RAFI",
	author_email="rafigrandhyper@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
