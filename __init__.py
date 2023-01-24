from mycroft import MycroftSkill, intent_file_handler


class WeatherWarnings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('warnings.weather.intent')
    def handle_warnings_weather(self, message):
        self.speak_dialog('warnings.weather')


def create_skill():
    return WeatherWarnings()

