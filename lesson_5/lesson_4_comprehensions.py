import time
list_var = []

list_time = time.time()
for i in range(100):
    list_var.append(i)

list_final_time = time.time() - list_time


compr_list_time = time.time()
new_list_var = [i for i in range(100) if not i % 2]
compr_final_time = time.time() - compr_list_time

print(list_final_time > compr_final_time)
# Добавить i в список, если делится на 2 на цело в
# диапазоне в range(100)



our_dict = dict(
    key1="value1",
    key2="value2",
    key3="value1"
)

new_dict = {key: value for key, value in our_dict.items() if value == "value1"}
print(new_dict)