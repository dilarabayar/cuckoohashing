# Cuckoo Hashing Visualization 

In order to run the program, it will be enough for the user to enter only the inputs desired by the program.

**Some Explanations:**

If inputs such as how many tables will exist or the size of each table are entered incorrectly,
the user will be asked to enter the input again. After each of the operation, current situation of each table will be shown to user. For character/string type keys ASCII code is used to place key in a table.

**"-"** symbol shows that related index in table is empty.

**Search:** key element x is will be searched in all of the tables until it's found. If it's not found in any of the table
warning will be appear.

**Deletion:** Search method used to find key x element and if it's exist it will be deleted immediately. After deletion load factor
of tables will be shown to user.

**Insertion:** There are 4 possible scenarios. First one is key is already exist. Insertion will be failed and location of key,
current tables and their loadfactor will be shown to user. Second one is key is not exist and  T1[h1(x)] is empty. Key will be
inserted and location of new key, current tables and their loadfactor will be shown to user. Third one is collision is occured in
T1[h1(x)] but in any of the other tables empty index is found. Key x will be put to T1[h1(x)] and the key y is in T1[h1(x)] will be 
put to T2[h2(y)] if other collision occurs as well this process will iterate until there is some place found which is empty in any 
of the tables. New location of each key and where is the collision occured, total number of collisions occured, load factor of each
table and current situation of all tables will be shown to user. Fourth scenario is similar to third one but if any key is trying 
to be placed to its previous index, the cycle has occurred. Additional to third scenario outputs, it will
be shown that the cycle is occured.

There can be a maximum of 5 tables in the entire program, and all of them have different key insertion principle.

**Table 1 insertion h1(x):** index of key = key % tablesize\
**Table 2 insertion h2(x):** index of key = (key / tablesize) % tablesize\
**Table 3 insertion h3(x):** index of key = (key * 2) % tablesize\
**Table 4 insertion h4(x):** index of key = (key * 3) % tablesize\
**Table 5 insertion h5(x):** index of key = (key + 7) % tablesize

