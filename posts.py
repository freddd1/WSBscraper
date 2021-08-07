class Post(object):
    def __init__(self, post_id, stock, ups, downs, num_comments, url):
        self.post_id = post_id
        self.stock = stock
        self.ups = ups
        self.downs = downs
        self.num_comments = num_comments
        self.url = url

    def json_enc(self):
        return {'stock': self.stock,
                'post_id': self.post_id,
                'url': self.url,
                'ups': self.ups,
                'downs': self.downs,
                'num_comments': self.num_comments}

