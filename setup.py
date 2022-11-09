from setuptools import setup


def get_version(fname='flake8_autospec/version.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('version'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.md',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-autospec',
    version=get_version(),
    description="autospec checker for flake8",
    long_description=get_long_description(),
    keywords=['flake8', 'mock', 'autospec', 'testing'],
    author='Matt Lewellyn',
    author_email='matt.lewellyn@autospec.io',
    url='https://github.com/Synthego/flake8-autospec.git',
    py_modules=['flake8_autospec'],
    packages=['flake8_autospec'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'M10 = flake8_autospec.mock_autospec:MockAutospecChecker',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    license='BSD',
    extras_require={
        'test': [
            'flake8',
            'pytest',
            'pytest-cov',
            'tox',
        ],
    }
)
