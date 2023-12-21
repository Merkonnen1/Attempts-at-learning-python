import matplotlib.pyplot as plt

DATA_FILE = 'earth-orbit-objects.csv'
Header = []
List = []

with open(DATA_FILE) as data_file:
    lines = data_file.readline()
    Header.append(lines.strip().split(","))
    for _ in range(442):
        lines = data_file.readline()
        List.append(lines.strip().split(","))

dictionary = {
    Header[0][0]: [],
    Header[0][1]: [],
    Header[0][2]: []
}

for n in range(len(List)):
    dictionary[Header[0][0]].append(List[n][0])
    dictionary[Header[0][1]].append(float(List[n][1]))  # Convert to float for plotting
    dictionary[Header[0][2]].append(float(List[n][2]))  # Convert to float for plotting

n = 0
count = 1

while n < 442:
    Store = dictionary[Header[0][0]][n]
    x = []
    y = []

    while n < 442 and dictionary[Header[0][0]][n] == Store:
        x.append(dictionary[Header[0][1]][n])
        y.append(dictionary[Header[0][2]][n])
        n += 1
    if count>6:
        break
    plt.subplot(2, 3, count)
    plt.plot(x, y)
    count += 1
    plt.grid(True)

plt.suptitle(str(List[0][0]))
plt.ylabel(Header[0][2])
plt.xlabel(Header[0][1])
plt.show()