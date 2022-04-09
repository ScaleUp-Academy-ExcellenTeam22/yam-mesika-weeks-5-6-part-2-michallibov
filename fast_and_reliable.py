import time


def find_word_in_list_or_set(iterable):
    """
    This function runs a loop of 1000 iterations and in each iteration it searches the word "zwitterion" in the
    iterable structure we got.
    :param iterable: a list or a set of words from the file 'words.txt' that we recieved from the average_runtime
    function.
    """
    # The res variable is just to prevent a warning that the statement has no effect. 
    res = [word for _ in range(1, 1000) for word in iterable if word == "zwitterion"]


def average_runtime(words_from_file) -> float:
    """
    This function gets an iterable structure and calls the find_word_in_list_or_set and counts down the time it
    took to find_word_in_list_or_set function to do it's job.
    :param words_from_file: an iterable structure which contains words from the file 'words.txt'.
    :return: the time it took for the function find_word_in_list_or_set to finish it's job.
    """
    start = time.time()
    find_word_in_list_or_set(words_from_file)
    end = time.time()
    return (end-start)/1000


if __name__ == '__main__':
    file = open("C:\\Users\\Michal\\Downloads\\Notebooks-master\\week06\\resources\\words.txt", 'r')
    words_list = [word for line in file for word in line.split()]
    words_set = {word for line in file for word in line.split()}
    print(f"on a list the average time is {average_runtime(words_list)} seconds")
    print(f"on a set the average time is {average_runtime(words_set)} seconds")
