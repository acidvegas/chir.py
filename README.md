# chir.py
> twitter news bot that builds followers, posts, and bitcoin via ppc links

## Requirments
* [FeedParser](http://pypi.python.org/pypi/feedparser)
* [Tweepy](http://pypi.python.org/pypi/tweepy)
* [ndg-httpsclient](http://pypi.python.org/pypi/ndg-httpsclient) *(Install only if you are getting an "InsecurePlatformWarning" error.)*

## Instructions
Register a Twitter account, and [sign up](http://dev.twitter.com/apps/new) for a new developer application.

Go to your new application settings "Keys and Access Tokens" tab.

Click the "Create Your Access Token" button on the bottom.

These will be used in the config to connect to your Twitter account.

Go to your new application settings "Permissions".

Change your access to "Read, Write and Access direct messages".

Register a [CoinURL](http://coinurl.com/) account and get your [api key](http://coinurl.com/profile-api.php).

The random number you will see after "uuid" is your unique user id that will be use in the config.

Edit your `config.py` and change the Twitter & CoinURL API settings.

## Mirrors
- [acid.vegas](https://acid.vegas/chir.py) *(main)*
- [GitHub](https://github.com/acidvegas/chir.py)
- [GitLab](https://gitlab.com/acidvegas/chir.py)
