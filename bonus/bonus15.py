import  json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
#
# print(type(content))
# print(type(data))
# print(data)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)