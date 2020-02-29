from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultDict")
        self.filters = [
            filters['FilterStripAndLower'],
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartRule']
        ]
        self.custom_dict_en = "/usr/share/SmartHashCat/dict/1k_words_en.txt"
        self.custom_dict_fr = "/usr/share/SmartHashCat/dict/1k_words_fr.txt"
    
    def run_child(self):
        return
    
    def get_results(self):
        with open(self.custom_dict_en, 'r') as f:
            for line in f:
                yield line
        with open(self.custom_dict_fr, 'r') as f:
            for line in f:
                yield line