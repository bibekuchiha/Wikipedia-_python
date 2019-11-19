import wikipedia 
while True:
	input = raw_input("Q:")
	wikipedia.set_lang("EN")
	print wikipedia.summary(input,sentences=3)
