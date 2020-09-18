from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag) 
        for element in attrs:
            print('->',element[0],'>',element[1])
    def handle_startendtag(self, tag, attrs):
        print(tag) 
        for element in attrs:
            print('->',element[0],'>',element[1])

# instantiate the parser and fed it some HTML
string = ""
for _ in range(int(input())):
    string += input()
parser = MyHTMLParser()
parser.feed(string)