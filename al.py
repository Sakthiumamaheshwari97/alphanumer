ui=input()
for i in range(0,len(ui)):
   if(ui[i].isalpha() and ui[i].isdigit()):
       print("No")
   else:
       print("Yes")
