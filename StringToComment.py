import sublime, sublime_plugin

def _stringToComment(str):
    words = str.split(" ")
    total, ret, comment_char = 0, [], '# '
    max = 80

    for idx, c in enumerate(words):
        if total == 0:
            ret.append(comment_char)
        if total + len(c) > max:
            ret.append('\n'+comment_char)
            total = 0
        total += len(c)+1
        ret.append(c+' ')
    return "".join(ret)

class StringToCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        max, comment_char = 80, '# '
        new_sels = []
        sels = self.view.sel()  
        for sel in sels:  
            new_sels.append(_stringToComment(self.view.substr(sel)))
        begin_point = sels[0].begin()
        for sel in new_sels:
            self.view.erase(edit, sels[0])
            self.view.insert(edit, begin_point, sel)

