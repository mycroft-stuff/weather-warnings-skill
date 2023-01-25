from mycroft import MycroftSkill, intent_file_handler
from subprocess import Popen, PIPE
from subprocess import list2cmdline
import shlex
from shlex import split



class WeatherWarnings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('warnings.weather.intent')
    def handle_warnings_weather(self, message):
        self.speak_dialog("intent handler")
        self.aemet()
        self.translate()
        
        
    def aemet():
        aemet = Popen(split("lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642"), stdout=PIPE)
        cut1 = Popen(split("grep -A5000 -m1 -e 'explanations:'"), stdin=lookup_aemet.stdout, stdout=PIPE)
        cut2 = Popen(split("grep -vE 'explanations:|^--'"), stdin=cut1.stdout, stdout=PIPE)
        cut3 = Popen(split("grep -m1 -B 999 -- 'Instructions:'"), stdin=cut2.stdout, stdout=PIPE)
        cut4 = Popen(split("grep -vE 'Instructions:|^--$'"), stdin=cut3.stdout, stdout=PIPE)         
        aemet = Popen(split("tail -n +2"), stdin=cut4.stdout)
        self.speak_dialog("a e m e t function")
        return(aemet)

    def translate():
        translate = Popen(split("trans :en ",str(aemet)))
        self.speak_dialog("translate function")
        print(translate)
        

def create_skill():
    return WeatherWarnings()


#lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -A5000 -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- "Instructions:" | grep -vE 'Instructions:|^--$' | tail -n +2"
