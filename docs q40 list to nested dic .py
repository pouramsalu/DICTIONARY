# write a python program to convert more than one list to nested dictionary
a=["s001","s002","s003","s004"]
b=["adina park","leyton marsh","ducan boyle","saim richards"]
c=[85,98,89,92]
x=[{'key':b} for key_value in zip(b,c)]
y=[{'key':a} for key_value in zip(a,x)]
print(y+x)