import os
import threading
import json
import time

CRON_PATH = '/var/cron.json'
class File:
    
    def get_crons(self):
        with open(CRON_PATH) as file_in:
            lines = []
            for line in file_in:
                if(line[0] != "#"):
                    line = line.rstrip('\n')
                    lines.append(line)
            return lines
    
    def create(self):
    
        f = open(CRON_PATH, "a")
        f.write("#------------  CRON TAB -----------------")
        f.close()

class Console:
	
	def run_command(self,command):
		os.system(command)

class Cron:
    
    def __init__(self):
        self.console = Console()
        self.file = File()
    
    def cron_start(self,cron):
        cron_data = json.loads(cron)
        time_interval = cron_data['time']
        commad = cron_data['command']
        time.sleep(int(time_interval))
        self.console.run_command(commad)
        time.sleep(int(time_interval))
        self.cron_start(cron)
        
    def schedule(self,crons):
        for cron in crons:
            crone_thread = threading.Thread(target=self.cron_start, args=(cron,))
            crone_thread.start()
    
    def set_cron_tab(self):
        path = CRON_PATH
        check_file = os.path.isfile(path)
        if(check_file == False):
            self.file.create()
        else:
            self.schedule(self.file.get_crons())
    
    def get_cron(self):
        self.console.run_command("ls")
        print("Working")

coron = Cron()
coron.set_cron_tab()
