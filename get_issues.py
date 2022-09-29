import requests

repo_addr = 'matomo-org/matomo'

params = {'state': 'all', 'per_page': 100, 'page': 1}

r = requests.get(f'https://api.github.com/repos/{repo_addr}/issues', params=params)

print(r.status_code)

issue = r.json()[7]

with open(f'{repo_addr}.txt'.replace('/', '-'), 'w') as f:
    f.write(f'ISSUE {issue["number"]}\n{issue["title"]} \n')
    for label in issue['labels']:
        f.write(label['name'])
    f.write('\n' + issue['body'])
