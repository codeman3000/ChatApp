list = []
f = open("datalogs.txt")
list = f.readlines()
print(list)
phrase = input("Please type phrase with 1 word replaced with --")
words = phrase.split()
#do AI thing idk
preword = -1
for i in words:
  if i == "--":
    break
  preword += 1
postword = 1
for i in words:
  if i == "--":
    break
  postword += 1

prewordOK = True
postwordOK = True

#try Exception
try:
  temptry = (words[preword])
except:
  prewordOK = False

try:
  temptry = (words[postword])
except:
  postwordOK = False
postcorrelation=-1
postmatch = False
if (postwordOK):
  for i in list:
    if(i==words[postword]):
      postmatch = True
      break
  postcorrelation += 1

if (postcorrelation>-1):
  answer = list[postcorrelation]

print(answer)

print(words[preword]+words[postword])
words.append("|")
list.append(input("hey")+ "\n")
x = 0
for i in list:
  print(x)
  if list[x] == "\n":
    list.pop(x)
  x += 1
f.close
f = open("datalogs.txt","w")
print(list)


for element in list:
    if (element != "\n"):
      print("element accepted "+element)
      f.write(element + "\n")
      print("write" + element)
    else:
      print("pass")
f.close
f = open("datalogs.txt")
list = f.readlines()
print(list)