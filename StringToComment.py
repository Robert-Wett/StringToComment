import sublime, sublime_plugin

def string_to_comment(self, sel, edit):
    words = self.view.substr(sel).split(" ")
    total, ret, max = 0, [], 80

    for word in words:
        if total + len(word) > max:
            ret.append('\n')
            total = 0
        total += len(word)+1
        ret.append(word+' ')
    self.view.replace(edit, sel, "".join(ret))
    self.view.run_command("toggle_comment", {"block" : "false"})

class StringToCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():  
            string_to_comment(self, sel, edit)
