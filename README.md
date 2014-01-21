# String to Comment
## Purpose:
I find myself constantly copy+pasting comments/info into my python scripts, then manually formatting them (well, I start a macro with `10Wi<enter>`). I'd like to just highlight the string I want to convert to comments, press a command, and let it do it.

Sure, you can take a string and comment it no problem, but as far as I know there doesn't exist a plugin that will split the lines based on a defined character count, like an 80 char limit via PEP (python)

This will eventually become a **Sublime Text 2** plugin.

###TODO: 
 * Handle multiple-selections better
 * ~~Default the comment character to that of the view's current language syntax~~
 * Add in logic to handle strings that are longer than 80 chars without a `\n`
 * ...Profit!

===
###Current State
**Input:**  
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.  
  
**Output:**
<pre><code># Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem  
# Ipsum has been the industry's standard dummy text ever since the 1500s, when an  
# unknown printer took a galley of type and scrambled it to make a type specimen  
# book. It has survived not only five centuries, but also the leap into electronic  
# typesetting, remaining essentially unchanged. It was popularised in the 1960s  
# with the release of Letraset sheets containing Lorem Ipsum passages, and more  
# recently with desktop publishing software like Aldus PageMaker including  
# versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and  
# typesetting industry. Lorem Ipsum has been the industry's standard dummy text  
# ever since the 1500s, when an unknown printer took a galley of type and  
# scrambled it to make a type specimen book. It has survived not only five  
# centuries, but also the leap into electronic typesetting, remaining essentially  
# unchanged. It was popularised in the 1960s with the release of Letraset sheets  
# containing Lorem Ipsum passages, and more recently with desktop publishing  
# software like Aldus PageMaker including versions of Lorem Ipsum.
</code></pre>
