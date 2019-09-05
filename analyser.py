import codecs

def normalize(s):
    """
    (str) -> str

    Given a string, return a copy of that string with
    all alphabetical characters turned lowercase and
    all special characters removed and replaced with a space.

    >>> normalize("Hey! How are you? I'm fine. ;D")
    'hey  how are you  i m fine   d'
    """

    new_string = ''

    for ch in s:
        if ch.isalpha():
            new_string = new_string + ch.lower()
        elif ch == ' ':
            new_string = new_string + ' '
        else:
            new_string = new_string + ' '

    return new_string.strip()

def get_sentiment_scores(filename):
    """
    (str) -> dict

    Given the name of a file which contains a list of words
    and their positive and negative weights, return a dictionary
    storing this information as follows:
    - the keys in the dict are the words
    - the values associated with each key is a tuple of two floats,
      where the first element is the positivity weight of this word,
      and the second element is the negativity weight of this word      
    """
    d = {}
    L = []
    f = codecs.open(filename, "r", "utf-8")

    for line in f:
        if not line.startswith('#'):
            x = line.strip()
            x = line.split('\t')
            key = x[2][:-1]
            pos = x[0]
            neg = x[1]
            d[key] = (pos, neg)

    sentiment_scores = d

    return sentiment_scores

    pass


def fix_file(filename):
    ''' (str -> list)

    Adjusts the file to return a list of the words in the file.

    '''

    f = codecs.open(filename, "r", "utf-8")
    L = []
    final_string = ''.join(L)

    for line in f:
        L.append(normalize(line.strip()))

    final_string = ''.join(L)

    return final_string.split(' ')


    

def analyze_file(filename, sentiment_scores):
    """
    (str, dict) -> tuple of three floats

    Given a filename and a dict of sentiment scores, analyze the contents
    of the file and figure out its total positivity, negativity and sentiment.
    Return this in a tuple of floats where the first element is the total
    positivity score as a ratio to total number of words in the file, the
    second element is the total negativity as a ratio to total words, and
    the third element is the total sentiment.
    """
    i = 0
    p = 0 
    n = 0
    string_list = fix_file(filename)

    while i < len(string_list):
        if string_list[i] in sentiment_scores:
            tup = sentiment_scores.get(string_list[i])
            p = (p) + float(tup[0]) * 100 
            n = (n) + float(tup[1]) * 100
            i = i + 1
        else:
            i = i + 1


    return ((p) / (len(string_list)), (n) / (len(string_list)), (p / (len(string_list)) - n / (len(string_list))))


if __name__ == "__main__":

    sentiment_scores = get_sentiment_scores("sentiment_scores.txt")

    while True:
        filename = input("Enter a filename: ")
        pos, neg, total = analyze_file(filename, sentiment_scores)
        print("Total positivity score: {:.3f}, \nTotal negativity score: {:.3f}, \nTotal sentiment score: {:.3f}".format(pos, neg, total))
