from setuptools import setup

setup(
    name='excel2sth',
    version='0.0.1',
    packages=['excel2sth'],
    url='https://cupen.github.com',
    license='WTFPL',
    author='cupen',
    install_requires = [
        'xlrd >= 0.9',
        'docopt >= 0.6.0'
        'pies == *'
    ],
    author_email='cupen@foxmail.com',
    description='Export excel to something(e.g. json sql lua).',
    # entry_points={
    #     'console_scripts': [
    #         'excel2mysql = excel2mysql:main',
    #         'excel2lua = excel2lua:main'
    #     ]
    # },
    scripts=['excel2json.py']
)
