import datetime
from datetime import datetime

class Post(object):
    def __init__(self, stock, post:"praw.models.Submission"):
        self.post_id = post.id
        self.author = post.author.name
        self.author_id = post.author.id
        self.stock = [stock]
        self.title = post.title
        self.text = post.selftext
        self.flair_text = post.link_flair_text
        self.num_comments = post.num_comments
        self.permalink = post.permalink
        self.url = 'https://www.reddit.com/'+post.permalink
        self.upvoats = post.score
        self.upvoats_ratio = post.upvote_ratio
        self.create_datetime = str(datetime.fromtimestamp(post.created_utc))
        self.scrape_datetime = str(datetime.now().replace(microsecond=0))

    def json_enc(self):
        return {
                'post_id': self.post_id,
                'author': self.author,
                'author_id': self.author_id,
                'stock': self.stock,
                'title': self.title,
                'text': self.text,
                'flair_text': self.flair_text,
                'num_comments': self.num_comments,
                'permalink': self.permalink,
                'url': self.url,
                'upvoats': self.upvoats,
                'upvoats_ratio': self.upvoats_ratio,
                'create_datetime': self.create_datetime,
                'scrape_datetime': self.scrape_datetime,
        }

    # def json_enc(obj):
    #     if hasattr(obj, 'json_enc'):
    #         return obj._json_enc()
    #     else:  # some default behavior
    #         return obj.__dict__

    # print(post.id)
    # print(post.author.id, post.author)
    # print(post.title)
    # print(post.selftext)
    # print(post.link_flair_text)
    # print(post.name)
    # print(post.num_comments)
    # print(post.permalink)
    # print(post.permalink)
    # print(post.url)
    # print(post.score)
    # print(post.upvote_ratio)
    # print(post.created_utc)
    # print(datetime.fromtimestamp(post.created_utc))
    # print(datetime.now())
# import praw
# reddit = praw.Reddit()
# sub = 'wallstreetbets'
# subreddit = reddit.subreddit(sub)
#
# i = 1
# for post in subreddit.hot(limit=1):
#     a = Post(post)
#     print(a.post_id)