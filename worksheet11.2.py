import random
main_list = []
def hangman(word):
    for n in range(len(word)):
        main_list.append("_")
    max_wrong_attempts = 6  # Maximum allowed incorrect attempts
    wrong_attempts = 0

    while wrong_attempts < max_wrong_attempts:
        print("Current status: " + " ".join(main_list))
        guess = input("What is your guess?: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess and main_list[i] == "_":
                    main_list[i] = guess
                    print("Correct")
        else:
            print("Incorrect")
            wrong_attempts += 1

        if "_" not in main_list:
            print("You won! The word is:", word)
            return main_list

    print("You lost. The word was:", word)
    return main_list

word_list = []
with open("B99_episode.txt") as data_file:
    for line in data_file:
        word_list.append(line.strip())

random_word = random.choice(word_list)
main_list = hangman(random_word)
print(" ".join(main_list))