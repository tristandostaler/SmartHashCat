from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputName",)
        self.filters = [
            filters['FilterWriteToSmartFileTemp'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison']
        ]
    
    def run_child(self):
        '''
        This function run any logic that's needed to generate it's result.
        Many functions do nothing here because they return something static.
        An example of something done here is the input for cewl
        '''
        raise NotImplementedError("Not yet implemented!")
    
    def get_results(self):
        '''
        This function returns the result(s) of the execution.
        It is preferable to use yield instead of return to avoid heavy memory usage
        '''
        raise NotImplementedError("Not yet implemented!")
