from itertools import permutations 

def generate_utterances(utterance_list, entity_list):

	final_utterances = []
	# generate all possible permuations of entities
	permutation = list(permutations(entity_list))

	for utterance in utterance_list:
		counter = utterance.count('_')
		utterance  = utterance.replace('_', '{}')
		# if replacements are only one then u can directly use from original list
		if counter == 1:
			tmp = utterance
			for enty in entities_list:
				tmp = tmp.format(enty)
				final_utterances.append(tmp)
				tmp = utterance
		else:
			tmp = utterance
			for perm in permutation:
				tmp = tmp.format(*perm[:counter])
				final_utterances.append(tmp)
				tmp = utterance
	return final_utterances


if __name__ == '__main__':
	entities_list = ["kolkata", "delhi", "mumbai"] 
	utterance_list=["How far is _ from _", "How is the weather in _?"]
	print(generate_utterances(utterance_list, entities_list))
