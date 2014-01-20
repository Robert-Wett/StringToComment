# String to Comment
## Purpose:
I find myself constantly copy+pasting comments/info into my python scripts, then manually formatting them (well, I start a macro with `10Wi<enter>`). I'd like to just highlight the string I want to convert to comments, press a command, and let it do it.

Sure, you can take a string and comment it no problem, but as far as I know there doesn't exist a plugin that will split the lines based on a defined character count, like an 80 char limit via PEP (python)

This will eventually become a **Sublime Text 2** plugin.

###TODO: 
 * Handle multiple-selections better
 * Default the `comment_char` to that of the view's current language syntax
 * Add in logic to handle strings that are longer than 80 chars without a `\n`
 * ...Profit!
