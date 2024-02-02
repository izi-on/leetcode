from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.follows: dict[int, set] = defaultdict(set)
        self.tweets: dict[int, list] = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follows[userId].add(userId)
        for follower in self.follows[userId]:
            if follower in self.tweets:
                idx = len(self.tweets[follower]) - 1
                count, tweetId = self.tweets[follower][idx]
                min_heap.append((count, tweetId, follower, idx - 1))
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[userId][index]
                heapq.heappush(min_heap, (count, tweetId, follower, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
