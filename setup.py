from os.path import dirname, join

from setuptools import setup

import pm4pyws


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(
    name=pm4pyws.__name__,
    version=pm4pyws.__version__,
    description=pm4pyws.__doc__.strip(),
    long_description=read_file('README.md'),
    author=pm4pyws.__author__,
    author_email=pm4pyws.__author_email__,
    py_modules=[pm4pyws.__name__],
    include_package_data=True,
    packages=['pm4pyws', 'pm4pyws.util', 'pm4pyws.handlers', 'pm4pyws.handlers.xes', 'pm4pyws.handlers.xes.sna',
              'pm4pyws.handlers.xes.cases', 'pm4pyws.handlers.xes.statistics', 'pm4pyws.handlers.xes.process_schema',
              'pm4pyws.handlers.xes.process_schema.tree', 'pm4pyws.handlers.xes.process_schema.dfg_freq',
              'pm4pyws.handlers.xes.process_schema.dfg_perf', 'pm4pyws.handlers.xes.process_schema.alpha_freq',
              'pm4pyws.handlers.xes.process_schema.inductive_freq',
              'pm4pyws.handlers.xes.process_schema.inductive_perf',
              'pm4pyws.handlers.xes.process_schema.alpha_performance', 'pm4pyws.handlers.parquet',
              'pm4pyws.handlers.parquet.sna', 'pm4pyws.handlers.parquet.cases', 'pm4pyws.handlers.parquet.statistics',
              'pm4pyws.handlers.parquet.process_schema', 'pm4pyws.handlers.parquet.process_schema.tree',
              'pm4pyws.handlers.parquet.process_schema.dfg_freq', 'pm4pyws.handlers.parquet.process_schema.dfg_perf',
              'pm4pyws.handlers.parquet.process_schema.alpha_freq',
              'pm4pyws.handlers.parquet.process_schema.inductive_freq',
              'pm4pyws.handlers.parquet.process_schema.inductive_perf',
              'pm4pyws.handlers.parquet.process_schema.alpha_performance'],
    url='http://www.pm4py.org',
    license='GPL 3.0',
    install_requires=[
        'pm4py',
        'Flask',
        'flask-cors',
        'requests'
    ],
    project_urls={
        'Documentation': 'http://pm4py.pads.rwth-aachen.de/documentation/',
        'Source': 'https://github.com/pm4py/pm4py-source',
        'Tracker': 'https://github.com/pm4py/pm4py-source/issues',
    }
)
