import json

with open('test.json', 'r') as f:
    d = json.load(f)
    f.close()

for page in d['storyContent']:
    print(page['sentences'])
