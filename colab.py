a=list(map(str,input().strip().split()))
if a[0].endswith('lios') or  a[0].endswith('etr') or  a[0].endswith('initis') in a:
    while True:
        for i in range (len(a)):
            if a[i].endswith('liala') or  a[i].endswith('etra') or  a[i].endswith('inites') in a:
                print('NO')
            break
        if a[0].endswith('etr') and len(a)==1:
            print('YES')
            break
        d=0
        for j in range (len(a)-1):
            if a[j].endswith('etr'):
                d=d+1
        for j in range (len(a)-1):
            while True:
                if a[j].endswith('etr'):
                    if a[j+1].endswith('lios'):
                        print('NO')
                        break
                elif a[j].endswith('initis'):
                    if a[j+1].endswith('etr'):
                        if a[j+1].endswith('lios'):
                            print('NO')
                            break
                elif a[j].endswith('lios'):
                    if a[j+1].endswith('initis'):
                        print('NO')
                        break
        if d!=1:
            print('NO')
            break
        else:
            print('YES')
            break
elif a[0].endswith('liala') or  a[0].endswith('etra') or  a[0].endswith('inites') in a:
    while True:
        for i in range (len(a)):
            if a[i].endswith('lios') or  a[i].endswith('etr') or  a[i].endswith('initis') in a:
                print('NO')
            break
        if a[0].endswith('etra') and len(a)==1:
            print('YES')
            break
        d=0
        for i in range (len(a)):
            if a[i].endswith('etra'):
                d=d+1
        for j in range (len(a)-1):
            if a[j].endswith('etra'):
                if a[j+1].endswith('liala'):
                    print('NO')
                    break
            elif a[j].endswith('inites'):
                if a[j+1].endswith('etra'):
                    if a[j+1].endswith('liala'):
                        print('NO')
                        break
            elif a[j].endswith('liala'):
                if a[j+1].endswith('inites'):
                        print('NO')
                        break
        if d!=1:
            print('NO')
            break
        else:
            print('YES')
            break
