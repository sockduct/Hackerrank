from pprint import pprint
#
# lxml provides a faster 100% compatible ElementTree API extended with full XPath 1.0 support+
try:
    from lxml import etree
    from lxml.etree import XMLSyntaxError
except ImportError:
    import xml.etree.ElementTree as etree


XML_FILE = 'feed.xml'
XML_BADFILE = 'feed-bad.xml'
XML_NS = '{{http://www.w3.org/2005/Atom}}{}'


def nselmt(e, ns=XML_NS):
    return ns.format(e)


def main():
    pass


if __name__ == '__main__':
    # main()
    pass


# Keep everything at the global level to allow invocation with -i:
#
# Parse XML file into an object
tree = etree.parse(XML_FILE)
# Get the root element from the object (parsed document)
root = tree.getroot()

# Note:  ElementTree represents XML elements as {namespace}<tagname>
#        (aka localname)
print(f'Root:  {root}')
print(f'Root element (tag):  {root.tag}')

# Direct children of root:
print(f'\nThe root element has {len(root)} child elements:')
for child in root:
    print(f'\\_Child:  {child}')

# Attributes:
print(f'\nAttributes:')
print(f'Root ({root}):  {root.attrib}')
# Can access direct children by index number:
print(rf'\_Child[3] ({root[3]}) has no attributes:  {root[3].attrib}')
print(rf'\_Child[4] ({root[4]}) has attributes:  {root[4].attrib}')

# Search direct children - can also do tree.findall(nselmt('entry')):
print(f'\nBasic searches:')
res = root.findall(nselmt('entry'))
for e in res:
    print(f'Search result:  {e}')
if root.findall(nselmt('feed')) == []:
    print(f"Can't find feed element because it's at the root level and we're searching "
           "root's children!")
if root.findall(nselmt('author')) == []:
    print(f"Can't find author element because it's at the grandchild level and we're "
           "searching root's children!")
# Note:  Find returns only the first match
print(f"Title of first entry:  {tree.find(nselmt('entry')).find(nselmt('title')).text}")
if (res := tree.find(nselmt('does_not_exist'))) is None:
    print(f'Searching for a non-existent element results in None:  {res}')

# Search recursively:
print(f'\nRecursive searches:')
# Leading '//' means recursive search, not just direct children
res = tree.findall(f"//{nselmt('link')}")
for e in res:
    print(f'Recursive result:  {e}, and its attributes:')
    pprint(e.attrib, indent=4)

# More powerful search expressions with lxml:
# Confirm we're using lxml:
if 'xpath' in tree.__dir__():
    # Alternatively:  if str(tree.__class__).split()[1].split('.')[0].strip('"\''):
    print(f'\nlxml extended searches:')
    # * = any localname (tag), [@href] = has href attribute
    res = tree.findall(f"//{nselmt('*[@href]')}")
    for e in res:
        print(f'Search 1:  {e}')

    # Find elements with an href whose value is "http://diveintomark.org/"
    query = nselmt("*[@href='http://diveintomark.org/']")
    res = tree.findall(f'//{query}')
    for e in res:
        print(f'Search 2:  {e}')

    xmlns = XML_NS.format('')
    # Search for Atom author elements with an Atom uri element as a child
    res = tree.findall(f"//{xmlns}author[{xmlns}uri]")
    for e in res:
        print(f'Search 3:  {e}')

    # XPath expressions
    print(f'\nlxml XPath 1.0 expressions:')
    # XPath query on namespaces elements requires namespace prefix mapping (dict):
    nsmap = dict(atom='http://www.w3.org/2005/Atom')
    # Search for category elements (in Atom namespace) that contain term attribute
    # with value 'accessibility' and then return parent element (the /..) of category
    # element found - essentially find all entries with child element of
    # <category term='accessibility'>
    ents = tree.xpath("//atom:category[@term='accessibility']/..", namespaces=nsmap)
    for e in ents:
        print(f'Entry:  {e}')
    ent = ents[0]
    # XPath expressions don't always return a list of elements
    # DOM of parsed XML doc contains nodes, not elements.  Nodes can be elements,
    # attributes, or even text content.  This query returns a list of text nodes -
    # text content (text()) of title element (atom:title) of child of current
    # element (./)
    print(ent.xpath('./atom:title/text()', namespaces=nsmap))

# Create XML document
print(f'\nCreate XML Document:')
xmlns = XML_NS.format('')
xmlns2 = '{http://www.w3.org/XML/1998/namespace}'
new_feed = etree.Element(f'{xmlns}feed', attrib={f'{xmlns2}lang': 'en'})
print(f'{etree.tostring(new_feed)}')

# Create XML document with lxml enhancements
print(f'\nCreate XML Document with lxml:')
# Using None as the prefix declares a default namespace:
nsmap = {None: 'http://www.w3.org/2005/Atom'}
xmlns2 = '{http://www.w3.org/XML/1998/namespace}'
new_feed = etree.Element(f'feed', nsmap=nsmap, attrib={f'{xmlns2}lang': 'en'})
print(f'{etree.tounicode(new_feed)}')
# Alternative way to add attribute:
# new_feed.set(f'{xmlns2}lang', 'en')
# print(f'{etree.tounicode(new_feed)}')
# Add child elements:
title = etree.SubElement(new_feed, 'title', attrib={'type': 'html'})
title.text = 'dive into &hellip;'
print(f'{etree.tounicode(new_feed)}')
print(f'{etree.tounicode(new_feed, pretty_print=True)}')

# Parsing broken XML - per standard should abort on any errors
# However, lxml can be more liberal if desired (not the default)
print(f'\nParse broken XML Document:')
try:
    tree = etree.parse(XML_BADFILE)
# except lxml.etree.XMLSyntaxError as e:
except XMLSyntaxError as e:
    print(f'{e}')

# Create a custom parser:
print(f'\nParse broken XML Document with customer lxml parser:')
cparser = etree.XMLParser(recover=True)
tree = etree.parse(XML_BADFILE, cparser)
print(f'Error log from parsing file:\n{cparser.error_log}')
print(f'Parsed:\n{etree.tounicode(tree, pretty_print=True)}')

