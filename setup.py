from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-mock',
    'pytest-click',
    'pytest-pylint',
]

setup(
    name='Lektor',
    version='3.1.1',
    url='http://github.com/lektor/lektor/',
    description='A static content management system.',
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Jinja2>=2.4',
        'click>=6.0',
        'watchdog',
        'mistune>=0.7.0',
        'Flask',
        'EXIFRead',
        'inifile',
        'Babel',
        'setuptools',
        'pip',
        'requests[security]',
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'ipython': ['ipython'],
    },
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points='''
        [console_scripts]
        lektor=lektor.cli:main
    '''
)
