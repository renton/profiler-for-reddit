import praw
import config

class RProfiler():
    def __init__(self):
        reddit = praw.Reddit(
                                client_id = config.REDDIT_CLIENT_ID,
                                client_secret = config.REDDIT_CLIENT_SECRET,
                                password = config.REDDIT_PASSWORD,
                                user_agent = config.REDDIT_USER_AGENT,
                                username = config.REDDIT_USERNAME,
                            )


if __name__ == "__main__":
    profiler = RProfiler()
