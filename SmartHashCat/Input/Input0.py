from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCeWL")
        self.filters = [
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartRule']
        ]
        self.cewl_depth = attacker.cewl_depth
        self.url = attacker.url
        self.cewl_file = "tmp/cewl_out.txt"
    
    def run_child(self):
        print('Starting cewl. You can force stop anytime with '
                  '"CTRL+C"')
        CommandRunner.run_command("cewl -d " + self.cewl_depth +
                                    " -e -v " + self.url + " -w " +
                                    self.cewl_file,
                                    interuptable=True)
        Misc.print_date_time()
    
    def get_results(self):
        with open(self.cewl_file, 'r') as f:
            yield f.readline()
            