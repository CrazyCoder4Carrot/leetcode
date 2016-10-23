import collections
class Twitter(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.timer = 0
		self.postdict = collections.defaultdict(list)
		self.followdict = collections.defaultdict(list)
	def postTweet(self, userId, tweetId):
		"""
		Compose a new tweet.
		:type userId: int
		:type tweetId: int
		:rtype: void
		"""
		self.timer += 1
		self.postdict[userId].append((self.timer, tweetId))

	def getNewsFeed(self, userId):
		"""
		Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
		:type userId: int
		:rtype: List[int]
		"""
		userlist = self.followdict[userId]
		res = [_ for _ in self.postdict[userId]]
		for user in userlist:
			res += self.postdict[user]
		res = list(set(res))
		res.sort(key = lambda x : x[0], reverse = True)
		return [i[1] for i  in res[:10]]
		
					
		
		
	def follow(self, followerId, followeeId):
		"""
		Follower follows a followee. If the operation is invalid, it should be a no-op.
		:type followerId: int
		:type followeeId: int
		:rtype: void
		"""
		if followerId == followeeId:
			return
		self.followdict[followerId].append(followeeId)
		

	def unfollow(self, followerId, followeeId):
		"""
		Follower unfollows a followee. If the operation is invalid, it should be a no-op.
		:type followerId: int
		:type followeeId: int
		:rtype: void
		"""
		if followeeId in self.followdict[followerId]:
			self.followdict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)