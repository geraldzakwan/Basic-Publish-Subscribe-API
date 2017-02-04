#Main driver to test the subscriber
from subscriber import Subscriber

#Listen to two publisher
portlist = ["9292", "9393"]
exampleSubscriber = Subscriber(portlist)
#Will only receive message on topics "1" and "5"
exampleSubscriber.registerTopic("1")
exampleSubscriber.registerTopic("2")
exampleSubscriber.registerTopic("3")
exampleSubscriber.registerTopic("4")
exampleSubscriber.registerTopic("5")
exampleSubscriber.unregisterTopic("2")
exampleSubscriber.unregisterTopic("3")
exampleSubscriber.unregisterTopic("4")

#Stop to listen if already got 10 notes
count = 0
while(count < 10):
    exampleSubscriber.receiveNote()
    count = count + 1

#Print all the notes received
print()
notes = exampleSubscriber.allNotesReceived();
for topics in notes:
	for i in range(0, len(notes[topics])):
		print(topics, notes[topics][i])   