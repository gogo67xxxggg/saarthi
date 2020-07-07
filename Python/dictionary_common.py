def common_dictionary(dict1=None, dict2=None):

	# Check for empty dicts
	if not dict1:
		return dict2
	if not dict2:
		return dict1 
	if not dict1 and not dict2:
		return None 

	# Add keys of both dict 1 and 2 to final dict
	final_dict = dict(dict1)
	final_dict.update(dict2)

	# if keys equal add values
	for k1, v1 in dict1.items():
		for k2, v2 in dict2.items():
			if k1 == k2:
				final_dict[k1] = v1+v2
	return final_dict

if __name__ == '__main__':
	d1 = {'a': 100, 'b': 200, 'c':300}
	d2 = {'a': 300, 'b': 200, 'd':400}
	print(common_dictionary(d1,d2))