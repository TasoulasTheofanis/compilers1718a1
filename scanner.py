
def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the time is like 1st schedule separator 2nd schedule where sepator is the character ":" or the character "." 
# 1st schedule is a number from 00 to 24 and 2nd the character is a number from 00 to 59

td = { 'q0':{ '0':'q4','1':'q4','2':'q5', '3':'q1','4':'q1','5':'q1','6':'q1','7':'q1','8':'q1','9':'q1',}, #1st schedule number (first or second digit(if it's the second digit, this means that the first digit is 0, for example if the 1st schedule is 8, the 1st schedule is automaticallty 08 (8:54 and 08:54 is the same time)))
       'q1':{ ':':'q2','.':'q2' },                                                                          #now we split apart the 1st schedule from the 2nd schedule
       'q2':{ '0':'q3','1':'q3','2':'q3','3':'q3','4':'q3','5':'q3' },                                      #first digit of the number from 2nd schedule 
       'q3':{ '0':'q6','1':'q6','2':'q6','3':'q6','4':'q6','5':'q6','6':'q6','7':'q6','8':'q6','9':'q6' },  #second digit of the number from 2nd schedule
       'q4':{ '0':'q1','1':'q1','2':'q1','3':'q1','4':'q1','5':'q1','6':'q1','7':'q1','8':'q1','9':'q1','.':'q2',':':'q2' }, #second digit of the number from 1st schedule when the first digit is 1 or 0, we split apart the 1st schedule from the 2nd schedule
       'q5':{ '0':'q1','1':'q1','2':'q1','3':'q1','.':'q2',':':'q2' }, #second digit of the number from 1st schedule when the first digit is 2, or we split apart the 1st schedule from the 2nd schedule
     } 

# the dictionary of accepting states and their
# corresponding token

# 
ad = { 'q6':'TIME_TOKEN', #everything worked fine! YEAAAAAAAA!!!
	}


# get a string from input
text = input('give some input>')
# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print("token:",token,"string:",text[:position])
		print('unrecognized input at pos',position+1,'of',text)
		print('______________________________________________')
		break
	
	print("token:",token,"string:",text[:position])
	print('______________________________________________')
	
	# remaining text for next scan
	text = text[position:]

