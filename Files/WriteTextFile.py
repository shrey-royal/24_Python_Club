file_name = input("Enter fileName: ") + ".txt"

# with open(file_name, 'w') as file:
#     # data = "This is data.\nThis is data in next line"
#     data = input(f"Enter the data you want to write into {file_name}: ")
#     file.write(data)


with open(file_name, 'w') as file:
    n = int(input("Enter n: "))
    for i in range(1, 11):
        file.write(f"{n} x {i} = {n*i}\n")


# read this multiplication table