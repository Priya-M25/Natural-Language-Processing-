import re

sent = ' this is my sentence that starts and ends with whitespace '
pattern = re.compile('^\s|\s$')
sent = pattern.sub('', sent)
print(sent)

sent = "   This    is   an   example   text   with  extra   whitespace.   "
sent = sent.split(' ')
sent = [word for word in sent if word]
sent = ' '.join(sent)
print(sent)
