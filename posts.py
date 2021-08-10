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

