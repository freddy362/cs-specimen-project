import cPickle as pickle
tablenames = pickle.load(open('tablenames.p', 'rb'))
tablemark1 = pickle.load(open('tablemark1.p', 'rb'))
tablemark2 = pickle.load(open('tablemark2.p', 'rb'))
tablemark3 = pickle.load(open('tablemark3.p', 'rb'))
totalmark = pickle.load(open('totalmark.p', 'rb'))
amountofstudents = len(tablenames)
for i in range(amountofstudents):
    
