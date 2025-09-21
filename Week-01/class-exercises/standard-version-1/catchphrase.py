def print_catchphrase(character):
	if character == "Winnie the Pooh":
		print("Oh, bother!")
	elif character == "Tigger":
		print("TTFN: Ta-ta for now!")
	elif character == "Eeyore":
		print("Thanks for noticing me.")
	elif character == "Christopher Robin":
		print("Silly old bear.")
	else:
		print("Sorry, I don't know " + character + "'s catchphrase.")
		
print_catchphrase("Winnie the Pooh")  # Output: Oh, bother!
print_catchphrase("Tigger")  # Output: TTFN: Ta-ta for
print_catchphrase("Eeyore")  # Output: Thanks for noticing me.
print_catchphrase("Christopher Robin")  # Output: Silly old bear.
print_catchphrase("Piglet")  # Output: Sorry, I don't know Piglet
