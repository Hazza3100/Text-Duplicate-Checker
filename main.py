with open('check.txt') as f:
    content = f.read().split('\n')

content = set([line for line in content if line != ''])
content = '\n'.join(content)

with open('check.txt', 'w') as f:
    f.writelines(content)
