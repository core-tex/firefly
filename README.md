watch-the-skies
---------------

Evennia game code for an invite-only Firefly setting MUSH.

NOW DEFUNCT.  Kept around for personal reference.

Status
======

static code analysis health<A href="https://www.quantifiedcode.com/app/project/bb2a251198734661bc3d1bb1cd9bb6eb"><img src="https://www.quantifiedcode.com/api/v1/project/bb2a251198734661bc3d1bb1cd9bb6eb/badge.svg" alt="Code issues"/></A>

---

Welcome to Evennia!
===================

This directory is your game directory, set up to let you start with your new game right away.

You can delete this readme file when you've read it and you can re-arrange things in this game-directory to suit your own sense of organisation (the only exception is the directory structure of the server/ directory, which Evennia expects). If you change the structure you must however also edit/add to your settings file to tell Evennia where to look for things.

Your game's main configuration file is found in`server/conf/settings.py` (but you don't need to change it to get started). If you just created this directory, `cd` to this directory then initialize a new database using

```
evennia migrate
```

To start the server, `cd` to this directory and run

```
evennia -i start
```

This will start the server so that it logs output to the console. Make sure to create a superuser when asked. By default you can now connect to your new game using a MUD client on localhost:4000. You can also log into the web client by pointing a browser to http://localhost:8000.

Getting started
===============

It's highly recommended that you look up Evennia's extensive documentation found here: https://github.com/evennia/evennia/wiki.

Plenty of beginner's tutorials can be found here: http://github.com/evennia/evennia/wiki/Tutorials.
