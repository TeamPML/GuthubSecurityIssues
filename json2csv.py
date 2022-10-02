import json
import os

repo_addr = 'matomo-org/matomo'


def prepare_to_csv(text):
    return '"' + text.replace('"', '""') + '"' if text else ""


with open(f'{repo_addr}.csv', 'w',  encoding='utf-8') as f:
    f.write('number,title,description,labels\n')

    for filename in os.listdir(repo_addr):
        json_file = os.path.join(repo_addr, filename)

        with open(json_file, encoding='utf-8') as jf:
            issues = json.load(jf)

        for issue in issues:
            f.write(str(issue['number']) + ',')
            f.write(prepare_to_csv(issue['title']) + ',')
            f.write(prepare_to_csv(issue['body']) + ',')

            labels = ""
            for label in issue['labels']:
                labels += label['name'] + ','

            f.write(prepare_to_csv(labels))
            f.write('\n')
