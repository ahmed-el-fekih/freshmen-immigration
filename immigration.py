# task1 (python lists)
commands = int(input("number of commands> "))
list = []
for i in range(commands):
    userCmd = input("type your command ").split()
    if userCmd[0] == "print":
        print(list)

    elif userCmd[0] == "pop":
        list.pop()

    elif userCmd[0] == "reverse":
        list = list.reverse()

    elif userCmd[0] == "append":
        list.append(int(userCmd[1]))

    elif userCmd[0] == "remove":
        list.remove(int(userCmd[1]))

    elif userCmd[0] == "insert":
        list.insert(int(userCmd[1]),int(userCmd[2]))

    elif userCmd[0] == "sort":
        list.sort()

# task2 (nested lists)
n = int(input())
fullList = [[]]*n
scores = [1]*n

for i in range(n):
    name = input()
    score = input()
    nameAndScore = [name,score]
    fullList[i] = nameAndScore
    scores[i] = score

scores.sort()
secondLowest = scores[1]
names = []

for i in range(len(fullList)):
    if fullList[i][1] == secondLowest:
        names.append(fullList[i][0])
names.sort()
print(names)

# task 3 (stuttering)
word = input("type a word that has more than 2 characters> ")
repeat = word[0:2] + "..."
print(repeat + repeat + word + "?")
