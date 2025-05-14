## 功能
使用该插件可以将消息推送至n8n的Webhook中。
## 使用方法
### n8n配置
1. 在n8n中创建一个Webhook节点，设置Webhook的path。
2. 设置请求方法为POST
3. 设置一个鉴权方式 目前仅支持Basic Auth、Header Auth、None
4. 设置一个请求体格式 目前仅支持JSON、Form Data
### 插件配置
#匹配消息的发送者wxid,只要这些才会触发回调,可修改为你需要的前缀
sender=["wxid1","wxid2","wxid3"]
#匹配消息的前缀,只要这个前缀的才会触发回调,可修改为你需要的前缀
message-keyword=["n:","N:","n8n:","N8N:","n：","N：","n8n：","N8N："]
# n8n的webhook地址, 注意只支持post请求，消息体会作为请求体发送
n8n-webhook-url = "https://n8n.example.com/webhook/这里是你设置的path"
# 支持 Basic Auth, Header Auth, None
auth-type = "Header Auth"
# Basic Auth 时当前值为用户名(username)
# Header Auth时为HeaderName,
# None 无需填写
auth-key= "Authorization"
# Basic Auth 时当前值为密码(password)
# Header Auth时为HeaderValue,
# None 无需填写
auth-value= "sk-0ZxCTjjCsPoZEK"
### n8n 处理demo
1. 打开n8n
2. 导入[wechat_n8n_webhook](./wechat_n8n_webhook.json)文件
3. 开启并配置当前插件
4. 发送消息"n:a:你好"

### n8n处理接收消息格式案例如下
```json
[
  {
    "headers": {
      "connection": "keep-alive",
      "host": "n8n.example.com",
      "x-forwarded-scheme": "https",
      "x-forwarded-proto": "https",
      "x-forwarded-for": "**.**.**.**",
      "x-real-ip": "**.**.**.**",
      "content-length": "662",
      "user-agent": "python-requests/2.32.3",
      "accept-encoding": "gzip, deflate, br",
      "accept": "*/*",
      "content-type": "application/json",
      "authorization": "sk-0ZxCAjHul8tTjjCsPoZEK"
    },
    "params": {},
    "query": {},
    "body": {
      "MsgId": 176701310,
      "ToUserName": {
        "string": "wxid_id"
      },
      "MsgType": 1,
      "Content": "这里是排除前缀后的消息",
      "Status": 3,
      "ImgStatus": 1,
      "ImgBuf": {
        "iLen": 0
      },
      "CreateTime": 1747217407,
      "MsgSource": "<msgsource>\n\t<pua>1</pua>\n\t<alnode>\n\t\t<cf>2</cf>\n\t</alnode>\n\t<eggIncluded>1</eggIncladfdfdf</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n",
      "PushContent": "张三 : n：a：你好",
      "NewMsgId": 4369693081088619500,
      "MsgSeq": 709744630,
      "FromWxid": "wxid_id",
      "ToWxid": "",
      "SenderWxid": "wxid_id",
      "IsGroup": false,
      "Ats": []
    },
    "webhookUrl": "https://n8n.example.com/webhook/webhook/wechat",
    "executionMode": "test"
  }
]

```