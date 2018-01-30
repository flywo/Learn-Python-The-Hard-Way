#--coding:utf-8--

from sys import argv

script, user_name = argv
prompt = '> '
print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("Where do you live %s?" % user_name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("""
Alright, so you said %r about liking me. You live in %r. Not sure where that is. And you have a %r computer. Nice.
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21 """ % (likes, lives, computer))