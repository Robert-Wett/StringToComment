import sublime, sublime_plugin


def str_to_comment(self, sel, edit, add_char=False, char=''):
    comment_char = char if add_char else ''
    words = self.view.substr(sel).split(" ")
    comments = format_string(words, d=comment_char)
    self.view.replace(edit, sel, comments)
    if not add_char:
        self.view.run_command("toggle_comment", {"block" : "false"})

def format_string(words, d, max=80):
    total, str_builder = 0, [d]
    for idx, word in enumerate(words):
        if total + len(word) > max:
            str_builder[idx-1] = str_builder[idx-1][:-1]
            str_builder.append('\n' + d)
            total = 0
        total += len(word) + 1
        str_builder.append(word + ' ')    
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
