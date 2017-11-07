# Coding Style
* Should follow dependency injection (DI) design pattern using snake-guice where appropriate (e.g., DAOs, Factories, etc.) (see https://github.com/google/guice/wiki/GettingStarted (good introduction to Guice and DI in general, but the Java implementation (snake-guice docs are weak but extremely similar to regular Guice for Java))
* All files must have interfaces (unless they are implementation files)
* Only one class per file
* Class name and file name should be the same
* Class name should start with "AMZN<name-of-file>.py" (e.g., AMZNCamelScraper.py)
* All files should have the following block comment, with one author per class/file:
```
"""
	Amazon Discount Finder. All rights reserved.
	Author: <author-name>
"""
```
* Tabs are 4 spaces
* Supplemental documents for developers should be Markdown (see https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html)
* Method names are separated by underscores (e.g. camel_scraper)
* CamelCase variables only (e.g., camelScraper)
* Only check in working code (flexible given a few exceptions)
* Try to prevent any one method from taking up an entire screenlength
* There should be a comment on top of file explaining gist of what is in file and there should be a comment for each global variable if any about what it is for.
* Block comments right above all classes, parameters, methods, variables, etc (see conventions for pydocs -- very similar to javadocs)
* All imports should be on their own line, organized by library/framework (e.g., `import os, sys` => wrong)
* No single letter variable names unless it is an index.
* Do not terminate a line with semicolons.
* 80 character ruler.
* If you find a bug or something unimplemented, put a `#TODO` to it, explaining what needs to be implemented/done.
