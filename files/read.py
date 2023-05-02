


def readList():
# storing data from laptop.txt to a list
    laptop_list = []

    # indexing in the list
    sn = 1
    with open("laptop.txt", "r") as file:
        for line in file:
            laptops = line.split(",")

            for x in range(0, len(laptops)):
                # strips each word in the array of trailing whitespaces
                laptops[x] = laptops[x].strip()

            # append a dict of laptop in the list
            laptop_list.append(
                dict(
                    id=sn,
                    name=laptops[0],
                    manufacturer=laptops[1],
                    price=laptops[2],
                    quantity=int(laptops[3]),
                    cpu=laptops[4],
                    gpu=laptops[5]
                )
            )
            sn += 1