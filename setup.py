from setuptools import setup


def readme():
	with open('README.md') as f:
		info = f.read()
	return info



setup(
	name='speedo',
	version='1.0.0',
	description='analyse and illustrate data and equation',
	long_description=readme(),
	long_description_content_type='text/markdown',
	url=''
)