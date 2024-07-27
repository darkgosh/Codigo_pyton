'''Exercise with json strings ' loads ',' dumps  '
'''

import json


json_string = '''
    {
        "students":[
            {
                "id":2253,
                "name":"Tim",
                "age":"21",
                "full-time":true
            },
            {
                "id":"1449",
                "name":"Joe",
                "age":33,
                "full-time":false
            }
        ]
    }
'''
data = json.loads(json_string)
#print(data["students"][0],)

data["test"] = True

new_json = json.dumps(data,indent=2, sort_keys=True)
print(new_json)

