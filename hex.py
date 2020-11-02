import sys
import string
import binascii

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
y = open(sys.argv[2], "r")
key = y.read()
z = open(sys.argv[3], "r")
inp = z.read()
#key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
#inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False



if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

values = []
message = ""

if len(key) < len(inp):
    loopedkey = ''.join(key[i % len(key)] for i in range(len(inp)))
    key = loopedkey
k = list(map(ord,key))
m = list(map(ord,inp))
for x in range(len(inp)):
    values.append(k[x] ^ m[x])

if mode == "human":
    for x in range(len(inp)):
        message = ''.join(list(map(str,map(chr,values))))
else:
    for x in range(len(inp)):
        message += hex(values[x]).lstrip("0x").rstrip("L")
        message += " "

print message
