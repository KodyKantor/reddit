'''
Created on Jun 16, 2014

@author: kkantor
'''

import praw

class Agent():
    '''
    The Agent is the component that interact with the Reddit API
    '''

    LIMIT = 50

    def __init__(self, subreddit):
        '''
        Constructor
        '''
        self.subreddit = subreddit
        self.agent = praw.Reddit(user_agent='Kantor Reddit by /u/kantosaurus')
        self.sub = self.agent.get_subreddit(self.subreddit)
        
    def retrieve(self, section):
        '''
        Retrieves the 
        '''
        if section == 'HOT':
            entries = self.sub.get_hot(limit=self.LIMIT)
        elif section == 'RECENT':
            entries = self.sub.get_new(limit=self.LIMIT)
        elif section == 'TOP':
            entries = self.sub.get_top(limit=self.LIMIT)
        resp = []
        for entry in entries:
            entry = unicode(entry)
            resp.append(entry.split(' :: '))
        return resp