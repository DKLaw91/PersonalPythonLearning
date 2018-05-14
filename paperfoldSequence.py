# https://old.reddit.com/r/dailyprogrammer/comments/8g0iil/20180430_challenge_359_easy_regular_paperfold/

sequence=""
for n in range(9):
    sequence+="1"
    bef=sequence[0:len(sequence)-1]
    for d in bef[::-1]:
        if d == "1":
            sequence+="0"
        else:
            sequence+="1"

lines=[""]
count=0
for n in sequence:
    if len(lines[count]) != 78:
        lines[count]+=n
    else:
        lines.append("")
        count+=1

for l in lines:
    print(l)
