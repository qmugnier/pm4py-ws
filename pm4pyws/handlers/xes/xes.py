from pm4py.objects.log.importer.xes import factory as xes_importer

from pm4pyws.handlers.xes.sna import get_sna as sna_obtainer
from pm4pyws.handlers.xes.cases import variants
from pm4pyws.handlers.xes.process_schema import factory as process_schema_factory
from pm4pyws.handlers.xes.statistics import events_per_time, case_duration
from pm4py.objects.log.util import insert_classifier
from pm4py.util import constants
from pm4py.objects.log.util import xes

class XesHandler(object):
    def __init__(self):
        """
        Constructor (set all variables to None)
        """

        # sets the current log to None
        self.log = None
        # sets the first ancestor (in the filtering chain) to None
        self.first_ancestor = None
        # sets the last ancestor (in the filtering chain) to None
        self.last_ancestor = None
        # classifier
        self.activity_key = None

    def build_from_path(self, path, parameters=None):
        """
        Builds the handler from the specified path to XES file

        Parameters
        -------------
        path
            Path to the log file
        parameters
            Parameters of the algorithm
        """
        if parameters is None:
            parameters = {}
        self.log = xes_importer.apply(path)
        self.log, classifier_key = insert_classifier.search_act_class_attr(self.log)

        self.activity_key = xes.DEFAULT_NAME_KEY
        if classifier_key is not None:
            self.activity_key = classifier_key

    def get_schema(self, variant=process_schema_factory.DFG_FREQ, parameters=None):
        """
        Gets the process schema in the specified variant and with the specified parameters

        Parameters
        -------------
        variant
            Variant of the algorithm
        parameters
            Parameters of the algorithm

        Returns
        ------------
        schema
            Process schema (in base64)
        model
            Model file possibly describing the process schema
        format
            Format of the process schema (e.g. PNML)
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return process_schema_factory.apply(self.log, variant=variant, parameters=parameters)

    def get_case_duration_svg(self, parameters=None):
        """
        Gets the SVG of the case duration

        Parameters
        ------------
        parameters
            Parameters of the algorithm

        Returns
        -----------
        graph
            Case duration graph (expressed in Base 64)
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return case_duration.get_case_duration_svg(self.log, parameters=parameters)

    def get_events_per_time_svg(self, parameters=None):
        """
        Gets the SVG of the events per time

        Parameters
        -------------
        parameters
            Parameters of the algorithm

        Returns
        -------------
        graph
            Events per time graph (expressed in Base 64)
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return events_per_time.get_events_per_time_svg(self.log, parameters=parameters)

    def get_variant_statistics(self, parameters=None):
        """
        Gets the variants of the given log

        Parameters
        --------------
        parameters
            Parameters of the algorithm

        Returns
        --------------
        variants
            Variants of the log
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return variants.get_statistics(self.log, parameters=parameters)

    def get_sna(self, variant="handover", parameters=None):
        """
        Gets a Social Network representation from a given log

        Parameters
        -------------
        variant
            Variant of the algorithm (metric to use)
        parameters
            Parameters of the algorithm (e.g. arc threshold)

        Returns
        ------------
        sna
            SNA representation
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return sna_obtainer.apply(self.log, variant=variant, parameters=parameters)
