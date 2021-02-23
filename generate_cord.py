import os
import json

f = open("img.txt", "r")
filer = str(f.read())
f.close()

c1 = open('json\\coordinates_' + str(filer) + '.json',)
c2 = open('json\\coordinates_head.json')
data1 = json.load(c1) 
data2 = json.load(c2)

print(data1['Mouth'][0])
dict_cord = {}

cordMouth = []
cordRightEyebrow = []
cordLeftEyebrow = []
cordRightEye = []
cordLeftEye = []
cordNose = []
cordJaw = []

item = []

for i, j in zip(data1['Mouth'], data2['Mouth']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordMouth.append(item)
dict_cord['Mouth'] = cordMouth

for i, j in zip(data1['Right_Eyebrow'], data2['Right_Eyebrow']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordRightEyebrow.append(item)
dict_cord['RightEyebrow'] = cordRightEyebrow

for i, j in zip(data1['Left_Eyebrow'], data2['Left_Eyebrow']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordLeftEyebrow.append(item)
dict_cord['LeftEyebrow'] = cordLeftEyebrow

for i, j in zip(data1['Right_Eye'], data2['Right_Eye']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordRightEye.append(item)
dict_cord['RightEye'] = cordRightEye

for i, j in zip(data1['Left_Eye'], data2['Left_Eye']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordLeftEye.append(item)
dict_cord['LeftEye'] = cordLeftEye

for i, j in zip(data1['Nose'], data2['Nose']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordNose.append(item)
dict_cord['Nose'] = cordNose

for i, j in zip(data1['Jaw'], data2['Jaw']): 
    item1 = abs(i[0] - j[0])
    item2 = abs(i[1] - j[1])
    item = [item1, item2]
    cordJaw.append(item)
dict_cord['Jaw'] = cordJaw

print(dict_cord)

cmd1 = 'final_json\\cord_' + str(filer) + '.json'
with open(cmd1, 'w') as outfile:
    json.dump(dict_cord, outfile)