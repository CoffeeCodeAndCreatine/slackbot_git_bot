# slackbot_git_bot
This is a basic of how to integrate git API's into a slack bot.

## Main Features
1. Pull a list of open pull requests for a given git organization.  

## Explanation of Files
1. slackbot_git_boy.py: Source code for the slack bot
2. github_integration.py: Source code responsible for making the git call to github
3. configs.py: Confings used for auth
4. requirements.txt: List of requirements for the project

## How to Configure the slackbot_events_api_example
In order for this slack bot to work it will need a few keys to authenticate to slack, the contents of the config file as well as what they are can be found below. 
```json
{
  "slack_bot_token":"",
  "git_hub_key": "",
  "git_hub_org": "",
  "git_hub_repo_list": ["",""]
}
```

1. slack_bot_token: This is the token of the bot user configured in slack
2. git_hub_key: This is a developer key used to auth into git
3. git_hub_org: This is the name of the org you wish to monitor
4. git_hub_repo_list: This is an array containing the repos you want to check for open pull requests

## How to Run
At a high level, the steps you will need to take to get this set up are listed below. If you want a more comprehensive walk through, please check out the youtube link below. 

1. Create an application in slack
2. Add a bot user to the slack application
3. Enable OAuth for the bot user
4. Grant the bot user chat:write:bot scope
7. Copy the slack bot token to the configs.json file
8. Add in the org name, git token, and repo names into the configs.json 
8. In a terminal session launch the slack bot
9. Type 'pull requests' into slack 


## How To Video
[Coming Soon]()
