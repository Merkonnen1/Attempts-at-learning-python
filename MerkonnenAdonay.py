import matplotlib.pyplot as plt

def plot_user_choice(data_file, num_subplots=7):
    Header = []
    List = []

    with open(data_file) as data_file:
        lines = data_file.readline() #read a line in the file
        Header.append(lines.strip().split(",")) #Get the first line in the file splits in the comma and strip removes the new line
        for _ in range(442): #The amount of lines in the file is 443 as I skipped the header I did 442
            lines = data_file.readline()
            List.append(lines.strip().split(",")) #Gets the whole data in the file Imported as a list in list
    Header = [item for sublist in Header for item in sublist]
    dictionary = {} #Split entity year and objects in dictionary
    for n in range(len(Header)):
        dictionary[Header[n]] = []
    for n in range(len(List)):#go through the list and add values for all data
        dictionary[Header[0]].append(List[n][0])
        dictionary[Header[1]].append(float(List[n][1]))
        dictionary[Header[2]].append(float(List[n][2]))

    n = 0
    count = 1

    plt.figure(figsize=(20, 15))

    for _ in range(num_subplots): #max number of plots in the file
        if n >= 442:
            break

        Store = dictionary[Header[0]][n]
        x = [] #empty list everytime a graph is drawn
        y = []

        while n < 442 and dictionary[Header[0]][n] == Store:
            x.append(dictionary[Header[1]][n])
            y.append(dictionary[Header[2]][n])
            n += 1


        if input('Do you want to plot ' + Store + '?:').lower() != 'no':
            userchoice = input('The graph is ' + Store + ' bar or line graph?: ').lower()
            if userchoice == 'bar':
                plt.subplot(3, 3, count)  # Adjust the subplot layout as needed
                plt.bar(x,y)#plot the graph as a bar chart
                plt.title(str(Store))
                plt.ylabel(Header[2])
                plt.xlabel(Header[1])
                count += 1
            else:
                plt.subplot(3, 3, count)  # Adjust the subplot layout as needed
                plt.plot(x, y) #plot the graph as line graph
                plt.title(str(Store))
                plt.ylabel(Header[2])
                plt.xlabel(Header[1])
                count += 1 # for every graph increase the count for the subplot

    plt.suptitle(str(Header[0]) + str(Header[1]) + str(Header[2]))
    plt.savefig('Pie')

# Ask the user for their choice
file_choice = 'earth-orbit-objects.csv'
num_subplots = 7
# Call the function with user choices
plot_user_choice(file_choice)