import praw
import requests
import json
import os
import csv

config_json = json.load(open('config.json'))
reddit = praw.Reddit(username=config_json['username'],
    password=config_json['password'],
    client_id=config_json['client_id'],
    client_secret=config_json['client_secret'],
    user_agent=config_json['user_agent']
)

after = None
cluster = ''

# create folder if not existed
if not os.path.isdir(cluster):
    os.mkdir(cluster)

for i in range(50):

    # Fetch once
    fetched = reddit\
    .subreddit(cluster).top(limit=None, time_filter='month', params={ 'after': after })

    if not os.path.isfile(f'{cluster}.csv'):
        with open(f'{cluster}.csv', "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['post_id', 'post_name', 'post_caption', 'img_path', 'upvote_ratio'])

    with open(f'{cluster}.csv', "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        for post in fetched:
            print(post.id, post.name, post.title, post.url)

            # save img
            if not post.over_18 and not post.is_video\
            and post.url and not 'https://www.reddit.com/gallery/' in post.url\
            and not 'https://www.reddit.com/r/' in post.url:
                t = post.url.split(".")[-1]
                data = requests.get(post.url).content
                with open(f'{cluster}/{post.name}.{t}', 'wb') as img:
                    img.write(data)
                    after = post.name
                    # write to csv
                    writer.writerow([post.id, post.name, post.title, f'{post.name}.{t}', post.upvote_ratio])