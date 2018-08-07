
from rtmbot import RtmBot
from rtmbot.core import Plugin
from secret import SLACK_TOKEN


class HelloPlugin(Plugin):
    def process_message(self, data):
        if "덥다" in data["text"]:
            self.outputs.append([data["channel"], "http://www.kma.go.kr/upload/images_by_editor/201808/ns_08012018134529.jpg"])
        elif "날씨" in data["text"]:
            self.outputs.append([data["channel"], "http://www.onday.or.kr/wp/wp-content/uploads/2015/01/0124_1.jpg"])
        elif "기상청" in data["text"]:
            self.outputs.append([data["channel"], "https://www.youtube.com/channel/UCeBvOV4YdHbUsbsyVZDCBbA"])
        elif "노래불러줘" in data["text"]:
            self.outputs.append([data["channel"], "우리엄마:woman: 매일내게 말했어 언제나 남자:male-police-officer:조심하라고 사랑은 마치 불장난:fire:같아서 다치니까~"])
        elif "더워요" in data["text"]:
            self.outputs.append([data["channel"], "강해지세요."])
        elif "추워요" in data["text"]:
            self.outputs.append([data["channel"], "CM님 에어컨 꺼주세요"])
config = {
    "SLACK_TOKEN": SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()



# print("Be Strong")
# print("강해지겠습니다. 반성했습니다.")
# print("덥죠?")
# print("http://www.kma.go.kr/index.jsp")
# print("https://www.youtube.com/channel/UCeBvOV4YdHbUsbsyVZDCBbA")
# print("http://www.kma.go.kr/upload/images_by_editor/201808/ns_08012018134529.jpg")
# print("http://www.kma.go.kr/unkindweatherbot")
