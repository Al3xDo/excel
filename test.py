import re,os
fname=re.compile(r'^(.*?)(.pdf)$')
for f in os.listdir('.'):
    n=fname.search(f)
    if n==None:
        continue
    else:
        print(n.group(0))
        print(type(n.group(0)))
