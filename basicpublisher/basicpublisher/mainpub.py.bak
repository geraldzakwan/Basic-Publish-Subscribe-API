#Main driver to test the publisher
from publisher import Publisher
import random
import time
import sys

if len(sys.argv) > 1:
    port =  sys.argv[1]    

examplePublisher = Publisher(int(port))
#Will only send message on topics "1", "2", "3", "4", and "5"
examplePublisher.registerTopic("0")
examplePublisher.registerTopic("1")
examplePublisher.registerTopic("2")
examplePublisher.registerTopic("3")
examplePublisher.registerTopic("4")
examplePublisher.registerTopic("5")
examplePublisher.registerTopic("6")
examplePublisher.unregisterTopic("0")
examplePublisher.unregisterTopic("6")

#Stop to publish if already sent 5 messages with topic "1" or "5"
count = 0
while(count < 5):
    topic = str(random.randrange(1, 6))
    note = str(random.randrange(1,10))
    print(topic, note)
    #A delay before next publish
    time.sleep(1)
    examplePublisher.publishNote(topic, note)
    if(topic=="1" or topic=="5"):
    	count = count + 1