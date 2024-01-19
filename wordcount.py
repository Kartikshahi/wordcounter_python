
file1 = open("sample.txt")
text1 = ""

for line in file1:
    text1 += line

text1.replace(".", "")
text1.replace("!", "")
text1.replace("?", "")
text1.replace(",", "")
text1.replace(";", "")
text1.replace(":", "")
List = text1.split()
wordDictn = {}

# Count words
for word in List:
    if word in wordDictn:
        wordDictn[word] += 1
    else:
        wordDictn[word] = 1

sortedWord = sorted(wordDictn.items(), key=lambda x: x[1], reverse=True)

reports = "Word\tFrequency\n"
for entry in sortedWord:
    reports += entry[0] + "\t|\t" + str(entry[1]) + "\n"

file2 = open("report_file.txt", "w")
file2.write(reports)