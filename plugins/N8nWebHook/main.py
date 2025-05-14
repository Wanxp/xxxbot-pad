import tomllib

import aiohttp
import jieba
import requests

from WechatAPI import WechatAPIClient
from utils.decorators import *
from utils.plugin_base import PluginBase


class GetWeather(PluginBase):
    description = "N8N WebHook"
    author = "Wanxp"
    version = "0.0.1"

    # Change Log
    # 初始化 2025-05-14 创建插件

    def __init__(self):
        super().__init__()

        with open("plugins/N8nWebHook/config.toml", "rb") as f:
            plugin_config = tomllib.load(f)

        config = plugin_config["N8nWebHook"]

        self.enable = config["enable"]
        self.sender = config["sender"]
        self.message_keyword = config["message-keyword"]
        self.webhook_url = config["n8n-webhook-url"]
        self.auth_type = config["auth-type"]
        self.auth_key = config["auth-key"]
        self.auth_value = config["auth-value"]


    @on_text_message
    async def handle_text(self, bot: WechatAPIClient, message: dict):
        if not self.enable:
            return
        if message["FromWxid"] not in self.sender:
            return




        # 匹配keyword
        if not any(message["Content"].startswith(keyword) for keyword in self.message_keyword):
            return
        # 处理消息
        content = message["Content"]
        for keyword in self.message_keyword:
            if message["Content"].startswith(keyword):
                content = content[len(keyword):]
                break

        api_url = self.webhook_url

        headers = {
            "Content-Type": "application/json",
        }
        if self.auth_type == "Header Auth":
            headers[self.auth_key] = self.auth_value
            response = requests.post(api_url, json=message, headers=headers)
        elif self.auth_type == "Basic Auth":
            headers["Authorization"] = f"Basic {self.auth_key}:{self.auth_value}"
            response = requests.post(api_url, json=message, headers=headers)
        elif self.auth_type == "None":
            response = requests.post(api_url, json=message)
        else:
            print("Invalid auth type. Please check your config.")
            return

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return
        response_data = response.text
        return response_data
