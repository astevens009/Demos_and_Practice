import sys
import fileinput

x = input("Everything that has a beginning\n")
y = input("Everything that has a beginning has an end\n")

for l in fileinput.input(files = "/workspaces/Demos_and_Practice/Sandbox/oracle_quote.txt"):
	l = l.replace(x, y)
	sys.stdout.write(l)
