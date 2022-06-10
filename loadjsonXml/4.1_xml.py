# XML (extensible markup language)
# It is similar to HTML in its appearance, but XML is used for data transfer.
# It is used to send and receive data b/w client and servers.

# Similar to HTML, XML also have tags.
# In XML we have both predefined and user defined tags.

# We should open and close the tags.
# eg. <student> John </student>  - XML element: a unit of information in XML document.
# The data between the opening and closing tags is called "text data".

# To copy data from an XML file (called parsing) we need the 'ElementTree' module.

# ElementTree is user for:
# > parsing
# > finding an element
# > modifying (adding/deleting) an element from and XML file.

"""
<data>                                      -> Root Tag- XML elements should have one root element (parent element)
                                            -> Remaining all are called 'nodes'
   <country name="Liechtenstein">           -> "country" is the child element
       <rank updated="yes">2</rank>         -> "rank", "year" etc. are sub-child elements
                                            -> "updated" is an attribute name (a variable with a value)
                                            -> "yes" is the attribute value
       <year>2008</year>
       <gdppc>141100</gdppc>
       <neighbor name="Austria" direction="E"/>
       <neighbor name="Switzerland" direction="W"/>
   </country>
</data>
"""

# import xml.etree.ElementTree as Tree
# content = Tree.parse('4_data.xml')
# print(content)
# root = content.getroot()  # to get the root element of this file
# print(root)
# print(root.tag)  # to get the name of the root element
# print(root[0].tag)  # to know the first child element's tag name
# print(root[0].attrib)  # to know the attribute of the child element
#
# for child in root:
#     print('tag name:', child.tag, '  attribute: ', child.attrib)
# #
# for child in root:
#     print('tag name:', child.tag, '  attribute: ', child.attrib)
#     for element in child:
#         print('\ttag name:', element.tag, '  attribute:', element.attrib, '  content:', element.text)
# #
# for child in root:
#     for element in child:
#         if element.tag == 'year':
#             print(element.text)
# #
# for child in root:
#     for element in child:
#         if element.tag == 'rank':
#             print(element.attrib)
# #
# for child in root:
#     for element in child:
#         if element.tag == 'neighbor':
#             print(element.attrib)
#             print(element.attrib['name'])
