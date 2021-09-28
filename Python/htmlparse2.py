from html.parser import HTMLParser


example_html = '''
<html>
  <head>
    <title>HTML Parser - I</title>
  </head>
  <body data-modal-target class='1'>
    <h1 class="header">HackerRank</h1>
    <br id="main"/>
    <!--[if IE 9]>IE9-specific content
    <![endif]-->
    <div> Welcome to HackerRank</div>
    <!--[if IE 9]>IE9-specific content<![endif]-->
  </body>
</html>
'''


class MyHTMLParser(HTMLParser):
    '''
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for k, v in attrs:
            print(f'-> {k} > {v}')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    # Empty tags:
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for k, v in attrs:
            print(f'-> {k} > {v}')
    '''

    def handle_data(self, data):
        if data.strip():
            # print(f'Encountered some data:  {data}')
            print(f'>>> Data\n{data}')

    def handle_comment(self, data):
        if data.strip():
            lines = data.splitlines()
            if len(lines) == 1:
                # print(f'Encountered a comment:  {data}')
                print(f'>>> Single-line Comment\n{data}')
            else:
                print(f'>>> Multi-line Comment\n{data}')


def main():
    parser = MyHTMLParser()
    lines = int(input())
    data = '\n'.join(input() for _ in range(lines))

    parser.feed(data)
    parser.close()

    # Example:
    # parser.feed(example_html)


if __name__ == '__main__':
    main()
