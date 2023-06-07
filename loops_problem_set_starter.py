
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)

# Write a while loop that does the same thing!
print("*" * 50)

i = 0

while i < len(word):
    print(word[i])
    i += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
print("*" * 50)

num = 100

while num <= 140:
    print(num)
    num += 2



# Write a for loop that does the same thing (with range())
print("*" * 50)

for num in range(100, 141, 2):
    print(num)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
print("*" * 50)

passphrase = ""

while not passphrase:
    entry = input("type in 'sillygoose':  ")
    if entry == "sillygoose":
        passphrase = entry