import setuptools

from setuptools import setup, find_packages

setup(
        name = 'jfantom',
        version = '0.0.1',
        packages = find_packages(),
        install_requires = [
            'flask>=0.11, <0.12',
            'gunicorn==19.7.1',
            'eventlet==0.21.0',
            'PyMySQL==0.8.0',
            'SQLAlchemy==1.1.15',
            'MySQL-python==1.2.5',
            ],
        tests_require = [
            'pytest==3.2.3',
            'pytest-mock==1.6.3',
            'pytest-flask==0.10.0',
            'pytest-cov==2.5.1',
            'pytest-xdist==1.20.1',
            ],
        setup_requires = [ 'pytest-runner==2.12.1' ],
    )
