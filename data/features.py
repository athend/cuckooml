import json
import numpy as np


X=np.random.random((3,5))

print(X)

jobj = json.load(open('2'))

filetype = []

list_obj = []

print list_obj


#print



#Signatures - Severity level
#Virustotal - scans info
#Target - category
#Behavior - Summary


for k in jobj["virustotal"]["scans"]["Symantec"]:
	list_obj.append("|".join(["virustotal", "scans", "Symantec" , str(k), "result"]) )

print jobj["target"]["category"]

print list_obj


#Generate sparse matrices here