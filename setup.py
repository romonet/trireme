from setuptools import setup, find_packages  # Always prefer setuptools over distutils

setup(
    name='trireme',
    version='1.1.0',

    description='Migration tool providing support for Apache Cassandra, DataStax Enterprise Cassandra, & DataStax '
                'Enterprise Solr.',

    url='https://github.com/o19s/trireme',
    download_url='https://github.com/o19s/trireme/tarball/1.1.0',

    author='Christopher Bradford',
    author_email='cbradford@opensourceconnections.com',

    license='BSD',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],

    keywords='cassandra solr dse dsc migrations development',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['lz4', 'blist', 'cassandra-driver', 'requests', 'invoke']
)
