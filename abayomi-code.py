#challenge1
def do_this():
    word = input("Enter the sentence :")
    now = word[::-1]
    print (now)
do_this()


#challenge2
kth=[1,2,4,54,88,022,15,23,12,11,67,3,4,5,6,7,8,9,0,]
MAX=max(kth)
MIN=min(kth)
print MAX
print MIN


#challenge 3
words=['4,backspace,google,federal,magic']
for i in words:
    c=words.count(i)
    if i==2:
        print i
    else:
        print "NONE"
        
#challenge on encryption
TEXT=raw_input('plaintext')
print TEXT.encode('base64')



