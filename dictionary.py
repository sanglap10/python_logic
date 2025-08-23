sample = {
    "name":"sanglap",
    "age":19,
    "city":"durgapur",
    "phoneNumber":3098040
}
people = [
    {
        "name":"sanglap",
        "age":18,
        "city":"durgapur"
    },
    {
        "name":"bhaskar",
        "age":30,
        "city":"chandigarh"
    }
]

def printProperty():
    for i in people:
        print(i["name"])


def appendToPeople(people_dict):
    people_dict.append({
        "name":"wefdkfn",
        "age":13,
        "city":"dsfjhorf"
    })

def addKeyUsingForLoop(dict,key,value):
    for d in dict:
        d[key] = value

def addKey(dict,key,value):
    dict[key] = value


printProperty()
# addKeyUsingForLoop(people,"email","ffkdjflofhdof@kf.com")
# print("\n")
# appendToPeople(people)
# print(people)    
# addKey(sample,"country","russia")
# print(sample)
