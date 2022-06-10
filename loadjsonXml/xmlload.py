## XML (extensible markup languge)
# It is similar to HTML in its appearance, but
# XML using for data transfer.
# It is used to send and receive data b/w client and servers.

# Similar to HTML, XML also have 'tags'
# in HTML, tags are predefined like 'h'->for heading.
# In xml we have both predefined and user defined tags.

# we should open and close the tags (eg: student)
# Eg: <student> Bibin </student>  # XML element: a unit of information in XML document.

## <'name of tag/element'> 'define each tag(called text data)' </closing the tag>

## to copy a XML file data(called parsing) we need a module 'elementtree'
'''
elementtree used for,
-parsing
-finding an element
-modifying(adding/deleting ) an element from an XML file.
'''
"""
<data>  -->Root Tag(XML elements should have one root element (Parent element). 
        --> remaining all are called 'nodes'
   <country name="Liechtenstein"> --> country is Child element
       <rank updated="yes">2</rank>  --> rank , year are sub child elements
                                    --> updated is attribute name (attribute is a variable with a value)
                                    --> "yes" is the attribute value
       <year>2008</year>
       <gdppc>141100</gdppc>
       <neighbor name="Austria" direction="E"/>
       <neighbor name="Switzerland" direction="W"/>
"""
import xml.etree.ElementTree as file
tree=file.parse('file1.xml')
root=tree.getroot()



# for sub in root:
#     print("tag name",sub.tag,"\n"
#           ,"attribute ",sub.attrib)   ##now we get the sub roots only
#     for element in sub:
#         print("tag name ",element.tag)
#         print("attribute ",element.attrib)
#         print("content",element.text)  #to get data
#
# for sub in root:
#     for element in sub:
#         if element.tag=="year":
#             print(element.text)
#
# for sub in root:
#     for element in sub:
#         if element.tag=="neighbour":
#             d=element.attrib
#             for k,v in d.items():
#                 if k=="name":
#                     print(v)










