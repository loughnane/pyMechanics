from pymech import *

mySystem=System()

object1=Object_PointParticle()
object2=Object_PointParticle()

mySystem.addObject(object1)
mySystem.addObject(object2)

mySystem.addInteraction(object1,object2,Gravity)