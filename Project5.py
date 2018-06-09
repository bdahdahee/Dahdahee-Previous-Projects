

# Function takes a string as a parameter and returns True if the string is a palindrome, False otherwise

def isPalindrome(text):
	Alph = "abcdefghijklmnopqrstuvwxyz"
	new_string=""
	if type(text) != str:
		return False
	text = text.lower()
	for char in text:
		if char in Alph:
			new_string += char
	rev = new_string[::-1]
	if (new_string == rev):
		return True
	return False 