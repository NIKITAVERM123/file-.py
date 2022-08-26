# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:

# Code Example
# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
a=open("flie question3 .txt","a")
s=["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"]
k=a.writelines(s)
print(k)