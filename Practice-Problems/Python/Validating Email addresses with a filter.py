import re
def fun(s):
    emailRegex = '^[a-z0-9_-]+@[0-9a-zA-Z]+[.][a-z]{0,3}$'
	# email is of the format : username@websitename.extension
	# username contains letters, digits, dashes, underscores [a-z0-9_-]
	# websitename contains only letters and digits [0-9a-zA-Z]
	# extension can have a max length of 3 [a-z]{0,3}
    return True if re.search(emailRegex,s) else False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)