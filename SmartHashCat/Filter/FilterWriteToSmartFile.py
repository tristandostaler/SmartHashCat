import CommandRunner
from Filter.FilterAbstract import FilterAbstract
import Misc


class Filter(FilterAbstract):

    '''Note: this is the only filter that outputs something and returns nothing!'''
    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.smart_file = attacker.smart_file

    def get_results(self):
        print("in filter write to smartfile")
        with open(self.smart_file, 'a') as f:
            for line in self.previous_input.get_results():
                #print(line)
                f.write(f"{line}\n")
        return