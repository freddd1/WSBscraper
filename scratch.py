# # import praw
# # from datetime import datetime
# #
# # reddit = praw.Reddit()
# #
# # sub = 'wallstreetbets'
# #
# # subreddit = reddit.subreddit(sub)
# #
# # i = 1
# # for post in subreddit.hot(limit=7):
# #     print('\n')
# #     print(post.id)
# #     print('\n')
# #     print(post.author.id, post.author)
# #     print('\n')
# #     print(post.title)
# #     print('\n')
# #     print(post.selftext)
# #     print('\n')
# #     print(post.link_flair_text)
# #     print('\n')
# #     print(post.name)
# #     print('\n')
# #     print(post.num_comments)
# #     print('\n')
# #     print(post.permalink)
# #     print('\n')
# #     print(post.permalink)
# #     print('\n')
# #     print(post.url)
# #     print('\n')
# #     print(post.score)
# #     print('\n')
# #     print(post.upvote_ratio)
# #     print('\n')
# #     print(post.created_utc)
# #     print(datetime.fromtimestamp(post.created_utc))
# #     print('\n')
# #     print(datetime.now())
# #     print('\n')
# #
# #     print('---------------------------------------------------------------------------\n')
# #     # for comment in post.comments:
# #     #     print(comment)
#
# from datetime import datetime
# import os
#
# d = {'a':1,'b':2,'c':'3'}
# # file_name = 'posts/' + '_'.join(datetime.now().replace(microsecond=0)).split(' ') + '_' + str(len(d)) + '.json'
# a = datetime.now().strftime('%m-%d-%Y_%H-%M-%S')
# print(a)
# # with open(a, 'w') as f:
# #     pass

# import praw
#
# reddit = praw.Reddit()
#
# for i, submission in enumerate(reddit.subreddit("wallstreetbets").stream.submissions()):
#     print(i, submission)

#
# import json
#
#
#
#
# print(len(j))


d = {'a': 1, 'b':2}
d['a'] = 11
print(d)