# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result)) # 2526302776944
print(id(another_result)) # 2526302776944

result += "ish"
print(id(result)) # 2526302781616
print(id(another_result)) # 2526302776944
