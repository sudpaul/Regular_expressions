 Regex Cheat Sheet — PyCon 2016 Regex Tutorial    
 
 [Regular Expressions Tutorial](https://pycon2016.regex.training/)


*   [Regex Cheat Sheet](https://pycon2016.regex.training/cheat-sheet#)
    *   [Regex Syntax](https://pycon2016.regex.training/cheat-sheet#regex-syntax)
    *   [Python](https://pycon2016.regex.training/cheat-sheet#python)
*   [Exercises](https://pycon2016.regex.training/exercises)
*   [The Basics](https://pycon2016.regex.training/regex-intro)
*   [Regular Expressions Module](https://pycon2016.regex.training/re-module)
*   [Advanced Features](https://pycon2016.regex.training/more-re-module)
*   [Substitutions](https://pycon2016.regex.training/substitutions)



[Regular Expressions Tutorial](https://pycon2016.regex.training/)

Regex Cheat Sheet[¶](https://pycon2016.regex.training/cheat-sheet#regex-cheat-sheet "Permalink to this headline")
=================================================================================================================

Regex Syntax[¶](https://pycon2016.regex.training/cheat-sheet#regex-syntax "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

Characters[¶](https://pycon2016.regex.training/cheat-sheet#id1 "Permalink to this table")  

Character

Matches

`a`

`a` character

`.`

Any character (except newline)

`\.`

`.` character

`\\`

`\` character

`\*`

`*` character

Character Classes[¶](https://pycon2016.regex.training/cheat-sheet#id2 "Permalink to this table")  

 

Matches

Description

`[abcd]`

Any one of the letters `a` through `d`

Set of characters

`[^abcd]`

Any character but `a`, `b`, `c`, or `d`

Complement of a set of characters

`[a-d]`

Any one of the letters `a` through `d`

Range of characters

`[a-dz]`

Any of `a`, `b`, `c`, `d`, or `z`

Range of characters

Special Sequences[¶](https://pycon2016.regex.training/cheat-sheet#id3 "Permalink to this table")  

Type

Expression

Equivalent To

Description

Word Character

`\w`

`[a-zA-Z0-9_]`

Alphanumeric or underscore

Non-word Character

`\W`

`[^a-zA-Z0-9_]`

Anything but a word character

Digit Character

`\d`

`[0-9]`

Numeric

Non-digit Character

`\D`

`[^0-9]`

Non-numeric

Whitespace Character

`\s`

`[ \t\n\r\f\v]`

Whitespace

Non-whitespace Character

`\S`

`[^ \t\n\r\f\v]`

Anything but a whitespace character

Anchors[¶](https://pycon2016.regex.training/cheat-sheet#id4 "Permalink to this table")  

Anchor

Matches

`^`

Start of the string

`$`

End of the string

`\b`

Boundary between word and non-word characters

Groups[¶](https://pycon2016.regex.training/cheat-sheet#id5 "Permalink to this table")  

Group Type

Expression

Capturing

`(` ... `)`

Non-capturing

`(?:` ... `)`

Quantifiers/Repetition[¶](https://pycon2016.regex.training/cheat-sheet#id6 "Permalink to this table")  

Quantifier

Modification

`{5}`

Match expression exactly 5 times

`{2,5}`

Match expression 2 to 5 times

`{2,}`

Match expression 2 or more times

`{,5}`

Match expression 0 to 5 times

`*`

Match expression 0 or more times

`{,}`

Match expression 0 or more times

`?`

Match expression 0 or 1 times

`{0,1}`

Match expression 0 or 1 times

`+`

Match expression 1 or more times

`{1,}`

Match expression 1 or more times

Non-greedy quantifiers[¶](https://pycon2016.regex.training/cheat-sheet#id7 "Permalink to this table")  

Quantifier

Modification

`{2,5}?`

Match 2 to 5 times (less preferred)

`{2,}?`

Match 2 or more times (less preferred)

`{,5}?`

Match 0 to 5 times (less preferred)

`*?`

Match 0 or more times (less preferred)

`{,}?`

Match 0 or more times (less preferred)

`??`

Match 0 or 1 times (less preferred)

`{0,1}?`

Match 0 or 1 times (less preferred)

`+?`

Match 1 or more times (less preferred)

`{1,}?`

Match 1 or more times (less preferred)

Alternators[¶](https://pycon2016.regex.training/cheat-sheet#id8 "Permalink to this table")  

Quantifier

Modification

`ABC|DEF`

Match string `ABC` or string `DEF`

Lookaround[¶](https://pycon2016.regex.training/cheat-sheet#id9 "Permalink to this table")  

Quantifier

Modification

`(?=abc)`

Zero-width match confirming `abc` will match upcoming chars

`(?!abc)`

Zero-width match confirming `abc` will **not** match upcoming chars

Python[¶](https://pycon2016.regex.training/cheat-sheet#python "Permalink to this headline")
-------------------------------------------------------------------------------------------

functions[¶](https://pycon2016.regex.training/cheat-sheet#id10 "Permalink to this table")  

Function

Purpose

Usage

`re.search`

Return a match object if pattern found in string

`re.search(r'[pat]tern', 'string')`

`re.finditer`

Return an iterable of match objects (one for each match)

`re.finditer(r'[pat]tern', 'string')`

`re.findall`

Return a list of all matched strings (different when capture groups)

`re.findall(r'[pat]tern', 'string')`

`re.split`

Split string by regex delimeter & return string list

`re.split(r'[ -]', 'st-ri ng')`

`re.compile`

Compile a regular expression pattern for later use

`re.compile(r'[pat]tern')`

flags[¶](https://pycon2016.regex.training/cheat-sheet#id11 "Permalink to this table")  

Flag

Description

`re.IGNORECASE`

Match uppercase and lowercase characters interchangeably

`re.VERBOSE`

Ignore whitespace characters and allow `#` comments

[Next](https://pycon2016.regex.training/exercises "Exercises") [Previous](https://pycon2016.regex.training/ "PyCon 2016 Regular Expressions Tutorial")


