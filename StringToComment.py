import sublime, sublime_plugin


def str_to_comment(self, sel, edit, add_char=False, char=''):
    """
    Converts a string into a valid comment string based on the
    language set for the current window/view

    Keyword arguments:
    self     -- reference to window object
    sel      -- the selected region to act on
    edit     -- sublime class needed for text manipulation
    add_char -- determines whether or not to manually prefix
                each line with a supplied `char` and whether
                or not to make the `toggle_comment` command.
                (default False)
    char     -- the value to prefix each new-line with (default '')
    """ 
    comment_char = char if add_char else ''
    words = self.view.substr(sel).lstrip().split(" ")
    comments = format_string(words, d=comment_char).replace(r"\s+\n", '\n')
    self.view.replace(edit, sel, comments)
    if not add_char:
        self.view.run_command("toggle_comment", {"block" : "false"})

def format_string(words, d, max=80):
    total, str_builder = 0, [d]
    for idx, word in enumerate(words):
        if total + len(word) > max:
            str_builder.append('\n' + d)
            total = 0
        str_builder.append(word + ' ')
        total += len(word) + 1
    return "".join(str_builder)


class StringToCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Individual checks based on languages that don't correctly add comments
        # when calling the `toggle_comment` command.
        slash = ['C#', 'ActionScript', 'Java', 'Groovy']
        dash = ['SQL', 'Haskell']
        syntax = self.view.settings().get('syntax')
        if 'Plain text' in syntax:
            [str_to_comment(self, sel, edit, add_char=True)\
             for sel in self.view.sel()]
        elif filter(lambda x: x in syntax, slash):
            [str_to_comment(self, sel, edit, add_char=True, char=r'// ')\
             for sel in self.view.sel()]
        elif filter(lambda x: x in syntax, dash):
            [str_to_comment(self, sel, edit, add_char=True, char=r'-- ')\
             for sel in self.view.sel()]
        else:
            [str_to_comment(self, sel, edit) for sel in self.view.sel()]
