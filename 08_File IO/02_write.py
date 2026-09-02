# Write to a file called Ronak Pawar.txt
# w - will overlap the previous content

f = open("Ronak Pawar.txt", "w")

string = """ Ronak Pawar is a python developer.She wants to travel India.
"""
f.write(string)

f.close()
