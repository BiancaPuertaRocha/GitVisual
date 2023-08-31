import csv, json

with open('files/projects_per_languages/bquxjob_6982122c_18a4d1be582.json', encoding='utf-8') as data_file:
   data = json.loads(data_file.read())

repos = []

for d in data:
   for repo in d.get('repo'):
      repos.append(repo.get('name'))


print(len(repos))
print(' or '.join([f"repo_name like '{x}'" for x in repos]))
   