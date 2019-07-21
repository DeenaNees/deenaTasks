import csv
import xml.etree.ElementTree as ET

tree = ET.parse('pair.xml')
root = tree.getroot()
test_result = []

with open('test_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Test Case Name", "file", "class name", "time", "status", "failure msg"])
csvFile.close()

for child in root:
    test_result = []

    name = child.get('name')
    test_result.append(str(name))

    file = child.get('file')
    test_result.append(file)

    class_name = child.get('classname')
    test_result.append(str(class_name))

    time = child.get('time')
    test_result.append(str(time))

    status = failure_str = ""

    if(child.find('failure') != None):
        status = "faild"
        failure = child.find('failure')
        failure_msg = failure.get('message')
        failure_txt = failure.text.split()
        failure_str = failure_msg + '\n' + failure_txt[0]+" "+failure_txt[1]+" "+failure_txt[2]
    else:
        status = "pass"
        failure_str = " _ "

    test_result.append(str(status))
    test_result.append(str(failure_str))

    with open('test_result.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(test_result)
    csvFile.close()