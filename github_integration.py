import requests

def get_pull_requests(git_hub_key, git_hub_org, git_hub_repos):
    response_json = []
    headers = {"Authorization": git_hub_key}
    for repo in git_hub_repos:
        try:
            url_string = "https://api.github.com/repos/" + git_hub_org + "/" + repo + "/pulls?state=open"
            resp = requests.get(url_string, headers=headers, verify=False)
            repo_pulls = resp.json()
            for repo_pull in repo_pulls:
                temp_json = {
                    "title": repo_pull.get('title'),
                    "user": repo_pull.get('user').get('login'),
                    "repo": repo,
                    "url": repo_pull.get('html_url')
                }
                response_json.append(temp_json)
        except:
            print("failed to get pr data")

    return api_to_text_response(response_json)

def api_to_text_response(response_json):
    response_string = "```Here is a list of the open pull requests:\n"
    for json in response_json:
        response_string = response_string + "\t " + json.get("url")

    response_string = response_string + "```"
    return response_string
