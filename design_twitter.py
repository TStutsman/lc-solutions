class Twitter:

    def __init__(self):
        self.followers = {}
        self.feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        followees = self.followers[userId] if userId in self.followers else [userId]

        user_feed = []
        for i in range(len(self.feed) -1, -1, -1):
            post_author, post = self.feed[i]
            if post_author in followees:
                user_feed.append(post)
            
            if len(user_feed) > 9:
                break
        
        return user_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set([followerId])
        
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers or followerId == followeeId:
            return
        
        self.followers[followerId].discard(followeeId)