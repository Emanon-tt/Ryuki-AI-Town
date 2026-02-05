import time

import requests
import json
import random

from Event import EventManager


class RyukiAgent:
    def __init__(self, id, name, persona):
        self.id = id
        self.name = name
        self.persona = persona
        self.memory = []

    @classmethod
    def from_json(cls, character_name, json_path="data/personas.json"):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        config = data.get(character_name)
        if not config:
            raise ValueError(f"Character {character_name} not found in {json_path}, may have vanished into the mirror "
                             f"world...")
        return cls(id=config['id'], name=config['name'], persona=config['persona'])

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


start_id = random.randint(1, 4)
kitaoka = RyukiAgent.from_json("kitaoka")
goro = RyukiAgent.from_json("goro")
shinji = RyukiAgent.from_json("shinji")
ren = RyukiAgent.from_json("ren")
riders = [kitaoka, goro, shinji, ren]
starter = next(r for r in riders if r.id == start_id)
event_mgr = EventManager()

print(f"--- 轮回开始：本次首位发言者是 [{starter.name}] ---")
event_info = event_mgr.event_prompt()
initial_prompt = ("This is the beginning of the cycle. Based on your personality and current environment, take the "
                  "initiative to speak the first words or make a gesture.")
# ------------------
current_msg = starter.chat(initial_prompt, "系统广播", event_info)
speaker_name = starter.name
print(f"{starter.name} (起始): {current_msg}\n")
last_speaker_id = start_id

for i in range(5):
    possible_next_ids = [r.id for r in riders if r.id != last_speaker_id]
    next_id = random.choice(possible_next_ids)
    active_speaker = next(r for r in riders if r.id == next_id)

    event_info = event_mgr.event_prompt()
    reply = active_speaker.chat(current_msg, "all of the people", event_info)
    current_msg = reply
    print(f"{active_speaker.name}: {current_msg}\n")
    last_speaker_id = active_speaker.id

    if event_mgr.scan_content_for_event(current_msg):
        print(f"!!! [系统提示] 检测到关键词，场景切换至: {event_mgr.current_event.name} !!!\n")

    time.sleep(1)
