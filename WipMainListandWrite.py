import maya.cmds as cmds
import re
import os
import sys
import itertools
import time
import json
from json import dumps, load
import pymel.core as pm
from datetime import date
from itertools import izip

allSelLights = cmds.ls(sl=True)
	
today = str(date.today()) + "_T" + str(time.strftime("%H-%M-%S"))


def MainListAndWrite(*args):

	'''
	Grabs all the attributes from lights with namespaces.
	writes the list to a json file. 
	'''
	#sel = pm.selected()
	#print "sel:" , sel
	
	myDict = dict((k, allSelLights) for k in args)
	print myDict
	
	for item in myDict:
		submyDict = {
			'lights ' : item,
			
		}
		
		myDict[str(item)] = submyDict

	with open(cmds.workspace(q=True, rd=True)+"data/outfile.json", 'w') as fp:
		json.dump(myDict, fp, indent=4)
	
	#print "json format: ", jsonValues
	
	
	#with open(filename, 'w') as f:
	#	f.write(dumps(i), f, indent=4)
	
MainListAndWrite(allSelLights);
		


def RampForAllSelectedLights(allSelLights):
	
	'''
	copies the color/position attributes if the color slot has a ramp
	
	'''
	colorList = []
	pointList = []
	Ramps = []
	com = '//'
	
	for j in allSelLights:
		
		print j
		
		sel = cmds.select(j, tgl=True)
		LightSel = """select -tgl %s;"""%(j)
		print LightSel
			
		currShapes = cmds.listRelatives(j, c=True, s=True)
		currColor = cmds.listConnections(currShapes, type='ramp')
		#print currColor
		mysTuple=[str(x) for x in currColor]
		#print "mysTuple: ", mysTuple
		flatT = " ".join(str(x) for x in mysTuple)
		#print "flatT: ", flatT
		Ramps.append(flatT)	
	
		
		for i in Ramps:
			
			point = cmds.getAttr(i+'.colorEntryList', multiIndices=1)
			#print "point: ", point
			for p in point: 
				p=str(p)
				
				colList = cmds.getAttr(i+'.colorEntryList['+p+'].color')
				posList = cmds.getAttr(i+'.colorEntryList['+p+'].position')
				cnum = list(colList)
				#print "colList: ", cnum
				pval = posList
				#print "posList: ", posList
				
				for c in cnum:
					colPos =  """setAttr "%s.colorEntryList[%s].position" %f;"""%(i,p,pval)
					colCol =  """setAttr "%s.colorEntryList[%s].color" -type double3 %f %f %f ;"""%(i,p,c[0],c[1],c[2]) 
					colorList.append(colPos)
					colorList.append(colCol)
		#print 'colorList: ', colorList			    

		#for d in colorList:
			#print d
		return colorList	
	


