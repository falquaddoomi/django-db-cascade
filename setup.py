from setuptools import setup, find_packages

setup(
    name='django-db-cascade-3',
    version='0.3.0',
    description='Fork of django-db-cascade for Django 3.0.  Optionally use postgres db ON CASCADE DELETE on django foreign keys',
    url='http://github.com/jkapelner/django-db-cascade',
    author='Nick Stefan, Jordan Kapelner, Faisal Alquaddoomi',
    author_email='nickstefan12@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django >= 3.0'
    ],
    classifiers=[
        'Framework :: Django',
        'Topic :: Database',
    ],
    zip_safe=False
)
