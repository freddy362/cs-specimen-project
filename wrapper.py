import os
import cPickle as pickle
lol = []
pickle.dump(lol, open("tablenames.p", "wb"))
pickle.dump(lol, open("tablemark1.p", "wb"))
pickle.dump(lol, open("tablemark2.p", "wb"))
pickle.dump(lol, open("tablemark3.p", "wb"))
pickle.dump(lol, open("totalmark.p", "wb"))

os.remove('tablemark1.p')
os.remove('tablemark2.p')
os.remove('tablemark3.p')
os.remove('tablenames.p')
os.remove('totalmark.p' )
import input
import basicstats1
import basicstats2
raw_input("Press Enter to continue...")
