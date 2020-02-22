print("name")
prog = { 'charan': 'hyg', 'vm1': ['java', 'java', 'kli'], 'vm2': {'NAME': 'cha', 'NAME2': 'juh', 'Status': 'active'}}
print(prog['vm1'])
print(prog['vm2'])
print("before" , prog['vm2'])
prog['vm2']['NAME']='reddy'
print("after" , prog['vm2'])
print(prog.get('vm2'))
print("before", prog)
del prog['vm2']['NAME']
print("after", prog)
