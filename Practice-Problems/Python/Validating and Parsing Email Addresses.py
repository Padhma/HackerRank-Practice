import re
import email.utils
for _ in range(int(input())):
    s = input()
    name, addr = email.utils.parseaddr(s)
    if re.match(r'^[a-zA-Z][\w\-_.]+@[a-zA-Z]+[.][a-z]{0,3}$', addr):
        print(name, '<{}>'.format(addr))