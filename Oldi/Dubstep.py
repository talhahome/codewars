# Input
# The input consists of a single non-empty string, consisting only of uppercase English letters,
# the string's length doesn't exceed 200 characters
# Output
# Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
# Examples
# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
# =>  WE ARE THE CHAMPIONS MY FRIEND

def song_decoder(song):
    b = song.split('WUB')
    print(b)
    a = []
    for i in range(len(b)):
        if b[i] != '':
            a.append(b[i])
    c = ' '.join(a)
    print(c)
    return c

song = "AWUBWUBWUBBWUBWUBWUBC"
song_decoder(song)
