from slackclient import SlackClient
import json
import time
import github_integration

tokens = {}
with open('configs.json') as json_data:
    tokens = json.load(json_data)

slack_client = SlackClient(tokens.get("slack_bot_token"))

if slack_client.rtm_connect():
    while slack_client.server.connected is True:
        messages = slack_client.rtm_read()
        print(messages)
        if messages:
             for message in messages:
                if message.get("subtype") is None and message.get('user') is not None and message.get('text') is not None and  "pull requests" in message.get('text'):
                    channel = message["channel"]
                    response = github_integration.get_pull_requests(tokens.get("git_hub_key"), tokens.get("git_hub_org"), tokens.get("git_hub_repo_list"))
                    send_message = response
                    slack_client.api_call("chat.postMessage", channel=channel, text=send_message)

        time.sleep(1)
else:
    print("Connection Failed")