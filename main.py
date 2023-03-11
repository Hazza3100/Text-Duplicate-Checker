with open('check.txt') as f:
    content = set(line.strip() for line in f if line.strip())

with open('output.txt', 'w') as f:
    f.write('\n'.join(content))
