import cPickle as pickle
tablenames = pickle.load(open('tablenames.p', 'rb'))
tablemark1 = pickle.load(open('tablemark1.p', 'rb'))
tablemark2 = pickle.load(open('tablemark2.p', 'rb'))
tablemark3 = pickle.load(open('tablemark3.p', 'rb'))
totalmark = []
average = 0
amountofstudents = len(tablenames)
for i in range(amountofstudents):
    totalmark.append(tablemark1[i] + tablemark2[i] + tablemark3[i])
    print tablenames[i],'got',totalmark[i],'overall'
    pickle.dump(totalmark, open("totalmark.p", "wb"))
for i in range(amountofstudents):
    average = tablemark1[i] + average
    average = tablemark2[i] + average
    average = tablemark3[i] + average
print 'The average is' ,average
pickle.dump(average, open("average.p", "wb"))




