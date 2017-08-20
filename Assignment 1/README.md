Here goes your first assignment. Happy coding!
What you could learn because of this assignment? - Basic text preprocessing with python
--> What we want to do is to transform text from a text file into a format that is easier to deal with. You are provided with a file containing some text like this:
"This is our 1st assignment for the ACA course project, and I think it is going to be a lot of #fun."
You have to convert this into a stream of tokens (a Python list), not containing any special characters, all in lowercase. So your output could be something like this:
['this', 'is', 'our', '1st', 'assignment', 'for', 'the', 'aca', 'project', 'and', 'i', 'think', 'it', 'is', 'going', 'to', 'be', 'a', 'lot', 'of', 'fun']
So go ahead and solve this! Look down only if you have no clue how to go about it, or get stuck at some point. Look straight at the last line otherwise.  


Your job is to:
1) Clean the text - for now, let's assume that we don't need commas, full stops or other characters that are not alphanumeric. Remove all of these, and replace them by spaces. Also, convert all the characters to lowercase. So, after this step, your text could look like this:
"this is our 1st assignment for the aca course project  and i think it is going to be a lot of fun " 
2) Now, split this into tokens based on the delimiter (<space> in our case)
Look below for hints only after you have searched the web long enough for tools that could help you achieve this. Please don't be lazy - Google has enough answers, if you have the right queries to make.  

1) For substituting all the non alphanumeric characters, you could look up the "re" library of python. Read up (in brief) about regular expressions from here: http://www.grymoire.com/Unix/Regular.html (don't take more than a few minutes - just get a hang of it, enough to get this task done. With re, this part should not take more than one line of code.
2) Try using primitive python functions - they will make your life very easy. (split, strip, upper etc.)
3) You'll have to use a couple of simple file handling operations like open and read.
Last line: Now where is the text file with some text like the sentences used as our example, which you have to use in your task?
It is this text file itself.
--x--
