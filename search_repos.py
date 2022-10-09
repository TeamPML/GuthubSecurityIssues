import github
from secrets import MY_TOKEN

from datetime import datetime
import pause


def is_s_label(label_name):
    return 'security' in label_name.lower()


g = github.Github(login_or_token=MY_TOKEN, per_page=100)
repos = g.get_repos(since=350370, visibility='public')

for repo in repos:
    if g.rate_limiting[0] < 10:
        reset_time = datetime.fromtimestamp(g.rate_limiting_resettime)
        print(f"waiting to reset at {reset_time}")
        pause.until(reset_time)

    try:
        for label in repo.get_labels():
            if is_s_label(label.name):
                with open("selected1.txt", 'a') as f:
                    n = f.write(f'{repo.full_name}\n')
        print(f'left: {g.rate_limiting[0]}      checked: {repo.id} — {repo.full_name}')

    except Exception as e:
        print(e)
