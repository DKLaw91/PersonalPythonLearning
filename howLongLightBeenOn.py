# https://old.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/

inp="1 3\n2 3\n4 5"

visitors=[i for i in inp.splitlines()]
ranges=(range(int(v[0]),int(v[2])) for v in visitors)
print(len(set().union(*ranges)))
