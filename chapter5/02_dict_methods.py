marks = {
        "ayush":368, 
         "jay":370,
         "sohan":300,
         0:"rohan"
         }
# print(marks,type(marks))

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"ayush":370,"mukesh":330})
# print(marks)

print(marks.get("ayush2")) # prints none
print(marks["ayush2"]) # returns an error