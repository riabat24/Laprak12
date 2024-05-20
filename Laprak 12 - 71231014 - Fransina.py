#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#soal 1

Finance =  {'RTI Saham', 'Mirae', 'IPOT', 'Poems', 'Calculator'}
Utilities =  {'Photos', 'Weather', 'Calculator', 'Camera', 'Notes'}

a = Finance ^ Utilities
print("Nama-nama aplikasi yang muncul di satu kategori: ", a)

b = Finance & Utilities
print("Nama-nama aplikasi yang muncul dua kali: ", b)


# In[ ]:


#soal 2

data = "Januari Februari Maret April Mei Juni "
bulan = data.split()
print()

list_set = set(bulan)
print("Konversi List menjadi Set")
print("Sebelum Konversi: ", bulan)
print("Sesudah Konversi: ", list_set)
print()

x = set(bulan)
set_list = list(x)
print("Konversi Set menjadi List")
print("Sebelum Konversi: ", x)
print("Sesudah Konversi : ", set_list)
print()

a = tuple(bulan)
tuple_Set = set(a)
print("Konversi Tuple menjadi Set")
print("Sebelum Konversi: ", a)
print("Sesudah Konversi: ", tuple_Set)
print()

b = set(bulan)
set_tuple = tuple(b)
print("Kpnversi Tuple menjadi Set")
print("Sebelum Konversi: ", b)
print("Sesudah Konversi: ", set_tuple)


# In[ ]:


#soal 3

file1 = input("Masukkan nama file 1 : ")
try:
    a = open(file1, 'r')
except: 
    print("File yang anda masukkan tidak ada: ", a)
    exit()

file2 = input("Masukkan nama file 2 : ")
try:
    b = open(file2, 'r')
except: 
    print("File yang anda masukkan tidak ada: ", b)
    exit()

a = a.read()
b = b.read()

x = a.lower()
y = b.lower()

ubh_split = x.split()
ubh_split1 = y.split()

ubh_set1 = set(ubh_split)
ubh_set2 = set(ubh_split1)

print()
kata_sama = ubh_set1 & ubh_set2
print(kata_sama)

