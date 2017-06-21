import praw
import config

# check comments + posts
# dict of subreddits
#   parent category to derive interests
# dict of words
#   positive/negative
#   nouns to derive interests
# should take arg of reddit username

clear_chars = [ '.', ' ', '\n', '!', '?', ',', ')', '(', '[', ']', '}', '{', '"' ]

ignore_words = ['and', 'or', 'i', 'to', 'the', '', 'a', 'of', 'you', 'in', 'for', 'it', 'is',
        'with', 'but', 'like', 'this', 'that', 'have', 'be', 'my', 'on', 'would', 'so', 'as',
        'more', "i'm", 'just', 'we', 'know', 'those', 'are', 'they', "you're", "it's", 'me', 'if',
        'do', 'these', 'what', 'how', 'then', 'here', 'were', 'them', 'was', 'an', 'who', 'what',
        'at', "i'll", 'can', 'too', 'by', "don't", 'your', 'get', 'at', 'from', 'all', 'up', "i've",
        'out', 'been', 'from', 'well', 'about', 'not', 'still', 'when', 'few', 'seems', 'could',
        'would', 'some', 'not', 'there', 'their', "they're", 'other', 'had', 'any', 'he', 'she' ]

MIN_WORD_LENGTH = 5

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
            self.parse_words(comment.body)
        self.print_dict_ord_v(self.subreddits)
        print '*'*10
        self.print_dict_ord_v(self.words)

    def _dict_inc(self, target_dict, key):
        if key not in target_dict:
            target_dict[key] = 0
        target_dict[key] += 1;

    def parse_words(self, comment):
        words = comment.split(' ')
        for word in words:
            for char in clear_chars:
                word = word.lower().replace(char, '')
            if word not in ignore_words and len(word) >= MIN_WORD_LENGTH:
                self._dict_inc(self.words, word)

    def print_dict_ord_k(self, target_dict):
        for k in sorted(target_dict.iterkeys()):
            print str(k)+' : '+str(target_dict[k])

    def print_dict_ord_v(self, target_dict):
        for k in sorted(target_dict.items(), key=lambda x:x[1]):
            try:
                print str(k[0])+' : '+str(k[1])
            except:
                pass

if __name__ == "__main__":
    profiler = RProfiler()
    profiler.profile_user('baxteria')
    #profiler.profile_user('tentacruelest')
