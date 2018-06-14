# CSCI 5308: Quality Assurance - Assignment 1


### Required set-up

  - Python 2.7
  - A module named "Unittest" for test
  - A module named "xml.etree.ElementTree" for parsing and writing XML files

### How to run (CMD or Terminal)
if python 2.7 is in default system file path
```
python order.py
```
else
```
py -2 order.py
```

and then provide the input xml file name i.e abc.xml
once input XML is provided, respective response file named 'output.xml' will be generated in the same directory.


### Files in repo


| Files | Function |
| ------ | ------ |
| Order | Handles input xml file from user |
| A1 | for parsing and writing xml file and displaying output |
| security | for validating and authenticating dealer id and access key |
| part_manager | for validating delivery details and items, and validate against mock data |
| mock_data| for reference |
| test_A1 | Unit tests |

### Mock Data

| Dealer Id | Dealer Access Key |
| ------ | ------ |
| XXX-1234-ABCD-1234 | kkklas8882kk23nllfjj88290 |
| XXX-1111-ABCD-1111 | kkklas8882kk23nllfjj88291 |
| XXX-2222-ABCD-2222 | kkklas8882kk23nllfjj88292 |
| XXX-3333-ABCD-3333 | kkklas8882kk23nllfjj88293 |
| XXX-4444-ABCD-4444| kkklas8882kk23nllfjj88294 |


| Part-number | Status |
| ------ | ------ |
| 1234 | success |
| 1111 | out of stock |
| 2222 | no longer manufactured |
| 3333 | invalid part |
| 4444| success |

### References
[1] "The ElementTree XML API", Python.org. [Online]. Available: https://docs.python.org/2/library/xml.etree.elementtree.html. [Accessed: 30- May- 2018]

[2] "Addin multiple sub-elements with same tag to en XML tree with Python/Elementtree
", stackoverflow.com. [Online]. Available: https://stackoverflow.com/questions/49259985/addin-multiple-sub-elements-with-same-tag-to-en-xml-tree-with-python-elementtree. [Accessed: 30- May- 2018]

[3] "Creating a simple XML file using python", stackoverflow.com. [Online]. Available: https://stackoverflow.com/questions/3605680/creating-a-simple-xml-file-using-python. [Accessed: 31- May- 2018]

[4] "Unittest - Assert a set of items of a list are (or not) contained in another list", stackoverflow.com. [Online]. Avialable: https://stackoverflow.com/questions/45736496/unittest-assert-a-set-of-items-of-a-list-are-or-not-contained-in-another-lis. [Accessed: 30- May- 2018]

[5] "(Python) ValueError: invalid literal for int() with base 10: ", stackoverflow.com. [Online]. Available: https://stackoverflow.com/questions/36372832/python-valueerror-invalid-literal-for-int-with-base-10. [Accessed: 31- May- 2018]

[6] "Can I fake/mock the type of my mock objects in python unittests", stackoverflow.com. [Online]. Available: https://stackoverflow.com/questions/11282401/can-i-fake-mock-the-type-of-my-mock-objects-in-python-unittests. [Accessed: 30- May- 2018]

