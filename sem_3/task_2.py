# Данна последовательность из N целых чисел и число K ,
# Необходимо сдвинуть всю последовательность (сдвиг циклический)
# на K элементов вправо, K - положительное число.
# staert_list = [1, 2, 3, 4, 5]
# k = 3
# --> [3, 4, 5, 1, 2]


#staert_list = [1, 2, 3, 4, 5]
#print(staert_list)
#num = 2
#k = num%len(staert_list)
#staert_list_temp = [0]*len(staert_list)
#for i in range(len(staert_list)):
#    if (i + k) >= len(staert_list):
#        staert_list_temp[(i + k) - len(staert_list)] = staert_list[i]
#    else:
#        staert_list_temp[(i + k)] = staert_list[i]
#print(staert_list_temp)

k = 2
staert_list = [1, 2, 3, 4, 5]
print(staert_list)
new_list = []

k = -(k%len(staert_list))
for i in staert_list:
    new_list.append(staert_list[k])
    k += 1
print(new_list)