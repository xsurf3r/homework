msg = "Hi sjfnsdfg hry"
msg_low = msg.lower()

keywords = ["Hi", "hry", "goodbye"]
reactions = ["Hello", "Fine", "bye"]
isCaseSensitive = [False, True, False]

matched = [x for x in range(len(keywords)) if (isCaseSensitive[x] and keywords[x] in msg) or (keywords[x] in msg_low)]

reactions[min(matched)]

def func(msg):
    msg_low = msg.lower()
    
    if "Hi" in msg_low:
        print("Hello")
    elif "hry" in msg:
        print("Fine")
    elif "goodbye" in msg_low:
        print("bye")
 