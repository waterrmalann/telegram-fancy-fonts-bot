"""
	A python module that allows you to create and play with psuedofonts.
	
	Psuedofonts are text styles made using unicode special characters.
	These can be rendered anywhere with UTF-8 support.
	Example: 𝓗𝓮𝓵𝓵𝓸 𝓦𝓸𝓻𝓵𝓭

	Usage: 
	my_custom_font = PseudoFont('L33TSP34K', '@6cdef9h!jk1mnopqr5+uvwxy2', '48(D3FG#|JK1MN0PQR$7UVWXY2', '')
	sample = my_custom_font("The Quick Brown Fox Jumps Over The Lazy Dog")
	
	sample -> '7he Qu!ck 8rown Fox Jump5 0ver 7he 1@2y Do9'

	I do realize that str.translate() could be used for the same purpose but I wrote my own implementation for the ease of use + more flexibility as I will be adding more to it in the future.
"""

class PseudoFont:

	def __init__(self, font_name: str, font_lower: str, font_upper: str, font_digits: str):
		# The name of the defined font style.
		self.name = font_name
		
		# Custom unicode characters to translate to.
		self.font_name = font_name
		self.font_lower = font_lower
		self.font_upper = font_upper
		self.font_digits = font_digits

		# Characters used as reference to translate from. (normal english alphabets as default)
		# Note: Make sure length of reference and custom fonts are always equal.
		# Change this only if you are changing the font assignment pattern or language.
		self.reference_lower = 'abcdefghijklmnopqrstuvwxyz'
		self.reference_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.reference_digits = '0123456789' 

	def __call__(self, text: str, inversion: bool = False) -> str:
		return self.convert(text) if not inversion else self.inverted_convert(text)
	
	def __repr__(self) -> str:
		return f"Psuedo-Font: {self.name} ({self.convert('The Quick Brown Fox Jumps Over The Lazy Dog')}"
	
	def __str__(self) -> str:
		return self.convert(self.name)
	
	def __len__(self) -> str:
		return len(self.font_lower)  # len(Font) = length of lowercase characters
	
	def convert(self, raw_text: str) -> str:
		"""Convert normal text to styled text."""

		t_converted = []
		for char in raw_text:
			if char in self.reference_lower:  # if character is lowercase
				t_converted.append(self.font_lower[self.reference_lower.find(char)])

			elif char in self.reference_upper:  # if char is uppercase
				t_converted.append(self.font_upper[self.reference_upper.find(char)])

			elif char in self.reference_digits:  # if char is digit
				t_converted.append(self.font_digits[self.reference_digits.find(char)])
			
			else:
				t_converted.append(char)
		
		return ''.join(t_converted)
	
	def inverted_convert(self, raw_text: str) -> str:
		"""Convert styled text back to normal text. (unused)"""

		t_converted = []
		for char in raw_text:
			if char in self.font_lower:  # if character is lowercase
				t_converted.append(self.reference_lower[self.font_lower.find(char)])

			elif char in self.font_upper:  # if char is uppercase
				t_converted.append(self.reference_upper[self.font_upper.find(char)])
			
			elif char in self.font_digits:  # if char is digit
				t_converted.append(self.reference_digits[self.font_digits.find(char)])
			
			else:
				t_converted.append(char)
		
		return ''.join(t_converted)