import json

from collections import defaultdict

words = defaultdict(int)
kill_chars = ['.', ',', '"', '\xe2', '\x80', '\x93', '\r', '\n', '\xa6']
death_words = ['\xe2\x80\x93']

with open('text.txt', 'r') as f:
	for line in f:
		if line != '\n':
			for word in line.split(' '):

				word = word.lower().strip()

				for death_word in death_words:
					if death_word in word:
						break

				for kill_char in kill_chars:
					word = word.replace(kill_char, '')

				word = word.decode('ascii')

				if word == '':
					break
				
				words[word] += 1

json_data = {'words': [], 'count': 0}
for item in sorted(words.items(), key=lambda word: word[1], reverse=True):
	item_dict = {}
	item_dict[item[0]] = item[1]
	json_data['words'].append(item_dict)
	json_data['count'] += 1

json_data = json.dumps(json_data)
with open('wc.json', 'w') as f:
	f.write(json_data) 