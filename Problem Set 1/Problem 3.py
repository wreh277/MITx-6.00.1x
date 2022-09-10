z="abcdefghijklmnopqrstuvwxyz"
orden0=0
orden1=0
palabra0=""
palabra1=""

for i in range(0,len(s)):
    for j in range(0,len(z)):
        if z[j]==s[i]:
            orden1=j
            print(orden1)
           
    if orden1>=orden0:
        orden0=orden1 
        palabra1+=s[i]
        if len(palabra1)>len(palabra0):
            palabra0=palabra1
            print(palabra0)
    else:
        orden0=orden1
        palabra1=s[i]
print("Longest substring in alphabetical order is:",palabra0)


#otro enfoque mas limpio utilizando la propiedad de los strings:
s="alfjljabc"
letra=s[0]
letra1=s[0]
for i in range(len(s)-1):
    print("letra   "+letra)
    print(letra1)
    if s[i+1]>=s[i]:
        letra1+=s[i+1]
        if len(letra1)>len(letra):
            letra=letra1
            print("yes")
    else:
        letra1=s[i+1]
print(letra)

#ambos dan lo mismo
