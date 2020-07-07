# Assumption that all dicts in list have same set of keys
def remove_duplicate_dicts(dict_list):
	# Check if one dict is equal to some other dict is yes then add to final ans
	# Since we do forward check duplicates won't get added
	return [dictionary for idx, dictionary in enumerate(dict_list) if dictionary not in dict_list[idx + 1:]] 

if __name__ == '__main__':
	dict_list=[
		{'name': 'affirm', 'confidence': 0.9448149204254}, 
		{'name': 'affirm', 'confidence': 0.944814920425415}, 
		{'name': 'inform', 'confidence': 0.9842240810394287}, 
		{'name': 'inform', 'confidence': 0.9842240810394287}
	]
	print(remove_duplicate_dicts(dict_list))