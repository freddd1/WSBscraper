import praw
import csv
import re
from posts import Post
import json
from datetime import datetime



class Scraper:
    def __init__(self, sub, sort='hot', lim=900):
        self.sub = sub
        self.sort = sort
        self.lim = lim

        print(f'Scraper instance created; values 'f'sub = {sub}, sort = {sort}, lim = {lim}')

    def set_sort(self):
        reddit = praw.Reddit()

        if self.sort == 'new':
            return self.sort, reddit.subreddit(self.sub).new(limit=self.lim)
        elif self.sort == 'top':
            return self.sort, reddit.subreddit(self.sub).top(limit=self.lim)
        elif self.sort == 'hot':
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)
        else:
            self.sort = 'hot'
            print('Sort method was not recognized, defaulting to hot.')
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)

    def get_posts(self):

        with open('tickers.csv', mode='r') as infile:
            reader = csv.reader(infile)
            tickers = [row[0] for row in reader]

        """Get unique posts from a specified subreddit."""

        # Attempt to specify a sorting method.
        sort, subreddit = self.set_sort()

        print(f'Collecting information from r/{self.sub}.')

        posts = {}
        for i, post in enumerate(subreddit):
            if post.link_flair_text != 'Meme':
                for stock in tickers:
                    # search for stock pattern:" $ticker " or " ticker$ " or " ticker "
                    search = r'\s\$?' + stock + r'\$?\s'
                    if re.search(search, post.selftext.upper()) \
                            or re.search(search, post.title.upper()):

                        id = str(post.id)
                        if id in posts:  # in case post speaks on few stocks
                            posts[id]['stock'].append(stock)
                        else:
                            posts[id] = Post(stock, post).json_enc()

            if (i + 1) % 25 == 0: print(f'scraped {i + 1} posts')  # print progress

        file_name = 'posts/{}_{}.json'.format(str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S')),
                                              str(len(posts)))
        # the file is saved in posts dir
        # with the name <date>_<time>_<num of posts>.json
        with open(file_name, 'w') as f:
            json.dump(posts, f, indent=4)


if __name__ == '__main__':
    Scraper('wallstreetbets', lim=10, sort='new').get_posts()
