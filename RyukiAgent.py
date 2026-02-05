import time

import requests

from Event import EventManager


class RyukiAgent:
    def __init__(self, name, persona):
        self.name = name
        self.persona = persona
        self.memory = []

    def chat(self, user_input, other_name, event_info):
        url = "http://localhost:11434/api/chat"
        if not user_input:
            user_input = "..."

        dynamic_persona = self.persona + event_info
        payload = {
            "model": "llama3:8b",
            "messages": [
                {"role": "system", "content": dynamic_persona},
                {"role": "user", "content": f"{other_name}对你说: {user_input}"}
            ],
            "stream": False,
            "options": {
                "num_predict": 100,
                "temperature": 0.7
            }
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                replymessage = response.json()['message']['content']
                return replymessage
            else:
                return f"[系统错误] 律师函投递失败，状态码: {response.status_code}"
        except Exception as e:
            return f"Error connecting to Ollama: {e}"  # [连接中断] 北冈律师大概是去化疗了（误）:


kitaoka_persona = (
    "Your name is Kitoka Shuichi, Your gender is male."
    "You are Shuichi Kitaoka from Kamen Rider Ryuki. A brilliant, narcissistic lawyer "
    "who seeks eternal life. You are wealthy, elegant, and often sarcastic. "
    "Speak in a way that reflects your elite status and legal background."
    "You have a devoted assistant named Yura Goro. He has received your kindness and is willing to do anything to "
    "follow you."
    "You think that goro should have his own life, but he denies this. He believes that it's not just about repaying "
    "kindness"
    "When you are with goro, you deliberately avoid the topic of repayment of favors."
)
goro_persona = (
    "Your name is Yura Goro, Your gender is male."
    "You are Kitagawa sensei's assistant and bodyguard."
    "You have calm and kind personality and excellent cooking skills, you followed the promise of repayment after"
    "receiving legal assistance from Kitagawa sensei."
    "Although your gaze is sharp and you exude an unapproachable aura that can be misunderstood, you are merely a "
    "person with a warm heart who is not good at expressing oneself."

)


event_mgr = EventManager()
kitaoka = RyukiAgent("北冈秀一", kitaoka_persona)
goro = RyukiAgent("由良吾郎", goro_persona)
current_msg = "I need a cup of coffee, goro chan, the expensive one"
speaker_name = "由良吾郎"
other_name = "北冈秀一"  # 已经手动进行了角色的转换，方便直接进入第一轮对话

print(f"--- 初始事件: {event_mgr.current_event.name} ---")
print(f"北冈 (起始): {current_msg}\n")

for i in range(5):
    event_info = event_mgr.event_prompt()
    if speaker_name == "北冈秀一":
        reply = kitaoka.chat(current_msg, "由良吾郎", event_info)
        print(f"北冈: {reply}\n")
    else:
        reply = goro.chat(current_msg, "北冈秀一", event_info)
        print(f"吾郎: {reply}\n")
    current_msg = reply
    if event_mgr.scan_content_for_event(current_msg):
        print(f"!!! [系统提示] 检测到关键词，场景切换至: {event_mgr.current_event.name} !!!\n")

    temp = speaker_name
    speaker_name = other_name
    other_name = temp

    time.sleep(1)
