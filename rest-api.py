import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)

print("r looks like",r.text[:100])

response_dict = r.json()

# print(response_dict.keys())

# print("Total Repositories",response_dict['total_count'])

repo_dicts = response_dict['items']

print("Respositories returned:", len(repo_dicts))

# repo_dict = repo_dicts[0]

# print('Name:',repo_dict['name'])
# print('Owner:',repo_dict['owner']['login'])
# print("Stars",repo_dict['stargazers_count'])


# print("\n Keys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#   print(key)

names, stars = [], []

for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most Starred Python projects on Git'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
