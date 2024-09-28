from setuptools import setup, find_packages

setup(
    name='horizon_plugin',
    version='0.1',
    description='Ein Beispiel-Plugin für OpenStack Horizon',
    author='Dein Name',
    author_email='deine.email@example.com',
    packages=find_packages(),
    install_requires=['horizon'],
    entry_points={
        'horizon.dashboard': [
            'horizon_plugin = horizon_plugin.panel:HelloWorld',
        ],
    },
)
