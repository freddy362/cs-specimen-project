import cPickle as pickle
tablenames = pickle.load(open('tablenames.p', 'rb'))
tablemark1 = pickle.load(open('tablemark1.p', 'rb'))
tablemark2 = pickle.load(open('tablemark2.p', 'rb'))
tablemark3 = pickle.load(open('tablemark3.p', 'rb'))
totalmark = pickle.load(open('totalmark.p', 'rb'))
amountofstudents = len(tablenames)
highscore = -65
highscorers = []
for i in range(amountofstudents):
    if totalmark[i] >= highscore:
        highscorers.append(tablenames[i])
        highscore = totalmark[i]
    else:
        print 'Highscorers: ', highscorers
    
    
    
    
