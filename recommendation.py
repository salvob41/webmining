from datasketch import MinHash
import json
import random
import unicodedata
import operator
from collections import defaultdict


def random_samples(data, k):
    print("These are example songs which you can choose from")
    keys = random.sample(list(data), k)
    for key in keys:
        (artist, song_name) = key.split("#")
        print("\t{} - {}".format(artist.replace("_", " "), song_name.replace("_", " ")))


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' "
                  "(or 'y' or 'n').\n")


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def ask():
    return strip_accents(input("Please enter the author or the title of a song (or part of it): ").lower().strip())


def normalize_title(title, accent=True):
    if accent:
        title = title.lower().strip()
        title = strip_accents(title)
    (artist, song_name) = title.split("#")
    return artist.replace("_", " "), song_name.replace("_", " ")


filename = "minhash_dist.json"

with open(filename) as f:
    data = json.load(f)

example_songs = 10
max_results = 5

print("#############")
print("Welcome! This is the system that take as input a song and it will suggest a list of {} songs similar to it",
      "calculated with a estimated Jaccard Similarity (MinHash)".format(max_results))
random_samples(data, example_songs)
print("Write 'x' to stop the program ")
print("If you want help, you might write 'h' or 'help' to show a list of songs you might look for")
print("#############")
input_song = ask()

while input_song != "x":
    if input_song == "help" or input_song == "h":
        random_samples(data, example_songs)
        input_song = ask()
        continue
    query = ""
    for key in data:
        artist, song = normalize_title(key)
        if input_song in song or input_song in artist:
            artist, song = normalize_title(key, False)
            if query_yes_no("Maybe you meant {} by {}?".format(song, artist)):
                print("Good choice")
                query = key
                input_song = None
                break
            else:
                continue

    if query:
        print("You chose {} by {}".format(song, artist))
        connected_songs = data[query]
        output = [(k, connected_songs[k]) for k in sorted(connected_songs, key=connected_songs.get, reverse=True)]
        i = 1
        print()
        print("Here the list of suggested songs:")
        for i in range(0, max_results):
            suggested_song = output[i][0]
            score = output[i][1]
            artist, song = normalize_title(suggested_song, False)
            print(" {} by {} \t{}".format(song, artist, score))
        print()
        input_song = ask()
    else:
        print("Sorry, I didn't quite catch the song you're referring too, please try again")
        input_song = ask()

print("Thank you!")
