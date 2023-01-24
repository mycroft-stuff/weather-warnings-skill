from mycroft import MycroftSkill, intent_file_handler
import subprocess


class WeatherWarnings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('warnings.weather.intent')
    def handle_warnings_weather(self, message):
        self.speak_dialog('warnings.weather')
        
        lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -A5000 -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- 'Instructions:' | grep -vE 'Instructions:|^--$' | tail -n +2"
        process = subprocess.Popen(lookup_aemet.split(), stdout=subprocess.PIPE)
        output = process.communicate()

        
        self.speak_dialog("Lalala this is a test")


def create_skill():
    return WeatherWarnings()


#lookup_aemet = "lynx -dump https://www.meteoblue.com/en/weather/warnings/gandesa_spain_3121642 | grep -A5000 -m1 -e 'explanations:' | grep -vE 'explanations:|^--' | grep -m1 -B 999 -- "Instructions:" | grep -vE 'Instructions:|^--$' | tail -n +2"
