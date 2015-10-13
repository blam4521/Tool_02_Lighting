import maya.cmds as cmds
import re
import os
import sys
import itertools
import time
import io, json
from datetime import date

allSelLights = cmds.ls(sl=True)
	
today = str(date.today()) + "_T" + str(time.strftime("%H-%M-%S"))
print today
	
def MainListAndWrite(arg):

	'''
	Grabs all the attributes from lights with namespaces.
	writes the list to a json file. 
	'''
	
	#writing json format
	for i in arg:
	    #print "values are: ", i
	    jsonValues = json.dumps(i)
	    print "json format: ", jsonValues
	    with io.open('C:\DA3_WORKSPACE\LIGHTING\data.txt', 'w', encoding='utf-8') as f:
	        f.write(unicode(json.dumps(jsonValues, ensure_ascii=False)))
        f.close()
	
		


def RampForAllSelectedLights(allSelLights):
	
	'''
	copies the color/position attributes if the color slot has a ramp
	
	'''
	colorList = []
	pointList = []
	Ramps = []
	com = '//'
	
	
	
	#file = open(path, 'wb')
	
	for j in allSelLights:
		#obj2 = j.rpartition(':')[2]
		#comment = """\n%s\tRamp colour and position values for:\t%s\n"""%(com,obj2)
		#print comment
		#Ramps.append(comment)
		print j
		
		#file.write(os.linesep)    
		#file.write(comment)
		#file.write(os.linesep)
		#file.write(os.linesep)
		sel = cmds.select(j, tgl=True)
		LightSel = """select -tgl %s;"""%(j)
		print LightSel
		#file.write(LightSel)
	
		currShapes = cmds.listRelatives(j, c=True, s=True)
		currColor = cmds.listConnections(currShapes, type='ramp')
		#print currColor
		mysTuple=[str(x) for x in currColor]
		print "mysTuple: ", mysTuple
		flatT = " ".join(str(x) for x in mysTuple)
		print "flatT: ", flatT
		Ramps.append(flatT)	
	
		
		for i in Ramps:
			
			point = cmds.getAttr(i+'.colorEntryList', multiIndices=1)
			print "point: ", point
			for p in point: 
				p=str(p)
				
				colList = cmds.getAttr(i+'.colorEntryList['+p+'].color')
				posList = cmds.getAttr(i+'.colorEntryList['+p+'].position')
				cnum = list(colList)
				print "colList: ", cnum
				pval = posList
				print "posList: ", posList
				
				for c in cnum:
					colPos =  """setAttr "%s.colorEntryList[%s].position" %f;"""%(i,p,pval)
					colCol =  """setAttr "%s.colorEntryList[%s].color" -type double3 %f %f %f ;"""%(i,p,c[0],c[1],c[2]) 
					colorList.append(colPos)
					colorList.append(colCol)
		print 'colorList: ', colorList			    

		for d in colorList:
			print d
			#file.write(d)
			#file.write(os.linesep)
		return colorList	
	#file.close()
	

MainListAndWrite(RampForAllSelectedLights(allSelLights));
