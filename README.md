# Basics Required For Web Scrapping Using Beautiful Soup

It contains 6 topics which will give you all the basic knowledge that you should know before starting web scrapping through Beautiful Soup.

1. EXCEL READ AND WRITE
This will tell you about how to read and write in Microsoft Excel.

2. INTRO TO BEAUTIFUL SOUP
This will tell how to read HTML code (tags like- head, title, body) using beautiful soup and also navigation of string.

3. INTRO TO REQUEST
In this, you will get to know about some libraries like fake agent(how to use Mozilla browser as your user agent) and how to know whether you request to website accepted (using status command) and how to make a request from a website for web scrapping.

4.  NAVIGATING BS4 SOUP
Basically, there are three ways of navigating in HTML code
a.  Going Down      - from parents to child
b.  Going Up        - from child to parents
c.  Going Sideways  - reaching to siblings of one parent

5. REGEX
It is quite difficult to use above commands for we big websites using many HTML tags so here come regular expressions to make this work easy.
Some of regular expressions are :
a. +     - counts from 1 to infinity
b. *     - counts from 0 to infinity
c. {m,n} - setting particular range for repeating characters matching

6. SEARCHING PARSE TREE - USING BS4
Now you have learned regex then the question arises how to you will find that particular type of string in the whole HTML code.
Here, comes in action find function. It is of two types:
a. find     - it finds only single object
b. find_all - it finds multiple objects