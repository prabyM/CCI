import re
# The patern of number to be searched is like 878-898-7656

st = "My name is Prabhakar and my contact number is 790-387-4985. I can also be contacted on 875-191-6801 or 870-562-1682. 790-387-4985 should be my primary contact."
result = re.findall(r'[1-9]\d{2}-\d{3}-\d{4}',st)
count_dict = {}
for retrieved_numbers in result:
    if retrieved_numbers not in count_dict:
        count_dict[retrieved_numbers] = 1
    else:
        count_dict[retrieved_numbers] = count_dict[retrieved_numbers] + 1

most_freq_number = max(count_dict, key=count_dict.get)
print(most_freq_number)
