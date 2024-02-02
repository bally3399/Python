def ascending_order(sample_list):

	for idx in range(len(sample_list)):
		for idx1 in range(idx + 1, len(sample_list)):
			if sample_list[idx] > sample_list[idx1]:
				temp = sample_list[idx]
				sample_list[idx] = sample_list[idx1]
				sample_list[idx1] = temp
	return sample_list
sample_list = [10, 2, 8, 9, 3, 4, 1, 5]

print(ascending_order(sample_list))

def descending_order(sample_list):

	for idx in range(len(sample_list)):
		for idx1 in range(idx + 1, len(sample_list)):
			if sample_list[idx] < sample_list[idx1]:
				temp = sample_list[idx]
				sample_list[idx] = sample_list[idx1]
				sample_list[idx1] = temp
	return sample_list
sample_list = [10, 2, 8, 9, 3, 4, 1, 5]

print(descending_order(sample_list))



