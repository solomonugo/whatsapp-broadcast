import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("",
                        "How far how your body? and this message na from python",
                        23, 20, 31)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")