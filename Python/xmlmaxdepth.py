from xml.etree.ElementTree import XMLParser


class MaxDepth:
    maxdepth = 0
    depth = 0

    # Called for each opening tag
    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.maxdepth:
            self.maxdepth = self.depth

    # Called for each closing tag
    def end(self, tag):
        self.depth -= 1

    def close(self):
        return self.maxdepth


def main():
    # Root depth = 0
    # Find maximum depth
    lines = int(input())
    xmldoc = ''.join(input() for _ in range(lines))

    target = MaxDepth()
    parser = XMLParser(target=target)
    parser.feed(xmldoc)
    maxdepth = parser.close() - 1  # 0-based
    print(f'{maxdepth}')


if __name__ == '__main__':
    main()
