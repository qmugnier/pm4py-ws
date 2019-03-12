from setuptools import setup

setup(
    name='pm4py-ws',
    version='',
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
    include_package_data=True,
    url='',
    license='',
    author='PADS',
    author_email='',
    description=''
)
