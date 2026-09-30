import collections
import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.num_tweets = 0
        self.network = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.num_tweets, tweetId))
        # Since min heap, newer tweets have larger absolute value
        self.num_tweets -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        tmp_heap = []
        
        # 1. Deduplicate the follow list using a Set
        follows = self.network[userId].copy()
        follows.add(userId) 

        # 2. Initialize the heap with the most recent tweet from everyone
        for followee in follows:
            if self.tweets[followee]:
                # Get the index of their most recent tweet
                index = len(self.tweets[followee]) - 1
                tweet_time, tweet_id = self.tweets[followee][index]
                
                # Push: (time, tweet_id, followee_id, next_index_to_check)
                heapq.heappush(tmp_heap, (tweet_time, tweet_id, followee, index - 1))

        # 3. K-way merge using the metadata packed in the heap
        while tmp_heap and len(res) < 10:
            tweet_time, tweet_id, followee, next_idx = heapq.heappop(tmp_heap)
            res.append(tweet_id)

            # If this user has more older tweets, push the next one into the heap
            if next_idx >= 0:
                next_time, next_id = self.tweets[followee][next_idx]
                heapq.heappush(tmp_heap, (next_time, next_id, followee, next_idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].discard(followeeId)
