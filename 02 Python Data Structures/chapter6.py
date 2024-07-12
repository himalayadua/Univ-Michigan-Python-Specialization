# Parsing and Extracting domain name from email address from strings

data = "From GoodTo.Great@waterman.com Sat Jul 12 2024 3:30:16 AM"

atpos = data.find("@")

sppos = data.find(' ', atpos)

domainname = data[atpos+1 : sppos]

print(domainname)
# waterman.com