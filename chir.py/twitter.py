#!/usr/bin/env python
# Chir.py Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/chir.py)
# twitter.py

import random
import threading
import time

import tweepy

import config
import debug
import functions

api = None
me  = None

def login():
    global api, me
    try:
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        me  = api.me()
    except tweepy.TweepError:
        debug.error_exit('Failed to login to Twitter!')

def stats():
    debug.action('SceenName\t: %s'  % me.screen_name)
    debug.action('Registered\t: %s' % me.created_at)
    debug.action('Favorites\t: %s'  % me.favourites_count)
    debug.action('Following\t: %s'  % me.friends_count)
    debug.action('Followers\t: %s'  % me.followers_count)
    debug.action('Tweets\t\t: %s'   % me.statuses_count)

class boost_loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                if 'boost_tweet' in locals(): api.destroy_status(boost_tweet.id)
                boost_tweet = api.update_status('Support our Twitter! #' + ' #'.join(config.boost_keywords))
                debug.alert('Re-posted boost tweet.')
            except tweepy.TweepError as ex:
                debug.error('Error occured in the boost loop', ex)
            finally:
                random.shuffle(config.boost_keywords)
                time.sleep(60*5)

class favorite_loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                for tweet in tweepy.Cursor(api.home_timeline, exclude_replies=True).items(50):
                    if tweet.user.screen_name != me.screen_name:
                        if not tweet.favorited:
                            if random.choice([True, False, False, False, False]):
                                api.create_favorite(tweet.id)
                                debug.alert('Favorited a friends tweet!')
                    time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the favorite loop!', ex)
            finally:
                time.sleep(60*15)

class follow_loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                followers = api.followers_ids(me.screen_name)
                friends   = api.friends_ids(me.screen_name)
                if me.friends_count / me.followers_count == 3:
                    debug.action('Following to follower ratio is off! Starting the unfollow loop...')
                    unfollow_loop()
                for follower in followers:
                    if not follower in friends:
                        api.create_friendship(follower)
                        api.send_direct_message(screen_name=follower, text='Thanks for following our Twitter. Be sure to share us with your friends & keep up with the latest sports news!')
                        debug.alert('Followed back a follower!')
                    time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the follow loop!', ex)
            finally:
                time.sleep(60*15)

def main_loop():
    boost_loop().start()
    favorite_loop().start()
    follow_loop().start()
    news_loop().start()
    search_loop().start()

class news_loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                news   = functions.get_news()
                tweets = list()
                for item in tweepy.Cursor(api.user_timeline, exclude_replies=True).items(50):
                    tweets.append(item.text.split('... ')[0])
                    time.sleep(2)
                for item in news:
                    split = item.split('... ')[0]
                    if split not in tweets:
                        api.update_status(item)
                        debug.alert('A tweet has been posted.')
                    time.sleep(60*5)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the news loop', ex)
            finally:
                time.sleep(60*15)

class search_loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        query_keywords = list()
        for item in config.news_keywords:
            query_keywords = query_keywords + list(config.news_keywords[item])
        query_keywords = query_keywords + config.boost_keywords
        while True:
            try:
                query = random.choice(query_keywords)
                for item in api.search(q='#' + query, count=50, lang='en', result_type='mixed'):
                    if not item.user.following and not item.favorited:
                        try:
                            api.create_favorite(item.id)
                            api.create_friendship(item.user.screen_name)
                            debug.alert('Followed a similar twitter!')
                        except tweepy.TweepError as ex:
                            debug.error('Unknown error occured in the search loop!', ex)
                    time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the search loop!', ex)
            finally:
                time.sleep(60*15)

def unfollow_loop():
    try:
        followers = api.followers_ids(me.screen_name)
        friends   = api.friends_ids(me.screen_name)
        for friend in friends:
            if friend not in followers:
                api.destroy_friendship(friend)
                debug.alert('Unfollowed an unsupporting friend!')
                time.sleep(30)
    except tweepy.TweepError as ex:
        debug.error('Error occured in the unfollow loop!', ex)
