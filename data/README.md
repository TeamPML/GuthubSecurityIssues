The structure of `security_issues.csv` and `non-security_issues.csv` is same; both files the following fields:

1. **`repository`** - full name of repository on github, in the format {owner-name/repo-name};
2. **`number`** - number of the issue; 
3. **`title`** - title of the issue; 
4. **`description`** - description(body) of the issue; 
5. **`comments`** - concatenated comments of the issue;
6. **`is_pr`** - pull requests are also considered as issues by the github API. This flag ('true'/'false') indicates whether the 'issue' is a pull request.
7. **`labels`** - comma-separated list of names labels given to the issue
8. **`is_sec`** - whether any of labels of the issue is considered security-related
