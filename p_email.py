import hashlib
text="Hash this message"
recipient="schultz@packer.edu"
nonce=0
state=True
num=5
lead=""
for i in range(num):
    lead=lead+"0"
while state:
    message=recipient+" "+text+" "+str(nonce)
    hashe=hashlib.sha256(message).hexdigest()
    if hashe[0:num]==lead:
        state = False
    else:
        nonce=nonce+1
print "The proper nonce is " + str(nonce)
print message
print hashe
