#!/usr/bin/env python
# Chir.py Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/chir.py)
# config.py

# API Settings
coinurl_uuid                = 'CHANGEME'
twitter_consumer_key	    = 'CHANGEME'
twitter_consumer_secret	    = 'CHANGEME'
twitter_access_token	    = 'CHANGEME'
twitter_access_token_secret = 'CHANGEME'

# Keywords & News Sources (DO NOT EDIT)
boost_keywords = ('500aday','autofollow','autofollowback','f4f','follow','follow4follow','followback','followtrain','teamfollowback','wefollowback')

news_feeds = {
    'baseball'   : 'https://sports.yahoo.com/mlb/rss.xml',
    'basketball' : 'https://sports.yahoo.com/nba/rss.xml',
    'boxing'     : 'https://sports.yahoo.com/box/rss.xml',
    'football'   : 'https://sports.yahoo.com/nfl/rss.xml',
    'golf'       : 'https://sports.yahoo.com/golf/rss.xml',
    'hockey'     : 'https://sports.yahoo.com/nhl/rss.xml',
    'mma'        : 'https://sports.yahoo.com/mma/rss.xml',
    'nascar'     : 'https://sports.yahoo.com/nascar/rss.xml',
    'soccer'     : 'https://sports.yahoo.com/soccer/rss.xml',
    'tennis'     : 'https://sports.yahoo.com/tennis/rss.xml'
}

news_keywords = {
    'baseball'   : ('baseball','mlb','homerun','worldseries','springtraining','angels','astros','athletics','bluejays','braves','brewers','cardinals','cubs','diamondbacks','dodgers','giants','indians','mariners','marlins','mets','nationals','orioles','padres','phillies','pirates','rangers','rays','redsox','reds','rockies','royals','tigers','twins','whitesox','yankees'),
    'basketball' : ('basketball','finals','nba','76ers','blazers','bucks','bulls','cavaliers','celtics','clippers','grizzlies','hawks','heat','hornets','jazz','kings','knicks','lakers','magic','mavericks','nets','nuggets','pacers','pistons','raptors','rockets','spurs','suns','thunder','timberwolves','warriors','wizards'),
    'boxing'     : ('boxing','fightnight'),
    'football'   : ('football','madden','nfl','superbowl','touchdown','49ers','bears','bengals','bills','broncos','browns','bucaneers','cardinals','chargers','cheifs','colts','cowboys','dolphins','eagles','falcons','giants','jaguars','jets','lions','packers','panthers','patriots','raiders','rams','ravens','redskins','saints','seahawks','steelers','texans','titans','vikings'),
    'golf'       : ('fedexcup','owgr','pga','pgachampionship','pgatour'),
    'hockey'     : ('hockey','nhl','worldcup','avalanche','blackhawks','bluejackets','blues','bruins','canadiens','canucks','capitals','coyotes','devils','ducks','flames','flyers','hurricanes','islanders','jets','kings','lightning','mapleleafs','oilers','panthers','penguins','predators','rangers','redwings','sabres','senators','sharks','stars','wild'),
    'mma'        : ('bellator','martialarts','mixedmartialarts','mma','ufc','wsof'),
    'nascar'     : ('buschseries','campingworldtruckseries','daytona500','iracing','nascar','sprintcup','sprintseries','winstoncup','winstoncupseries','xfinityseries'),
    'soccer'     : ('fifa','soccer','worldcup'),
    'tennis'     : ('atp','atpworldtour','masters1000','tennis','usopen')
}
