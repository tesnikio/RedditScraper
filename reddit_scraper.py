import praw
import pandas as pd
import datetime


reddit = praw.Reddit(client_id = "CLIENT ID",
                    client_secret = "CLIENT SECRET",
                    usernme = "#YOUR REDDIT USERNAME",
                    password = "#YOUR REDDIT PASSWORD",
                    user_agent = "USERAGENT")


def get_subreddit_dataframe_for_limit(subred: str, limit: int):
    subreddit = reddit.subreddit(subred)

    hot_post = subreddit.hot(limit=limit)

    author_list = []
    id_list = []
    link_flair_text_list = []
    num_comments_list = []
    score_list = []
    title_list = []
    upvote_ratio_list = []
    date = []

    for sub in hot_post:
        author_list.append(sub.author)
        id_list.append(sub.id)
        link_flair_text_list.append(sub.link_flair_text)
        num_comments_list.append(sub.num_comments)
        score_list.append(sub.score)
        title_list.append(sub.title)
        upvote_ratio_list.append(sub.upvote_ratio)
        date.append(datetime.datetime.fromtimestamp(sub.created))

    df = pd.DataFrame({'ID': id_list, 
                       'Author': author_list, 
                       'Title': title_list,
                       'Count_of_Comments': num_comments_list,
                       'Score': score_list,
                       'Upvote_Ratio': upvote_ratio_list,
                       'Flair': link_flair_text_list,
                       'Date': date
                      })

    return df
    


emacs_df = get_subreddit_dataframe_for_limit('emacs', 1000)
vim_df = get_subreddit_dataframe_for_limit('vim', 700)


emacs_df.to_csv('emacs_dataset.csv', index = False)
vim_df.to_csv('vim_dataset.csv', index = False)

