from xml.dom.minidom import parse


def read_xml(filename, sav_filename):
    domtree = parse(filename)
    rootnode = domtree.documentElement
    print(rootnode.nodeName)
    childs = rootnode.getElementsByTagName("seg")
    res = []
    for item in childs:
        # if item.hasAttribute("id")
        # print(item.getAttribute("id"))
        content = item.childNodes[0].data + '\n'
        res.append(content)

    with open(sav_filename, 'w', encoding='UTF-8') as f:
        f.writelines(res)


ref_filename = "CWMT2018-tc-govdoc-test-ref.xml"
src_filename = "CWMT2018-tc-govdoc-test-src.xml"

read_xml(src_filename, "src_test.txt")
read_xml(ref_filename, 'ref_test.txt')