from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCompanyName")
        self.filters = [
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartRule']
        ]
        self.company_name = attacker.company_name
    
    def run_child(self):
        return
    
    def get_results(self):
        for val in [self.company_name]:
            yield val