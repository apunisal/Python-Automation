import time
import notify2
from topnews import topStories
 
ICON_PATH = "Path" # Set Your Icon Path
# fetch news items
newsitems = topStories()
 
# initialise the d-bus connection
notify2.init("News Notifier")
 
# create Notification object
n = notify2.Notification(None, icon = ICON_PATH)
 

n.set_urgency(notify2.URGENCY_NORMAL)
 

n.set_timeout(10000)
 
for newsitem in newsitems:
 
    n.update(newsitem['title'], newsitem['description'])
    n.show()
    time.sleep(15)
