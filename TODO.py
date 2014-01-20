# Initial scratchpad/thinking.... provbably shouldn't commit this, but hey... :)

sent = "So basically, we have imported our LoginForm class, instantiated an object from it, and sent it down to the template. This is all that is required to get form fields rendered."
max = 80
comment_char = '#'

chars = [x for x in sent]
chars_delim = sent.split(" ")
space_bank = []
ret = []
total = 0

class sentence(object):
    def __init__(word=None):
        if word is None:
            self.sentence = []
        else:
            self.sentence = [word]
     
    def append(self, word):
        self.sentence.append(word + " ")


for idx, c in enumerate(chars_delim):
    pass

for idx, c in enumerate(chars):
    if c == ' ':
        if idx > 80 % 2:
            ret.append(chars[:[space_bank[-1]]])

        space_bank.append(idx)
