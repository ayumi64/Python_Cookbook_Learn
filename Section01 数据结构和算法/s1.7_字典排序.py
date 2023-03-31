from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['span'] = 4
print(d)
for key in d:
    print(key, d[key])

import json

j = json.dumps(d)
print(j)

j = json.loads(j)
print(j)
