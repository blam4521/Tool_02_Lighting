import maya.cmds as cmds
import re
import os
import sys
import itertools
import time
from datetime import date

def RampForAllSelectedLights(allSelLights, path):
	
	'''
	copies the color slot if the color slot has a ramp
	
	'''
	colorList = []
	pointList = []
	Ramps = []
	
	file = open(path, 'wb')
	
	for j in allSelLights:
		obj2 = j.rpartition(':')[2]
		comment = """\n%s\tRamp colour and position values for:\t%s\n"""%(com,obj2)
		print comment
		Ramps.append(comment)
		
		#file.write(os.linesep)    
		#file.write(comment)
		#file.write(os.linesep)
		#file.write(os.linesep)
	sel = cmds.select(i, tgl=True)
	LightSel = """select -tgl %s;"""%(obj2)
	print LightSel
	#file.write(LightSel)
	
	print 'currLight: ', obj2 
	currShapes = cmds.listRelatives(j, c=True, s=True)
	for currLightShape in currShapes:
		print '\tcurrLightShape: ',currLightShape
        point = cmds.getAttr(j+'.colorEntryList', multiIndices=1)
        for p in point:
			p = str(p)
			colList = cmds.getAttr(j+'.colorEntryList['+p+'].color')
			posList = cmds.getAttr(j+'.colorEntryList['+p+'].position')
			cnum = list(colList)
			pval = posList
			#   print 'CNUM',cnum
			#   print 'PVAL',pval
			for c in cnum:
				colPos =  """setAttr "%s.colorEntryList[%s].position" %f;"""%(obj2,p,pval)
				colCol =  """setAttr "%s.colorEntryList[%s].color" -type double3 %f %f %f ;"""%(obj2,p,c[0],c[1],c[2]) 
				platformRamps.append(colPos)
				platformRamps.append(colCol)

			for d in platformRamps:
				print d
				file.write(d)
				file.write(os.linesep)
				platformRamps = []
			
	file.close()


def ColorsForAllSelectedLight(allSelLights, path):
	
	'''
	Grabs and copies Colors from the lights
	
	'''
	colorList = []
	Ramps = []
	
	file = open(path, 'wb')

	for i in allSelLights:
		obj2 = i.rpartition(':')[2]
		comment2 =  """\n%s\tINTENSIY values for:\t%s\n"""%(com,obj2)
		print comment2
		file.write(comment2)
		file.write(os.linesep)
		file.write(os.linesep)
		sel = cmds.select(i, tgl = True)
		LightSel = """select -tgl %s;"""%(obj2)
		print LightSel
		file.write(LightSel)
		
		print 'currLight: ', obj2
		currShapes = cmds.listRelatives(i, c=True, s=True)
		for currLightShape in currShapes:
			items2 = currLightShape.rpartition(':')[2]
			print '\tcurrLightShape: ', items2
			iniRGB = cmds.getAttr(currLightShape+".color")
			print 'rgb values: ', iniRGB
			colorList.append(iniRGB)
		print "colorList: ", colorList
		#flattens the list
		merged = list(itertools.chain.from_iterable(colorList))
		print merged
			
		for c in merged:
			colCol =  """setAttr "%s.colorEntryList.color" -type double3 %f %f %f ;"""%(items2,c[0],c[1],c[2])
			print colCol
			Ramps.append(colCol)
		
		for d in Ramps:
			print d
			file.write(d)
			file.write(os.linesep)
			Ramps = []
	file.close()                		

def CoordinatesForAllSelectedLight(allSelLights, path):
	
	'''
	Grabs and copies Coordinates and attributes from the light shape and transform node
	
	'''

	#allSelLights = cmds.ls(sl=True, type='transform')
	areaLightTrans= []
	SelectionNode = []
	Lights = []
	#today = str(date.today()) + "_T" + str(time.strftime("%H-%M-%S"))
	#print today
	#path = r"C://DA3_WORKSPACE//LIGHTING//" + input + "_" + today+ ".mel"


	# Looks for all the ramps and arealights in the findAreaL
	for i in allSelLights:
		obj0 = i.rpartition(':')[0]
		obj1 = i.rpartition(':')[1]
		obj2 = i.rpartition(':')[2]
		#looks for key words to put into list, doesn't matter if it had numbers
		if 'areaLight' or 'spotLight' in obj2:
			#areaNode.append(i)
			# if var in obj2:
			Lights.append(i)
	print Lights

	file = open(path, 'wb')
	carRET = (os.linesep)
	mayaLine = 	'//Light Values for Episode:\t%s'%(input)

	file.write(mayaLine)
	file.write(os.linesep)

	for i in Lights:
		obj2 = i.rpartition(':')[2]
		comment2 =  """\n%s\tINTENSIY values for:\t%s\n"""%(com,obj2)
		print comment2
		sel = cmds.select(i, tgl = True)
		LightSel = """select -tgl %s;"""%(obj2)
		print LightSel
		SelectionNode.append(LightSel)
		file.write(os.linesep)
		file.write(comment2)
		file.write(os.linesep)
		file.write(os.linesep)
		file.write(LightSel)
		file.write(os.linesep)
		file.write(os.linesep)
		#areaLightTrans.append(comment2)
		areaT = cmds.getAttr(i + '.translate')
		areaR = cmds.getAttr(i + '.rotate')
		areaS = cmds.getAttr(i + '.scale')
		areal = cmds.getAttr(i + '.intensity')
		areaC = cmds.getAttr(i + '.color')
		areaLI = """setAttr %s.intensity %f ;"""%(obj2,areal) 
		areaLightTrans.append(areaLI)

		for t in areaT:
			t = list(t)
			areaLT = """setAttr %s.t %s %s %s ;"""%(obj2,t[0],t[1],t[2])
			areaLightTrans.append(areaLT)
		for r in areaR:
			r = list(r)
			areaLR = """setAttr %s.r %s %s %s ;"""%(obj2,r[0],r[1],r[2])
			areaLightTrans.append(areaLR)
		for s in areaS:
			s = list(s)
			areaLS = """setAttr %s.s %s %s %s ;"""%(obj2,s[0],s[1],s[2])
			areaLightTrans.append(areaLS)
		for c in areaC:
			c = list(c)
			areaLC = """setAttr %s.color -type double3 %f %f %f; """ %(obj2, c[0], c[1], c[2])
			areaLightTrans.append(areaLC)
			
		for a in areaLightTrans:
			areaLightTrans = []
			print a
			file.write(a)
			file.write(os.linesep)
			
		file.close()


def IntensityCurvesForSelectedLights(allSelLights, path):    
	
	'''
	Findes and copies the intensity curves of the spotLight
	
	'''


	keytimes = []     
	file = open(path, 'wb')
	mayaLine = 	'//Light Values for Episode:\t%s'%(input)

	print 'Looping through allSelLights...'
	for currLight in allSelLights:
		for i in allSelLights:
			obj2 = i.rpartition(':')[2]
			comment2 =  """\n%s\tINTENSIY values for:\t%s\n"""%(com,obj2)
			print comment2
			file.write(comment2)
			file.write(os.linesep)
			file.write(os.linesep)
		sel = cmds.select(i, tgl = True)
		LightSel = """select -tgl %s;"""%(obj2)
		print LightSel
		file.write(LightSel)
				
		print 'currLight: ' , obj2
		currShapes = cmds.listRelatives(currLight, c=True, s=True)
		# Looping through all shapes of current light	
		for currLightShape in currShapes:
			print '\tcurrLightShape: ',currLightShape
			currIntensity = cmds.listConnections(currLightShape, type = "animCurve")
			# Looping through all animCurve and filtering out the first and second indexes
			for a in currIntensity:
				ind2 = a.rpartition(':')[2]
				print 'Intensity curves name',ind2
			
						
			
			# Retrieve intensity key frames if current light shape has an intensity defined	    
			if(currIntensity!=None):
				intensityName = ind2
				currKeyFrames = cmds.keyframe(currIntensity, q=True, tc=True, vc=True, fc=True, iv=True)
				print '\t\tcurrKeyFrames: ', currKeyFrames
				# Iterate through key frames list in step of 3
				for i in range(0, len(currKeyFrames), 3):
											
					 index = currKeyFrames[i]
					 time = currKeyFrames[i+1]
					 value = currKeyFrames[i+2]
					 print 'keyframe -index', index,'-absolute -floatChange',time,'-valueChange',value, ind2,';'
										  
					 #keytimes.append(final)
					 for all in keytimes:
						print all                                     
						file.write(all)                     
						file.write(os.linesep)
						   
	file.close()
					 

def main():
	'''
	Gives options after the user enters the name of the light, temporary UI
	'''

	allSelLights = cmds.ls(sl=True)
	
	today = str(date.today()) + "_T" + str(time.strftime("%H-%M-%S"))
	print today
	
	path = r"C://LIGHTING//" + input + "_" + today+ ".mel"
	if os.path.isfile(path):
		print path

	if len(allSelLights) >= 1:
		print("""
				LightRig Options

				[1] - Get Ramp Color 
				[2] - Get Coordinates and Intensity
				[3] - Get Intensity Curves
				[4] - Get Color Values
				[5] - Exit
				""")
		action = raw_input("What would you like to do?(Enter a number) ")
		
		if action == '1':
			RampForAllSelectedLights(allSelLights, path)
		elif action == '2':
			CoordinatesForAllSelectedLight(allSelLights, path)
		elif action == '3':
			IntensityCurvesForSelectedLights(allSelLights, path)
		elif action == '4':
			action == ColorsForAllSelectedLight(allSelLights, path)
		elif action == '5':
			exit();
		else:
			print('No valid choice was given, try again')   
	else:
		cmds.promptDialog(title = "No Light Selected", message = "Must select at least one light")	    



##--------------------------------------------------------------------------
#Temporary UI 

dialog = cmds.promptDialog(title = "Episode Number|Light Rig", 
		message = "Enter Name:", button = ["OK", "Cancel"], 
		defaultButton = "OK", cancelButton="Cancel", dismissString = "Cancel")
 
if dialog == "OK":
	 input = cmds.promptDialog(query=True, text=True)
	 com = '//'     
	 main()
else: 
	dialog == "Cancel"
	exit()

