# hashmaps-python

Building a fixed-size hashmap that associates string keys with arbritatry data objects.

Functions available
----------------------
| Function                   | Return type |    Return
-----------------------------|-------------|--------------------------------------------------------|
| constructor (size)         | integer     |    pre-allocated space for the given number of objects |
| set (key,value)            | boolean     |    value indicating success / failure of the operation |
| get (key)                  | object      |    Value on success or None if the key has no value    |
| load ()                    | float       |    value representing the load factor                  |
| getCount ()                | integer     |    value of number of items in the hashmap             |
| printMap ()                | void        |    print hashmap items                                 |
