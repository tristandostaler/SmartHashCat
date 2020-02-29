from Input.InputAbstract import InputAbstract


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultFiles")
        self.filters = [
            filters['FilterStripAndLower'],
            filters['FilterRuleFormat'],
            filters['FilterWriteToSmartRule']
        ]
        self.user_list = attacker.user_list
        self.most_common_pass = attacker.most_common_pass
        self.modifier_list = attacker.modifier_list
    
    def run_child(self):
        return
    
    def get_results(self):
        with open(self.user_list, 'r') as f:
            for line in f:
                yield line
        with open(self.modifier_list, 'r') as f:
            for line in f:
                yield line
        with open(self.most_common_pass, 'r') as f:
            for line in f:
                yield line