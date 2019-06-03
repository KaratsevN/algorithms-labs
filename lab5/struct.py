_author_ = 'Nikita Karatsev'
_project_ = 'Lab5'

import json

struct = """[
    {
      "first_name": "lol",
      "last_name": "",
      "birthdate": 0,
      "estimates": {
        "algorithms": 0,
        "maths": 0,
        "physics": 0,
        "programming": 0,
        "total": 0
      }
    },
    {
      "first_name": "lol",
      "last_name": "",
      "birthdate": 0,
      "estimates": {
        "algorithms": 0,
        "maths": 0,
        "physics": 0,
        "programming": 0,
        "total": 0
      }
    }
]
"""
#with open("struct.json") as f:
#    data = json.load(f)

def main():
    #with open('data.json', 'w') as out:
    #    json.dump(data, out)
    data = json.loads(struct)
    print(data[0]["first_name"], end = '====')
    #print(data)

if "__main()__" == main():
    main()

#print(data["students"]["0"])