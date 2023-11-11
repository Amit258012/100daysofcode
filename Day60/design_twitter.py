# https://leetcode.com/problems/design-twitter/

"""
postTweet(userId, tweetId):
Time Complexity: O(1)
Space Complexity: O(1)

getNewsFeed(userId):
Time Complexity: O(FlogF + logF), where F is the number of followees
Space Complexity: O(F) for the min heap (store at most F tweets)

follow(followerId, followeeId):
Time Complexity: O(1)
Space Complexity: O(F), where F is the number of followees (adding one more followee)

unfollow(followerId, followeeId):
Time Complexity: O(1)
Space Complexity: O(1)
"""
import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        # Initialize a counter for tweets and two maps: tweetMap and followMap
        self.count = 0
        # tweetMap: userId -> list of [count, tweetIds]
        self.tweetMap = defaultdict(list)
        # followMap: userId -> set of followeeId
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet to the tweetMap for the user
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement the count for each tweet
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # List to store the result
        minHeap = []  # Min heap to keep track of tweets

        # Ensure the user follows themselves
        self.followMap[userId].add(userId)

        # Iterate through each followee of the user
        for followeeId in self.followMap[userId]:
            # Check if the followee has tweets
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Push the tweet information into the min heap
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Pop tweets from the min heap until reaching the limit of 10 or the heap is empty
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # If the followee has more tweets, push the next tweet into the min heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followeeId to the set of followees for followerId
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followeeId from the set of followees for followerId if it exists
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
