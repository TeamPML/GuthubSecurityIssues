import github
from secrets import MY_TOKEN

from utils import write_to_csv, is_s_label

from datetime import datetime
import pause

g = github.Github(login_or_token=MY_TOKEN, per_page=100)

src_file = "../data/security_issues_src.txt"
with open(src_file, 'r') as f:
    repo_names = f.readlines()
repo_names = list(map(lambda x: x.strip(), repo_names))


# with open("../data/non-security_issues.csv", 'w',  encoding='utf-8') as f:
#     f.write("repository,number,title,description,comments,is_pr,labels,is_sec\n")

for name in repo_names[repo_names.index('mRemoteNG/mRemoteNG')+1:]:
    repo = g.get_repo(name)

    for issue in repo.get_issues(state='all')[:2000]:
        if g.rate_limiting[0] < 100:
            reset_time = datetime.fromtimestamp(g.rate_limiting_resettime)
            print(f"waiting to reset at {reset_time}")
            pause.until(reset_time)

        if issue.labels and all(not is_s_label(x.name) for x in issue.labels):
            with open("../data/non-security_issues.csv", 'a',  encoding='utf-8') as f:
                write_to_csv(f, repo, issue)
        print(f'rate: {g.rate_limiting[0]} --- issue #{issue.number} in {repo.full_name} ')
