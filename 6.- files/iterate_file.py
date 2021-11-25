catalog = open('./6.- files/catalog.txt',"r")

hosts = []

for line in catalog:
    hosts.append(line.split(" ")[0])

print(hosts)