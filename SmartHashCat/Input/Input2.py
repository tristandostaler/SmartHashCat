from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultFiles")
        self.filters = [
            filters['FilterStripAndLower'],
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartRule']
        ]
        self.user_list = attacker.user_list
        self.most_common_pass = attacker.most_common_pass
        self.modifier_list = attacker.modifier_list
    
    def run_child(self):
        return
    
    def get_results(self):
        with open(self.user_list, 'r') as f:
            yield f.readline()
        with open(self.modifier_list, 'r') as f:
            yield f.readline()
        with open(self.most_common_pass, 'r') as f:
            yield f.readline()