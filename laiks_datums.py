import datetime

print(datetime.datetime.now())

print(datetime.datetime(2020,7,12))

import json

a= datetime.datetime.now()
perv_laiks = a.isoformat()
json_a = json.dumps(perv_laiks)
print(json_a)