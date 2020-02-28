import CommandRunner
from Filter.FilterAbstract import FilterAbstract
import Misc


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.smart_file = attacker.smart_file
        self.has_been_written = False

    def get_results(self):
        print("Write to smart file")
        for l in self.previous_input.get_results():
            yield l
        if not self.has_been_written:
            with open(self.smart_file, 'a') as f:
                for line in self.previous_input.get_results():
                    #print(line)
                    f.write(f"{line}\n")
                    #yield line
            self.has_been_written = True
