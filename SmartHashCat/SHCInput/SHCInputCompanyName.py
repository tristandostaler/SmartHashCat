from SHCInput.SHCInputAbstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters):
        super(SHCInput, self).__init__()
        self.filters = [
            filters['FilterStripAndLower'],
            filters['FilterWriteToSmartFile'],
            filters['FilterRuleCombinaison'],
            filters['FilterWriteToSmartRule']
        ]
        self.company_name = attacker.company_name
    
    def run_child(self):
        return
    
    def get_results(self):
        for val in [self.company_name]:
            yield val