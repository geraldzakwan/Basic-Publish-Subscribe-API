#Using zeromq for subscriber socket and it's operations
import zmq

class Subscriber:

	#Connect to publisher
	def __init__(self, portlist, verbose=None):
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.SUB)

		#Subscriber can connect to more than one publisher
		for i in range(0, len(portlist)):
			self.socket.connect ("tcp://localhost:%s" % portlist[i])

		#Create a dictionary of list to track all the notes received
		#The topics and notes are both in the form of string
		self.topiclist = {}			

		#Set verbose to true to print the notes received (stdout), false otherwise
		if(verbose==None):
			self.verbose = True
		else:			
			self.verbose = verbose

	#Subscribe to new topic that will be listened
	def registerTopic(self, utopictitle):
		topictitle = str(utopictitle)
		if(topictitle not in self.topiclist):
			#Create a new list for the topic
			self.topiclist[topictitle] = []
			#Set the new topic filter
			self.socket.setsockopt_string(zmq.SUBSCRIBE, topictitle)
		else:
			raise Exception("Topic is already registered")		

	#Unsubscribe from a topic
	def unregisterTopic(self, utopictitle):
		topictitle = str(utopictitle)
		if(topictitle in self.topiclist):
			#Delete the topic from dictionary
			del self.topiclist[topictitle]
			#Discard the topic filter
			self.socket.setsockopt_string(zmq.UNSUBSCRIBE, topictitle)
		else:
			raise Exception("Topic is not registered")

	#Listen to publisher message
	def receiveNote(self):
		#Receive the bytes
		bmessage = self.socket.recv()
		#Split it into topic and note
		btopictitle, bnote = bmessage.split()		
		#Convert byte to string (encoding=utf-8)
		topictitle = str(btopictitle, 'utf-8')
		note = str(bnote, 'utf-8')
		if(topictitle in self.topiclist):
			#Save the notes received
			self.topiclist[topictitle].append(note)
			if(self.verbose):
				print(topictitle, note)

	#To grab all the notes which have already received
	def allNotesReceived(self):
		return self.topiclist			