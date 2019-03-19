from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.objects.log.util import insert_classifier
from pm4py.objects.log.util import xes
from pm4py.statistics.traces.log import case_statistics
from pm4py.util import constants

from pm4pyws.handlers.xes.cases import variants
from pm4pyws.handlers.xes.ctmc import transient
from pm4pyws.handlers.xes.process_schema import factory as process_schema_factory
from pm4pyws.handlers.xes.sna import get_sna as sna_obtainer
from pm4pyws.handlers.xes.statistics import events_per_time, case_duration
from pm4pyws.util import casestats
from pm4py.algo.filtering.log.variants import variants_filter


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
        # variants
        self.variants = None
        # number of variants
        self.variants_number = 0
        # number of cases
        self.cases_number = 0
        # number of events
        self.events_number = 0

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
        try:
            # try faster non standard importer
            self.log = xes_importer.apply(path, variant="nonstandard")
            if len(self.log) == 0:
                # non standard imported failed
                self.log = xes_importer.apply(path)
        except:
            # revert to classic importer
            self.log = xes_importer.apply(path)
        self.log, classifier_key = insert_classifier.search_act_class_attr(self.log,
                                                                           force_activity_transition_insertion=True)

        self.activity_key = xes.DEFAULT_NAME_KEY
        if classifier_key is not None:
            self.activity_key = classifier_key
        self.build_variants()
        self.calculate_variants_number()
        self.calculate_cases_number()
        self.calculate_events_number()
        self.first_ancestor = self
        self.last_ancestor = self

    def build_variants(self, parameters=None):
        """
        Build the variants of the event log

        Parameters
        ------------
        parameters
            Possible parameters of the method
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        self.variants = variants_filter.get_variants(self.log, parameters=parameters)

    def calculate_variants_number(self):
        """
        Calculate the number of variants in this log
        """
        self.variants_number = len(self.variants.keys())

    def calculate_cases_number(self):
        """
        Calculate the number of cases in this log
        """
        self.cases_number = len(self.log)

    def calculate_events_number(self):
        """
        Calculate the number of events in this log
        """
        self.events_number = sum([len(case) for case in self.log])

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
        parameters["variants"] = self.variants
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

    def get_transient(self, delay, parameters=None):
        """
        Perform CTMC simulation on a log

        Parameters
        -------------
        delay
            Delay
        parameters
            Possible parameters of the algorithm

        Returns
        -------------
        graph
            Case duration graph
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return transient.apply(self.log, delay, parameters=parameters)

    def get_case_statistics(self, parameters=None):
        """
        Gets the statistics on cases

        Parameters
        -------------
        parameters
            Possible parameters of the algorithm

        Returns
        -------------
        list_cases
            List of cases
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        parameters["max_ret_cases"] = 500
        parameters["sort_by_index"] = parameters["sort_by_index"] if "sort_by_index" in parameters else 0
        parameters["sort_ascending"] = parameters["sort_ascending"] if "sort_ascending" in parameters else False
        if "variant" in parameters:
            filtered_log = variants_filter.apply(self.log, [parameters["variant"]], parameters=parameters)
            return casestats.include_key_in_value_list(
                case_statistics.get_cases_description(filtered_log, parameters=parameters))
        else:
            return casestats.include_key_in_value_list(
                case_statistics.get_cases_description(self.log, parameters=parameters))

    def get_events(self, caseid, parameters=None):
        """
        Gets the events of a case

        Parameters
        -------------
        caseid
            Case ID
        parameters
            Parameters of the algorithm

        Returns
        ------------
        list_events
            Events belonging to the case
        """
        if parameters is None:
            parameters = {}
        parameters[constants.PARAMETER_CONSTANT_ACTIVITY_KEY] = self.activity_key
        parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = self.activity_key
        return case_statistics.get_events(self.log, caseid, parameters=parameters)
