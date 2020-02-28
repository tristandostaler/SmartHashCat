import CommandRunner
from Filter.FilterAbstract import FilterAbstract
import Misc
import sys


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.new_run = False
        self.smart_file = attacker.smart_file
        self.user_list = attacker.user_list
        self.modifier_list = attacker.modifier_list

    def get_lines_1(self):
        for l in self.previous_input.get_results():
            yield l.strip().lower()
    
    def get_lines_2(self):
        for l in open(self.user_list, "r"):
            yield l.strip().lower()

    def get_lines_3(self):
        for l in open(self.modifier_list, "r"):
            yield l.strip().lower()

    def get_results(self):
        print("in filter combinaison")
        Misc.print_date_time()
        print("Starting combinations")

        for l1 in self.get_lines_1():
            yield l1
        for l2 in self.get_lines_2():
            yield l2
        for l3 in self.get_lines_3():
            yield l3
        
        for l1 in self.get_lines_1():
            for l2 in self.get_lines_2():
                yield f"{l1}{l2}"

        for l1 in self.get_lines_1():
            for l3 in self.get_lines_3():
                yield f"{l1}{l3}"

        for l2 in self.get_lines_2():
            for l3 in self.get_lines_3():
                yield f"{l2}{l3}"
        
        for l1 in self.get_lines_1():
            for l2 in self.get_lines_2():
                for l3 in self.get_lines_3():
                    yield f"{l1}{l2}{l3}"
                    yield f"{l1}{l3}{l2}"
                    yield f"{l2}{l1}{l3}"
                    yield f"{l2}{l3}{l1}"
                    yield f"{l3}{l1}{l2}"
                    yield f"{l3}{l2}{l1}"