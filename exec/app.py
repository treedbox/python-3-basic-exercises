exec("print('Print from exec')")

list_srt = "[5, 6, 7, 8]"
exec_list_srt = exec(list_srt)
print(exec_list_srt)
# None (don't work)

exec("list_srt2 = " + list_srt)
print(list_srt2)
# [5, 6, 7, 8]

exec("def foo(): print('Print from function')")
foo()
# Print from function


exec("""
def bar():
	print("Prinf from a multiline executed function")
	""")

bar()
# Prinf from a multiline executed function
