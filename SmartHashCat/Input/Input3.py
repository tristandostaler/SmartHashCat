from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultDict")
        self.filters = [
            filters['FilterUnique'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartFile']
        ]
        self.custom_dict_en = "/usr/share/SmartHashCat/dict/1k_words_en.txt"
        self.custom_dict_fr = "/usr/share/SmartHashCat/dict/1k_words_fr.txt"
    
    def run_child(self):
        return
    
    def get_results(self):
        print("in input3")
        with open(self.custom_dict_en, 'r') as f:
            yield f.readline()
        with open(self.custom_dict_fr, 'r') as f:
            yield f.readline()