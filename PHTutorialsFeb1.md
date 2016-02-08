These are my notes for the Programming Historian tutorials for February 1.

#### Automated Downloading with Wget

So, this is meant to teach you how to use Wget, which is used to pull information from a website, either to take information from it or to copy the whole thing.

Recommends caution, since this is a powerful tool. Build-in limits and delays to not overload servers.

Download instructions. For Windows, recommends putting it in the Windows directory to be able to use it anywhere. Hmm, recommends the 32-bit system, even though I'm on a 64-bit OS. I guess I'll go with the recommendation though.

For some reason my computer isn't letting me save in C:Windows, even though I'm running as an Administrator. I'll try putting it in my Downloads folder and then moving it. There we go, that worked.

Alright, so now I have it downloaded in the right directory.

Made a wget directory in my Research Notebook and then ran the command by copying it from the tutorial. It worked!

Learning extra commands.

-r: "Recursive retrieval" has the program follow links and download them too - any links, so be careful!

--no-parent (-np): this will make it follow links, but not past the parent directory, essentially staying on the same website.

Then you can add numbers to be more specific about the number of links you want it to follow.

-w followed by a number adds a wait between requests to not overload the server.

--limit-rate= limits your bandwith, again to avoid ovverloading.

Now we're going to download all the ActiveHistory papers. I should actually type all this in to make sure I understand it. Good tip about trailing slash indicating something is a directory rather than a file. Order of options doesn't matter, also a good tip.

I typed this
wget -r --no-parent -w 2 --limit-rate=20k http://activehistory.ca/papers/

As promised, it's slower, but seems to be working. It worked! Oh wait, actually, looking through the log it seems like a bunch of it failed. Although, every spot where it failed said that the name was right, there just wasn't data of that type there so maybe it was just looking for some stuff that doesn't exist and that's fine.

-m lets you mirror a whole website. Don't think I'll actually do that right now. Although, actually, that's the end of the tutorial, so I may as well try it

#### Datamining the Internet Archive

Kind of annoying that the tutorial doesn't explain where or how to get Python. And the link to the `pip` tutorial actually just goes to the PH homepage.

And now the `pip` tutorial doesn't even explain how to get Python. Oh okay, there are instructions for that on the homepage, I think? Ha, nope!

What the actual fuck? Why do these tutorials not just have a link to download python? I guess I'll just find it myself.

Installing Git Bash to use as a command line program as recommend in Slack.

Or does my computer already have Python? No, it doesn't, but I installed it.

Now the tutorial doesn't tell me where I need to be to install stuff with `pip`. This is really terrible.

I think I need to be in the python folder though.

Now I'm trying to use get-pip.py to install pip and it's not working. Hmm, I think double clicking on get-pip.py in the Python folder might have done something?

Goddamnit this stupid Bash thing is just telling me that none of these commands exist.

Hmm, maybe I should just follow the instructions on the get-pip.py page.

Nope, this is all written in Elvish.

Okay, the `python` command seems to work in Command Prompt

OKay, using that, it seems that I already have pip installed

Now I'm trying to install `internetarchive`, but it says there's no such file. Guess I have to download that. WOULD HAVE BEEN NICE FOR THE TUTORIAL TO SAY THAT.

Nope, downloaded it and the command `python pip install internetarchive` is still telling me no such thing exists. Maybe I need to use the actual file name? That would make sense.

OOOh, it's telling me that "pip" doesn't exist. What the fuck then?

Alright, I think I'm going to leave this one for now and try to get help later.

OH SHIT NEVERMIND THE ADVICE IN SLACK worked! typed in `python -m pip install pymarc` in Command Prompt and that worked! No clue why that `-m` was needed. Gonna try to see if that works in Bash. NOPE HAHAHA!

But it did work to install `internetarchive` as well, in Command Prompt, so that's fine. No clue why Bash isn't working.

Alright, now I'm in the Python interpreter (another thing that the tutorial should have specified), in order to get the Internet ARchive stuff. Oh nevermind, it does mention that in the second line.

typed in

`import internetarchive`

`search = internetarchive.search_items('collection:bplscas')`

`print search.num_found`

into the Python interpreter and that gave me 9774, so that seems to have worked

Now to look at the identifiers of an individual item. Typing

`item = internetarchive.get_item('lettertowilliaml00doug')`

`item.download()`

Seems to be working! Success! Now I exited the interpreter to go look at what I downloaded. And the folder's there, inside of the Python directory!

Alright, back into the interpreter to learn about metadata. Gotta import the module again and search again. Hmm the search didn't seem to work, gotta double check what I typed. Oh, nevermind, I just didn't ask it to print the result, so that should be fine.

Now looking at the identifiers of the items in the search.

`for result in search:`

  `print result['identifier']`

TAB is important! Success!

Now learning about `for` loops. Thing after `for` is a local variable: what you're calling the things in your larger colelction of things. You can also put more commands in a `for` loop.

Now I actually have to write a Python script!

Hmm... it's really unclear how to do this, but I'm making some guesses and looking at the Slack channel. Basically, I saved the file as GetMARC.py. Then, I tried typing `python run GetMARC.py` in the folder I saved that file too, but Command Prompt told me it didn't recognize `python`. So I went into the Python folder to set the file path, because that's what Shawn said in Slack. ALright, still says it doesn't recognize "python". Hmm... after some googling, looks like the PATH thing is the problem, but this is telling me to do it from control panel. Alright, did that, now let's see if that worked

IT WORKED! in Command Prompt I typed:

`python.exe "C:\Users\Thomas\Documents\School Work\Carleton\Winter 2016\HIST 5702\BPLSCASMARC.GetMARC.py"`

I stopped it, but I got at least 1 XML file.

Now to the next part: building error reporting into the script. Wrote all that in.

HA! Forgot to run the thing in the folder where I wanted to store this stuff. Whoops.

Oh man, so much more of this. This is the pymarc stuff now. Don't think I'm actually going to go into that right now.
