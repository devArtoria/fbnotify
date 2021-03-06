from setuptools import setup, find_packages

setup(
    name='fbnotify',
    version='0.0.2',
    description='A simple facebook messenger wrapper for noify',
    license='MIT',
    author='Lewis Kim',
    author_email='lewis_kim@outlook.com',
    url='https://github.com/devArtoria/fbnotify',
    keywords=['facebook', 'notify', 'fbchat'],
    install_requires=[
        'requests',
        'fbchat'
    ],
    packages=find_packages(exclude=['tests']),
    zip_safe=False
)