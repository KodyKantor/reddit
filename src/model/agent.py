'''
Created on Jun 16, 2014

@author: kkantor
'''

import threading
import praw

class Agent(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self, threadID, subreddit):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.subreddit = subreddit
        self.agent = praw.Reddit(user_agent='Kantor Reddit by /u/kantosaurus')
        self.sub = self.agent.get_subreddit(self.subreddit)
        
    def retreive(self):
        '''
        Implements the threading class
        '''
        hot = self.getHot()
        print(hot)
        return hot
    
    def getHot(self):
        hot = self.sub.get_hot(limit=10)
        entries = []
        for entry in hot:
            entry = str(entry)
            entries.append(entry.split(' :: '))
        return entries