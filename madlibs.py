# using string concatenation
#youtuber = "Bob Bobbington" # some string

# different wats to complete the same task
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
ran1 = input("Random: ")
ran2 = input("Random: ")

madlib = f"Life is but a {adj} {verb1}. That is why I am {verb2}. So that makes my brith person a {ran1}. \
Now while I sit on the dock of the bay {ran2}."

print(madlib)