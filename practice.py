# In this problem you will read from a file a list of comma separated integers
# A number can appear anywhere, any number of times
# The program:
  # A user can search for any number
  # You need to tell them where (starting at 1, not 0), and how many times the number occurs
  
######################################################
# Hi, Vincent. Please check if this is what you want the code to do ~ Saffa          #
def read_file(files):
    f = open(files, "r")
    r = f.read()
    z = []
    for i in r.split():
        z.append(i)
    # print z
    return z


def search(first, word):

    print "The word you are searching for \"%s\" occurs %s times" % (word, first.count(word))


def main():

    files = raw_input(" What is the name of your file:   ")
    read_file(files)
    u_input = raw_input("What word are you searching for:   ")
    search(read_file(files), u_input)
    
main()
