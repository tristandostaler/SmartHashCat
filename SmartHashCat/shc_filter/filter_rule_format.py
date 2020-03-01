from shc_filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)

    def transform_to_prepend_hashcat_format(self, word):
        to_return = ""
        for c in word[::-1]:
            to_return += "^"+c
        return to_return

    def transform_to_apend_hashcat_format(self, word):
        to_return = ""
        for c in word:
            to_return += "$"+c
        return to_return

    def get_results(self):
        yield ":"
        for l in self.previous_input.get_results():
            yield f"{self.transform_to_prepend_hashcat_format(l)} :"
            yield f": {self.transform_to_apend_hashcat_format(l)}"