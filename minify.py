import copy

file_name = raw_input('Enter file name: ')

t1 = open(file_name,'r')
file_name = file_name.split('.')
file_name_alias = copy.deepcopy(file_name)

file_name.insert(1, '.min.')
output_file_name = ''.join(file_name) 
t2 = open(output_file_name,'w')

content = t1.read()

# string -> list
content = content.split()

tags = ['h1','h2','h3','h4','h5','h6','body','html','section','div','p','header','footer','span','a','img','canvas','hr','form','input','textarea','nav','figure','article']

def css(words):

	words_copy = copy.deepcopy(words)

	for i in range(len(words_copy)):

		# add whitespace for multiple identifiers
		# for tags
		if ((words[i] in tags and words[i+1] != '{') or (words[i][:-1] in tags and words[i][-1] != '{')):
			words[i] = words[i] + chr(32)

		# identifiers with '#','.','@' and '-' initials
		if (words[i][0] == '#' and words[i-1][-6:] != 'color') or (words[i][0] == '.' and words[i][-1] != ';') or words[i][0] == '@' or (words[i][0] == '-' and words[i][-1] != ';'):
			if words[i-1][-1] == ':':
				pass
			else:
				if words[i][-1] == '{':
					pass
				elif words[i+1] != '{':
					words[i] = words[i] + chr(32)


		# add whitespace in properties with multiple declarations like text-shadow, margin etc.
		if words[i][-1] == ':' and words[i+2][-1] != '}':
			num_values = 0
			for j in range(i, len(words)):
				if words[j][-1] == ';':
					break
				else:
					num_values += 1
			index = i
			for k in range(num_values-1):
				index += 1
				words[index] = words[index] + chr(32)


		# remove semicolon from last property 
		if words[i][-1] == ';':
			if words[i+1][-1] == '}':
				words[i] = words[i][:-1]
			else:
				pass


		# add whitespace to 'and'
		if words[i] == 'and':
			words[i] = chr(32) + words[i] + chr(32)


		# remove free whitespace
		whitespace = ['',' ','\n','\t']
		if (words[i] == '{' and words[i-1][-1] in whitespace) or (words[i] == '}' and words[i-1][-1] in whitespace):
			words[i-1] = words[i-1][:-1]
		if (words[i][-1] == chr(32) and words[i][-2] == ';') or (words[i][-1] == chr(32) and words[i][-2] == ','):
			words[i] = words[i][:-1]
		if (len(words[i]) == 2 and words[i][0] == '{' and words[i][1] == chr(32)) or (len(words[i]) == 2 and words[i][0] == '}' and words[i][1] == chr(32)):
			words[i] = words[i][:1]
		if (words[i][-1] == chr(32) and words[i][-2] == ':'):
			words[i] == words[i][:-1]
		if (words[i][-1] == chr(32) and words[i][-2] == ':'):
			words[i] == words[i][:-1]
		if words[i][0] == '{' and words[i-1][-1] == chr(32):
			words[i-1] = words[i-1][:-1]


	# list -> string
	words = ''.join(words)

	t2.write(words)

	t1.close()
	t2.close()

if (file_name_alias[-1] == 'css'):
	css(content)
else:
	print "This script only works for css files"

