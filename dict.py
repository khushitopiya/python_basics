#dict()
d = dict(name="khushi", age=21)
print(d)  

d = dict([("name", "khushi"), ("age", 21)])
print(d)  




#clear()
d = {"a": 1, "b": 2}
d.clear()
print(d)  




#copy()
d = {"a": 1, "b": 2}
copy_d = d.copy()
print(copy_d)  




#fromkeys
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)  




#get
d = {"a": 1, "b": 2}
print(d.get("a"))         
print(d.get("c", "None")) 




#items
d = {"a": 1, "b": 2}
print(d.items()) 





#keys()
d = {"a": 1, "b": 2}
print(d.keys())  




#values()
d = {"a": 1, "b": 2}
print(d.keys())  




#pop()
d = {"a": 1, "b": 2}
print(d.pop("a"))        
print(d.pop("c", "None")) 




#pop itam()
d = {"a": 1, "b": 2}
print(d.popitem())  
print(d)            





#set defult()
d = {"a": 1, "b": 2}
print(d.popitem())  
print(d)            




#update()
d = {"a": 1}
d.update({"b": 2, "c": 3})
print(d) 



# Using a list of tuples
d.update([("d", 4)])
print(d)  




#len()
d = {"a": 1, "b": 2}
print(len(d))  




#del statement()
d = {"a": 1, "b": 2}
del d["a"]  
print(d)    
del d  




#in operator()
d = {"a": 1, "b": 2}
print("a" in d)  
print("c" in d)  



#intering 
d = {"a": 1, "b": 2}



# Iterating over keys
for key in d:
    print(key) 



# Iterating over values
for value in d.values():
    print(value)  

    

# Iterating over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")  
