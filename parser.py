from xml.dom import minidom
from sys import stdout

f = open('fixtures/input.html', mode='r')
dom = minidom.parse(f)

def printDom(domElement):

    for node in domElement.childNodes:

        if isinstance(node, minidom.Element):
            stdout.write("%s -> %s\n" % \
                  (node.nodeName ,' '.join([i.nodeName for i in node.childNodes if isinstance(i, minidom.Element)])))
            printDom(node)

printDom(dom)

