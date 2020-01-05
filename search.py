import os, webbrowser, sys, pyperclip

# from command line, type in title of search engine which you want to use
if sys.argv[1] == 'wikipedia':
    address = ' '.join(sys.argv[2:]) # concatenates all args[2:] to be used as search term 
    webbrowser.open('https://en.wikipedia.org/w/index.php?search=' + address + '&title=Special%3ASearch&go=Go&ns0=1') # copies term into search

elif sys.argv[1] == 'youtube':
    address = ' '.join(sys.argv[2:])
    webbrowser.open('https://www.youtube.com/results?search_query=' + address)

elif sys.argv[1] == 'wiktionary':
    address = ' '.join(sys.argv[2:])
    webbrowser.open('https://en.wiktionary.org/wiki/' + address)
