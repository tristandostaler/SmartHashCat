import CommandRunner
from Filter.FilterAbstract import FilterAbstract
import Misc


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.smart_rule = attacker.smart_rule

    def get_results(self):
        with open(self.smart_rule, 'a') as f:
            for line in self.previous_input.get_results():
                #print(line)
                f.write(f"{line}\n")
                yield line