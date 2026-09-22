import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:

        heap = []

        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, user, index)
                )

        result = []

        while heap and len(result) < 10:

            neg_time, user, index = heapq.heappop(heap)

            time, tweetId = self.tweets[user][index]

            result.append(tweetId)

            if index > 0:
                index -= 1

                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, user, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)