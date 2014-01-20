sent = "So basically, we have imported our LoginForm class, instantiated an object from it, and sent it down to the template. This is all that is required to get form fields rendered."
max = 80
comment_char = '# '

chars_delim = sent.split(" ")
total, ret = 0, []

for idx, c in enumerate(chars_delim):
    if total == 0:
        ret.append(comment_char)
    if total + len(c) > max:
        ret.append('\n'+comment_char)
        total = 0
    total += len(c)+1
    ret.append(c+' ')

print("".join(ret))


# Output:

# So basically, we have imported our LoginForm class, instantiated an object from
# it, and sent it down to the template. This is all that is required to get form
# fields rendered.
