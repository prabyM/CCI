import re
st = "My name is Prabhakar and my contact number is 7903874985. I can also be contacted on 8751916801 or 8705621682. 7903874985 should be my primary contact."
result = re.findall(r'\d\d\d\d\d\d\d\d\d\d',st)
count_dict = {}
for retrieved_numbers in result:
    if retrieved_numbers not in count_dict:
        count_dict[retrieved_numbers] = 1
    else:
        count_dict[retrieved_numbers] = count_dict[retrieved_numbers] + 1

most_freq_number = max(count_dict, key=count_dict.get)
print("Most frequetly seen number is: %s" %most_freq_number)

