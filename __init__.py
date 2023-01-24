from mycroft import MycroftSkill, intent_file_handler
from subprocess import Popen, PIPE
from subprocess import list2cmdline
from shlex import split



class WeatherWarnings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('warnings.weather.intent')
    def handle_warnings_weather(self, message):
        self.speak_dialog('warnings.weather')
        
        lookup_aemet = Popen(split("lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642"), stdout=PIPE)
        cut1 = Popen(split("grep -A5000 -m1 -e 'explanations:'"), stdin=lookup_aemet.stdout, stdout=PIPE)
        cut2 = Popen(split("grep -vE 'explanations:|^--'"), stdin=cut1.stdout, stdout=PIPE)
        cut3 = Popen(split("grep -m1 -B 999 -- 'Instructions:'"), stdin=cut2.stdout, stdout=PIPE)
        cut4 = Popen(split("grep -vE 'Instructions:|^--$'"), stdin=cut3.stdout, stdout=PIPE)         
        cut5 = Popen(split("tail -n +2"), stdin=cut4.stdout)
        print(str(cut5))
        #translate = Popen(split("trans :en ",str(cut5)), stdin=cut5.stdout, stdout=PIPE)
        #print("Test", translate)
        
        
        xy = shlex.join(['trans ', ':en \'', str(cut5), '\''])
        
        print(xy)
        
        #print(command)
        
        #p = Popen(command, shell=True)
        
        #translate = Popen(split("trans :en \'",cut5,"\'"), stdin=cut5.stdout, stdout=PIPE)
        #translate2 = Popen(split("awk 'NR==3'"), stdin=cut4.stdout)
        
        #lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- 'Instructions:' | grep -vE 'Instructions:|^--$' | tail -n +2"
        
        #print(p)

        
        self.speak_dialog("Lalala this is a test 1 2 3")


def create_skill():
    return WeatherWarnings()


#lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -A5000 -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- "Instructions:" | grep -vE 'Instructions:|^--$' | tail -n +2"
