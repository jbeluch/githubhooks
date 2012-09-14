githubhooks
===========

A simple script to list or test your activated github hooks.


Installation
------------

`pip install githubhooks` or clone this repo and execute 'scripts/githubhooks.py'.


Example Usage
-------------

## Setup oauth token as env var
    (github-hooks)jon@lenovo ~/Code/github-hooks $ source GITHUB_TOKEN


## Listing available hooks
    (github-hooks)jon@lenovo ~/Code/github-hooks $ githubhooks.py list
    .. Listing Hooks by Repository ..
    xam:414859 (travis)
    xbmc-vimcasts:416593 (travis)
    xbmcswift:78826 (twitter)
    xbmcswift2:239826 (readthedocs)
    Warning: Skipping  forecast since I couldn't access hooks. Perhaps you don't have permission.


## Specifying hooks to run as args
    (github-hooks)jon@lenovo ~/Code/github-hooks $ githubhooks.py --hook xam:414859 --hook xbmc-vimcasts:416593 run
    Triggering hook travis for xam... OK
    Triggering hook travis for xbmc-vimcasts... OK


## Specifying hooks to run from a config file
    (github-hooks)jon@lenovo ~/Code/github-hooks $ cat hooks 
    # travis
    xam:414859

    # travis
    xbmc-vimcasts:416593
    (github-hooks)jon@lenovo ~/Code/github-hooks $ githubhooks.py --config hooks run
    Triggering hook travis for xam... OK
    Triggering hook travis for xbmc-vimcasts... OK
