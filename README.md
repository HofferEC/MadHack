# MadHack
Madhacks Fall 2018


adding use of frequency

by adding a flag to our api call (&md=f)
"https://api.datamuse.com/words?ml=" + inputWord + "&md=f"
the api will return a tag value

this can be accessed with response[index]['tags']
this is where it gets tricky
there are multiple tags, the one we want looks like 'f:50.202'
but for some reason it doesn't let us do response[index]['tags']['f']

so you have to access it by index, it's typically the last index in the tag field
so you can do response[index]['tags'][-1] (-1 accesses the last item in array)

then you have to typecast that from a String to a float

So now if you save this you have the frequency of the word.

so if the current word we have has a frequency lower than a tolerance that we manually set, we want to get a new word

that's about it

frequencyTolerance = 20 is a decent value to use
