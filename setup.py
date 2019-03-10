from setuptools import setup

setup(
    name='pm4py-ws',
    version='',
    packages=['webapp.node_modules.node-gyp.gyp.pylib.gyp', 'webapp.node_modules.node-gyp.gyp.pylib.gyp.generator',
              'pm4pyws', 'pm4pyws.handlers', 'pm4pyws.handlers.xes', 'pm4pyws.handlers.parquet',
              'pm4pyws.handlers.parquet.sna', 'pm4pyws.handlers.parquet.cases', 'pm4pyws.handlers.parquet.statistics',
              'pm4pyws.handlers.parquet.process_schema', 'pm4pyws.handlers.parquet.process_schema.tree',
              'pm4pyws.handlers.parquet.process_schema.dfg_freq', 'pm4pyws.handlers.parquet.process_schema.dfg_perf',
              'pm4pyws.handlers.parquet.process_schema.alpha_freq',
              'pm4pyws.handlers.parquet.process_schema.inductive_freq',
              'pm4pyws.handlers.parquet.process_schema.inductive_perf',
              'pm4pyws.handlers.parquet.process_schema.alpha_performance'],
    package_data={
        'webapp': ['*']
    },
    url='',
    license='',
    author='PADS',
    author_email='',
    description=''
)
