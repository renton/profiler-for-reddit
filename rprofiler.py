import praw
import config

# dict of subreddits
#   parent category to derive interests
# dict of words
#   positive/negative
#   nouns to derive interests

class RProfiler():
    def __init__(self):
        self.subreddits = {}
        self.words = {}

        self.reddit = praw.Reddit(
                                client_id = config.REDDIT_CLIENT_ID,
                                client_secret = config.REDDIT_CLIENT_SECRET,
                                password = config.REDDIT_PASSWORD,
                                username = config.REDDIT_USERNAME,
                                user_agent = config.REDDIT_USER_AGENT,
                            )

    def profile_user(self, user):
        user = self.reddit.redditor(user)
        for comment in user.comments.new(limit=None):
            self._dict_inc(self.subreddits, comment.subreddit.display_name)
        self.print_dict(self.subreddits)

    def _dict_inc(self, target_dict, key):
        if key not in target_dict:
            target_dict[key] = 0
        target_dict[key] += 1;

    def print_dict(self, target_dict):
        for k,v in target_dict.items():
            print k+' : '+v

if __name__ == "__main__":
    profiler = RProfiler()
    profiler.profile_user('djangodjango')
