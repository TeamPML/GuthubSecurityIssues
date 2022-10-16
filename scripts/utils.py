def is_s_label(label_name):
    return 'security' in label_name.lower()


def prepare_to_csv(text):
    return '"' + text.replace('"', '""') + '"' if text else ""


# repository,number,title,description,comments,is_pr,labels,is_sec
def write_to_csv(f, repo, issue):
    f.write(repo.full_name + ',')
    f.write(str(issue.number) + ',')
    f.write(prepare_to_csv(issue.title) + ',')
    f.write(prepare_to_csv(issue.body) + ',')

    comments_str = ""
    if issue.comments:
        comments = issue.get_comments()

        for c in comments:
            comments_str += c.body
    f.write(prepare_to_csv(comments_str) + ',')

    if issue.pull_request:
        f.write('yes,')
    else:
        f.write('no,')

    labels = ""
    is_sec = False
    for label in issue.labels:
        labels += label.name + ','
        if is_s_label(label.name):
            is_sec = True

    f.write(prepare_to_csv(labels) + ',')

    if is_sec:
        f.write('yes')
    else:
        f.write('no')

    f.write('\n')
