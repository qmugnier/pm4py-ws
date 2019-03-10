from pm4py.objects.log.importer.xes import factory as xes_importer

class XesHandler(object):
    def __init__(self):
        self.log = None
        self.first_ancestor = None
        self.last_ancestor = None

    def build_from_path(self, path, parameters=None):
        if parameters is None:
            parameters = {}
        self.log = xes_importer.apply(path)