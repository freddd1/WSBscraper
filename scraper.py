import praw
import csv
import re
import json
from datetime import datetime
from time import sleep
from posts import Post

SUB = 'wallstreetbets'


class Scraper:
    def __init__(self, sub, sort='hot', lim=900):
        self.sub = sub
        self.sort = sort
        self.lim = lim
        self.posts = {}

        print(f'[+] Scraper instance created; values 'f'sub = {sub}, sort = {sort}, lim = {lim}')

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
            print('[-] Sort method was not recognized, defaulting to hot.')
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)

    def get_posts(self):

        with open('tickers.csv', mode='r') as infile:
            reader = csv.reader(infile)
            tickers = [row[0] for row in reader]

        """Get unique posts from a specified subreddit."""

        # Attempt to specify a sorting method.
        sort, subreddit = self.set_sort()

        print(f'[+] Collecting information from r/{self.sub}')

        for i, post in enumerate(subreddit):
            print(f'\r[+] scraped {i + 1} posts', end='')  # print progress

            if post.link_flair_text != 'Meme':
                for stock in tickers:
                    # search for stock pattern:" $ticker " or " ticker$ " or " ticker "
                    search_term = r'\s\$?' + stock + r'\$?\s'
                    if re.search(search_term, post.selftext.upper()) \
                            or re.search(search_term, post.title.upper()):

                        id = str(post.id)
                        if id in self.posts:  # in case post mention few stocks
                            self.posts[id]['stock'].append(stock)
                        else:
                            try:
                                self.posts[id] = Post(stock, post).json_enc()
                            except:
                                continue

    def save_to_json(self):
        file_name = 'posts/{}_{}.json'.format(str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S')),
                                              str(len(self.posts)))

        # the file is saved in posts dir
        # with the name <date>_<time>_<num of posts>.json
        with open(file_name, 'w') as f:
            json.dump(self.posts, f, indent=4)
        print(f'\n[+] saved {len(self.posts)} posts in file: {file_name}')

try:
    while True:
        scraper = Scraper(SUB, lim=1000, sort='hot')
        scraper.get_posts()
        scraper.save_to_json()
        sleep(60 * 61)  # run the script every hour

except KeyboardInterrupt:
    print('\n[-] keyboard interrupt...quitting...saving file')
    scraper.save_to_json()
