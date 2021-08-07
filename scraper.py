import praw
import csv
# import re
# import json
# import requests

reddit = praw.Reddit()


class Scraper:
    def __init__(self, sub, sort='new', lim=900):
        self.sub = sub
        self.sort = sort
        self.lim = lim

        print(f'Scraper instance created; values 'f'sub = {sub}, sort = {sort}, lim = {lim}')

    def set_sort(self):
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

        mentionedStocks = []
        i = 0
        for post in subreddit:
            i = i + 1
            print(i)
            if post.link_flair_text != 'Meme':
                for stock in stockTickers.keys():
                    if (re.search(r'\s+\$?' + stock + r'\$?\s+', post.selftext) or re.search(
                            r'\s+\$?' + stock + r'\$?\s+', post.title)):
                        stockTickers[stock][post.id] = StockPost(post.id, post.permalink, post.ups, post.downs,
                                                                 post.num_comments, stock)
        for stock in stockTickers:
            if len(stockTickers[stock]) > 0:
                for post in stockTickers[stock]:
                    mentionedStocks.append(stockTickers[stock][post])
        #
        # json_object = json.dumps(mentionedStocks, default=jsonDefEncoder, indent=4)
        # print(json_object)

        # with open('new.json', 'w') as j:
        #     json.dump(mentionedStocks, j, default=jsonDefEncoder, indent=4)

        # headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Flamingo-Signature': ""}
        # r = requests.post("https://wsbstonks.azurewebsites.net/api/RedditPostsAdmin", data=json_object, headers=headers)
        # print(r.status_code)
        # print(r.text)


if __name__ == '__main__':
    Scraper('wallstreetbets', lim=10, sort='hot').get_posts()
