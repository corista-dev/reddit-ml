import praw
import pandas as pd

post_limit =10


'''
API docs:
        https://praw.readthedocs.io/en/v6.4.0/code_overview/praw_models.html
        https://github.com/praw-dev/praw/blob/master/praw/models/subreddits.py
'''


def create_session():
    return praw.Reddit(client_id='S-tAN2vs9s7w5A',
                         client_secret='-aHw_5GvoX2ePqQ9D5ng4PyIH98',
                         user_agent='scraper_r',
                         username='to_scrap',
                         password='scraper2512')


def print_description(subreddit):
    print(subreddit.description)


def choose_posts(mode, subreddit):
    '''
    Chooses the mode to retrieve.
    Available modes:
            best
            hot
            new
            controversial
            top
            rising
    :param mode: the mode name
    :return: returns the corresponding mode
    '''
    if mode == 'best':
        return subreddit.best(limit = post_limit)
    elif mode == 'hot':
        return subreddit.hot(limit = post_limit)
    elif mode == 'new':
        return subreddit.new(limit = post_limit)
    elif mode =='controversial':
        return subreddit.controversial(limit = post_limit)
    elif mode =='top':
        return subreddit.top(limit = post_limit)
    elif mode =='rising':
        return subreddit.rising(limit = post_limit)
    else:
        print('Mode not supported')
        return



def dict_structure():
    # I am providing info as author, as It can be later usefull to discard fake news
    return {
                "id": [],
                "title":[],
                "score":[],
                "body": [],
                "url":[],
                "num_comments": [],
                "created": [],
                "author": [],
                "over_18": []
            }


def populate_dict(posts):

    my_dictionary = dict_structure()

    for post in posts:
        my_dictionary["id"].append(post.id)
        my_dictionary["title"].append(post.title)
        my_dictionary["score"].append(post.score)
        my_dictionary["body"].append(post.selftext)
        my_dictionary["url"].append(post.url)
        my_dictionary["num_comments"].append(post.num_comments)
        my_dictionary["created"].append(post.created)
        my_dictionary["author"].append(post.author)
        my_dictionary["over_18"].append(post.over_18)

    return my_dictionary


def  export_to_pandas(posts_dict):
    path = 'C:\\Users\\pasilvacorista\\Documents\\reddit\\results.csv'
    df = pd.DataFrame(posts_dict)
    df.to_csv(path, index=False)

def process(mode):

    reddit = create_session()
    subreddit = reddit.subreddit('syriancivilwar')
    posts = choose_posts(mode, subreddit)
    posts_dict = populate_dict(posts)

    export_to_pandas(posts_dict)

