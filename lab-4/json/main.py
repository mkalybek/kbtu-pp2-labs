import json
import texttable


with open("./sample-data.json", "r") as f:
    data = json.loads(f.read())
    table = texttable.Texttable()
    
    rows = []

    table.add_row(["DN", "Description", "Speed", "MTU"])

    im_data = data['imdata']
    for el in im_data:
        el_attributes = el["l1PhysIf"]["attributes"]
        table.add_row([el_attributes["dn"], el_attributes["descr"], el_attributes["speed"], el_attributes["mtu"]])

    print(table.draw())