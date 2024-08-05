'''
message = '"Beautiful is better than ugly.", this is the message'
message = "\"Beautiful is better than ugly.\", this is the message"

print(message)
'''

# slicing 
'''
Slicing is a powerful feature in Python that allows you to access parts of sequences like lists, tuples, and strings. It enables you to create a new sub-sequence from an existing sequence. The basic concept of slicing involves specifying a start, stop, and step value. The general syntax for slicing is:

sequence[start:stop:step]

-> Start: The index at which the slice starts (inclusive). If omitted, the slice starts from the beginning of the sequence.
-> Stop: The index at which the slice ends (exclusive). If omitted, the slice goes to the end of the sequence.
-> Step: The interval between elements in the slice. If omitted, the default step is 1.


'''

message = "Artificial Intelligence"

# print(message[11:16])
# print(message[11:])
# print(message[:16])
print(message[1::2]) # this will skip 1 character (step-1)

"""
Tasks:

1. Extract the first 5 characters of the string "Hello, World!"
    s = "Hello, World!"

2. Get the last 4 characters of the string "Python Programming"
    s = "Python Programming"

3. Retrieve the substring "thon" from the string "Python"
    s = "Python"

4. Extract every second character from the string "abcdefg"
    s = "abcdefg"

5. Get the substring "gram" from the string "Programming" using negative indices
    s = "Programming"

6. Retrieve the first half of the string "DataScience" (assuming the length is even)
    s = "DataScience"

7. Get the second half of the string "Artificial" (assuming the length is even)
    s = "Artificial"

8. Extract the substring "Sci" from the string "DataScience"
    s = "DataScience"

9. Get the substring "World" from the string "Hello, World!" using both positive and negative indices
    s = "Hello, World!"

10. Retrieve the entire string "Example" in reverse order
    s = "Example"

"""