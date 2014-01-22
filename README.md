## About
StringToComment allows you to highlight a string and convert it into an 80-char delimited block comment in the language currently set in the view.

## Features
* Converts highlighted text into a comment block.
* Uses currently set language to determine comment syntax.
* Trims leading space and ensures all lines have no trailing spaces.
  - *TODO*: Add leading space as a pad for each new-line to preserve initial position.

## Author's Note
I wrote this plugin because I found myself manually (or with a basic macro) turning a sentence/description into a nicely formatted comment to add above a snippet of code way too often.

## Installation
Install StringToComment through [Package Control](https://sublime.wbond.net/) or download and extract it into your Sublime Text `Packages` folder.

## Usage
* Default binding: <kbd>Ctrl+Shift+c</kbd> + <kbd>Ctrl+c</kbd> 
* Highlight text <kbd>></kbd> right-click <kbd>></kbd> choose <kbd>String to Comment</kbd>