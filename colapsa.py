#UFCG - P1
#João Matheus Pinto Villarim Coutinho de Almeida
#Colapsa N menores
def colapsa_n_menores(n, nums):
	oldnums = nums
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]
	counter = 0
	for i in range(n):
		counter += nums[i]
		for j in range(len(oldnums)):
			if oldnums[j] == nums[i]:
				oldnums.pop(j)
	oldnums.append(counter)
	print(oldnums)