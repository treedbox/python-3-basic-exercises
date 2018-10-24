import urllib2

try:
    x = urllib2.urlopen('https://pythonprogramming.net').read()

    print(x)

except Exception, e:
    print str(e)

"""
run in a Terminal:
2to3 python2-example.py
to see the changes between 2 and 3 in your file
or

2to3 -w python2-example.py
to write the code translation to your file

on/python.1.0.0/converter/python2-to-3/python2-example.py
RefactoringTool: Skipping optional fixer: buffer
RefactoringTool: Skipping optional fixer: idioms
RefactoringTool: Skipping optional fixer: set_literal
RefactoringTool: Skipping optional fixer: ws_comma
RefactoringTool: Refactored python2-example.py
--- python2-example.py	(original)
+++ python2-example.py	(refactored)
@@ -1,12 +1,12 @@
-import urllib2
+import urllib.request, urllib.error, urllib.parse

 try:
-	x = urllib2.urlopen('https://pythonprogramming.net').read()
+	x = urllib.request.urlopen('https://pythonprogramming.net').read()

 	print(x)

-except Exception, e:
-	print str(e)
+except Exception as e:
+	print(str(e))

"""
