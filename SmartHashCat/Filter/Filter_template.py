import CommandRunner
from Filter.FilterAbstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)

    def get_results(self):
        '''
        This function returns the result(s) of the execution.
        It is preferable to use yield instead of return to avoid heavy memory usage
        A filter should never write to a temporary of final file.
        The only filter allowed to do this is the FilterWriteToSmartFile
        '''
        raise NotImplementedError("Not yet implemented!")