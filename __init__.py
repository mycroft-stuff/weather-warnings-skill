from mycroft import MycroftSkill, intent_file_handler
from subprocess import Popen, PIPE
from shlex import split



class WeatherWarnings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('warnings.weather.intent')
    def handle_warnings_weather(self, message):
        self.speak_dialog('warnings.weather')
        
        lookup_aemet = Popen(split("lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642"), stdout=PIPE)
	cut1 = Popen(split("grep -A5000 -m1 -e 'explanations:'"), stdin=lookup_aemet.stdout)
	cut2 = Popen(split("grep -vE 'explanations:|^--'"), stdin=cut1.stdout)
	cut3 = Popen(split("grep -m1 -B 999 -- 'Instructions:'"), stdin=cut2.stdout)
	cut4 = Popen(split("grep -vE 'Instructions:|^--$'"), stdin=cut3.stdout)         
	cut5 = Popen(split("tail -n +2"), stdin=cut4.stdout)         
        
        
        #lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- 'Instructions:' | grep -vE 'Instructions:|^--$' | tail -n +2"
        
	print(cut5)

        
        self.speak_dialog("Lalala this is a test")


def create_skill():
    return WeatherWarnings()


#lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -A5000 -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- "Instructions:" | grep -vE 'Instructions:|^--$' | tail -n +2"
