import json
with open("log.json") as _f:
    papers = json.load(_f)

keywords_all = ['alternat']
keywords_any = ['optimization', 'optimisation']
keywords_not = ['deep', 'neural']


def related(it):
    s = it.lower()
    eva = True
    if keywords_all:
        eva &= all(k in s for k in keywords_all)
    if keywords_any:
        eva &= any(k in s for k in keywords_any)
    if keywords_not:
        eva &= not any(k in s for k in keywords_not)
    return eva

related_ps = []
with open("all.txt", 'w') as _f:
    for p in papers:
        if related(p['title']) or related(p['abstract']):
            print(p['title'])
            related_ps.append(p)

            print(p, file=_f)
            print('\n', file=_f)
