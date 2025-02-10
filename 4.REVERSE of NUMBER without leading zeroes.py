def reverseDigits(self, n):
		reversed=str(n)[::-1]
		return int(reversed.lstrip('0'))
