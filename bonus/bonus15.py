import  json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
#
# print(type(content))
# print(type(data))
# print(data)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = input("Enter your answer: ")
    question["user_choice"] = user_choice

    if question["correct_answer"] == question["user_choice"]:
        score = score + 1

print(data)
print(score, "/", len(data))