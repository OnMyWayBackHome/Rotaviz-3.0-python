def xmlTags(xml):
    import xml.etree.ElementTree as ET
    from collections import defaultdict

    xml_tree = defaultdict(list)
    attribs = defaultdict(list)
    root = ET.fromstring(xml)


    attrib = set()
    for a in root.findall('animal'):
        print("findall", a.attrib)
        for b in list(a.attrib.keys()):
            attrib.add(b)
    #print(', '.join(sorted(list(attrib))))

    def read_tree(curr_node):
        if curr_node.tag not in xml_tree:
            xml_tree[curr_node.tag] = []
            attribs[curr_node.tag] = []
        for node in curr_node:
            xml_tree[curr_node.tag].append(node.tag)
    return

def xml_walk(level, level_num):
    next_level_tags = []
    next_level = []
    attrib = set()
    for node in level:
        for child in node:
            next_level.append(child)
            if child.tag not in next_level_tags:
                next_level.append(child)
            for b in list(child.attrib.keys()):
                    attrib.add(b)

            print('{}{}({})'.format('--'*level_num, child.tag, ', '.join(sorted(list(attrib)))))
            xml_walk(next_level, level_num + 1)
    return

xml = '''<data>
    <animal name="cat" likeable="yup">
    	<genus>Felis</genus>
        <family name="Felidae" subfamily="Felinae"/>
        <similar name="tiger" size="bigger"/>
    </animal>
    <animal name="dog">
        <family name="Canidae" member="canid"/>
        <order>Carnivora</order>
        <similar name="fox" size="similar"/>
    </animal>
</data>'''
print(xmlTags(xml))
