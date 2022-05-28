"""
woerdle assistant 
2022 by N. Hillemann

for solving 
the daily riddle at 
www.woerdle.de
"""

def load_words_from_file(path): 
    """
    load German word list 
    """
    with open(path) as f:
        return [w.strip().lower() for w in f.readlines()]
        

def get_word_and_feedback(): 
    """
    ask user for word and color code feedback
    """
    word = input("Which word did you type in? ").lower()
    wordlength = len(word)
    if wordlength < 5:
        print("Only 5 letterss are valid!")
        exit()
    elif wordlength > 5:
        print("Only 5 letters are valid!")
        exit()   
    print("Good choice! So, which color did each of your letters get?")
    print("Type 'g' for green, 'y' for yellow and 'w' for wrong guess/grey! (e.g. gwwyg)")
    feedback = input("Feedback: ").lower()
    feedbacklength = len(feedback)
    if feedbacklength < 5:
        print("Only 5 letters are valid!")
        exit()
    elif feedbacklength > 5:
        print("Only 5 letters are valid!")
        exit()

    return word, feedback


def get_suggestions(word, feedback, words):
    """
    iterate through entire list of words
    compare it with input word and the color code in feedback
    remove invalid words
    return sorted list with suggestion
    """
    ws = set(words)
    for w in words:
        for i in range(5):
            f, c = feedback[i], word[i] 
            # discard every word that contains the letter marked with wrong (gray)
            if f == "w" and c in w:
                ws.discard(w) 
            # discard every word that contains the letter in any position 
            # besides the one marked with green
            elif f == "g" and c != w[i]:
                ws.discard(w) 
            # discard every word that does not contain the letter marked with yellow 
            elif f == "y" and c not in w:
                ws.discard(w) 
            # discard every word that has the letter marked with yellow on the same 
            # position as the yellow marker
            elif f == "y" and c == w[i]:
                ws.discard(w) 
            
    return sorted(ws)


def main():
    """
    main code to execute the assistant and call functions
    """
    print("Hello, I am your personal Wördle assistant today! My name is Wöödy.")
    print("Let's start with your first guess! Try a word with many vowels e.g. 'Mauer'!")
    
    # wordles are all allowed words from the German Woerdle game
    wordles = load_words_from_file('word_list_german.txt')

    for i in range(6):
        word, feedback = get_word_and_feedback()
        if feedback == 'ggggg':
            print("Lucky you! This was your guess number", i + 1)
            break
        
        for word in get_suggestions(word, feedback, wordles):
            print(word)
        

if __name__ == "__main__":
    main()