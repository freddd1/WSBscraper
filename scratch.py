import praw

reddit = praw.Reddit()

sub = 'wallstreetbets'

subreddit = reddit.subreddit(sub)

i = 1
for post in subreddit.hot(limit=1):
    print()
    print(post.id)
    break
    print(post.author)
    print(post.title)
    print(post.selftext)
    print('---------------------------------------------------------------------------\n')
    for comment in post.comments:
        print(comment)



