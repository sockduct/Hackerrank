from html.parser import HTMLParser


example_html = '''
<html>
  <head>
    <title>HTML Parser - I</title>
  </head>
  <body data-modal-target class='1'>
    <h1 class="header">HackerRank</h1>
    <br id="main"/>
  </body>
</html>
'''


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        '''
        print(f'      Found start tag:  {tag}')
        if attrs:
            print(f'     Found attributes:  {attrs}')
        '''
        print(f'Start : {tag}')
        for k, v in attrs:
            print(f'-> {k} > {v}')

    def handle_endtag(self, tag):
        # print(f'        Found end tag:  {tag}')
        print(f'End   : {tag}')

    # Empty tags:
    def handle_startendtag(self, tag, attrs):
        '''
        print(f'   Found an empty tag:  {tag}')
        if attrs:
            print(f'     Found attributes:  {attrs}')
        '''
        print(f'Empty : {tag}')
        for k, v in attrs:
            print(f'-> {k} > {v}')

    '''
    def handle_data(self, data):
        if data.strip():
            print(f'Encountered some data:  {data}')
    '''


def main():
    parser = MyHTMLParser()

    lines = int(input())
    for _ in range(lines):
        parser.feed(input())
        # Alternatively, collect all input and then parse:
        # html += input()

    # parser.feed(html)
    #
    # Need to explicitly close?
    # parser.close()

    # Example:
    # parser.feed(example_html)


if __name__ == '__main__':
    main()

