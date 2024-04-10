import praw


reddit = praw.Reddit(
        client_id="RVs5b8mNEXFtGdijcV-SXg",
        clinet_secret="yfSaXda8qsnZXJWrA3_L1-RXLeCjdw",
        user_agent="ALX APP by u/Ok_Internet3066",
)

subreddit = reddit.subreddit("python")

top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)

for post in top_posts:
    print("Title - ", post.title)
    print("ID - ", post.id)
    print("Author - ", post.author)
    print("URL - ", post.url)
    print("Score - ", post.score)
    print("Comment count - ", post.num_comments)
    print("Created - ", post.created_utc)
    print("\n")
