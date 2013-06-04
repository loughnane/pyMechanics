class Object(object):
	"""
	Has state variables like velocity/energy
	"""

	def __init__(self,):
		pass

class Model(object):
	"""
	What core Model(s) is(are) invovled?
	"""

class Motion(object):
	def __init__(self):
		self.mechanicalEnergy

class Interaction(object):
	def __init__(self,object1,object2):
		self.object1=object1
		self.object2=object2
	def __str__(self):
		return "{} interaction between {} and {}".format(self.__class__,object1,object2)

class System(object):
	def __init__(self,objectList=[],model=None):
		self.allowableInteractions=set([Gravity,Contact,Tension,ElasticRestoring])
		self.allowableModels=set([DynamicsNetForce,MomentumImpulse,MechanicalEnergyWork,RotationalDynamicsNetTorque,AngularMomentumImpulse])
		# if model:
			

		self.objects=objectList
		self.interactions=[]

	def addInteraction(self,object1,object2,interactionType):
		assert interactionType in self.allowableInteractions, '{} is not an allowable interaction'.format(interactionType)
		assert object1 in self.objects, '{} is not a part of this System'.format(object1)
		assert object2 in self.objects, '{} is not a part of this System'.format(object1)
		
		self.interactions.append(interactionType(object1,object2))

	def addObject(self,newObject):
		self.objects.append(newObject)





class DynamicsNetForce(Model):
	pass

class MomentumImpulse(Model):
	pass

class MechanicalEnergyWork(Model):
	pass

class RotationalDynamicsNetTorque(Model):
	pass

class AngularMomentumImpulse(Model):
	pass


class Motion_Rotational(Motion):
	def __init__(self):
		self.angularVelocity
		self.angularMomentum

class Motion_Linear(Motion):
	def __init__(self):
		self.velocity
		self.momentum


class Object_PointParticle(Object):
	"""
	"""
	pass

class Object_RigidBody(Object):
	"""
	"""
	pass


class Gravity(Interaction):
	def __init__(self,object1,object2):
		"""
		Both universal and uniform
		"""
		Interaction.__init__(self,object1,object2)

class Contact(Interaction):
	def __init__(self,object1,object2):
		"""
		When two bodies touch
		"""
		Interaction.__init__(self,object1,object2)

class Tension(Interaction):
	def __init__(self,object1,object2):
		"""
		Such as in a string
		"""
		Interaction.__init__(self,object1,object2)

class ElasticRestoring(Interaction):
	def __init__(self):
		"""
		Each of the two basic types of motion can
		be described using any one of five physical
		quantities of variables to describe the state
		of motion of the system
		"""
		Interaction.__init__(self,object1,object2)