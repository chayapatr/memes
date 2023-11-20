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

def dump_replies(replies, context):
    for reply in replies:
        if isinstance(reply, praw.models.MoreComments):
            continue

        reply_data = {
            "context": context,
            "response": reply.body,
            "id": reply.submission.id,
        }

        print(reply_data)

        context.append(reply.body)
        dump_replies(reply.replies, context)
        context.pop()


after = None

if not os.path.isdir('fetched'):
    os.mkdir('fetched')

for i in range(20):

    # Fetch once
    fetched = reddit\
    .subreddit("dankmemes").controversial(limit=7, time_filter='week', params={ 'after': after })

    if not os.path.isfile('fetched.csv'):
        with open('fetched.csv', "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['post_id', 'post_name', 'post_caption', 'img_path', 'upvote_ratio'])

    with open('fetched.csv', "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        for post in fetched:
            print(post.id, post.name, post.title, post.url)

            # save img
            if not post.over_18 and not post.is_video\
            and post.url and not 'https://www.reddit.com/gallery/' in post.url:
                data = requests.get(post.url).content
                t = post.url.split(".")[-1]
                with open(f'fetched/{post.name}.{t}', 'wb') as img:
                    img.write(data)
                    after = post.name

                    # write to csv
                    writer.writerow([post.id, post.name, post.title, f'{post.name}.{t}', post.upvote_ratio])
