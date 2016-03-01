# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets.UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = \
    """
        ██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗
        ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║
        ██║ █╗ ██║███████║   ██║   ██║     ███████║
        ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║               {Y___{n
        ╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║            {Y,o88888{n
         ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝         {Y,o88{R888{Y88'{n
                                        {G,:o:o:oooo.       {Y,8O88{RPd8{Y888"{n
                                    {G,.::.::o:ooooOoOoO. {Y,oO{R8O8Pd88{Y8'"{n
        ████████╗██╗  ██╗███████╗  {G,.:.::o:o{Co{GOoO{Co{GOO8O8OOo.{R8OOPd8O8{YO"{n
        ╚══██╔══╝██║  ██║██╔════╝ {G, .{C.:.{G::o{C:o{GoOo{COOOO8{ROOOOo.FdO8{YO8"{n
           ██║   ███████║█████╗  {G, ..:.{C::o:ooOoOO8O88{R8O8O,COC{YOO"{n
           ██║   ██╔══██║██╔══╝ {G, . ..:{C.::o:ooOoOOOO8{ROOOOCO{YCO"{n
           ██║   ██║  ██║███████╗{G. ..:.{C::o{B:{CooO{BoOo{ROO8O8OC{YCCC"o{n
           ╚═╝   ╚═╝  ╚═╝╚══════╝  {G. .{C.:.:{B:o:ooo{RoOoC{YoCCC"o:o{n
                                   {G. .{C.:.:{B:o:{Ro:,cooo{YoCo{C"oo:o{G:{n
                                {G`   . {C. ..{B:{R.:cocoo{Yoo"'o{C:o:::{G'{n
        ███████╗██╗  ██╗██╗   ██╗{Y.{G`   {C. ..{R::ccc{Ycoc"'o:{Co:o:::{G'{n
        ██╔════╝██║ ██╔╝╚██╗ ██╔╝{Y.:.    {R,c:c{Yccc"{C':.:{G.:.{C:.{G:.'{n
        ███████╗█████╔╝  ╚████╔╝{Y:.{R:"'{G`{R:::{Y:c:"{G'..{C:.:.{G:.:.:.'{n
        ╚════██║██╔═██╗   ╚██╔╝{R:.'.:.{Y::::"'    {G. {C. . {G. .'{n
        ███████║██║  ██╗   ██║{Y. {R....:."' `   {G.  . . ''{n
        ╚══════╝╚═╝  ╚═╝   ╚═╝ {R.{Y..."'{n
                        {Y.. . ."'{n
                       {Y.{n
       +------------------------------------------------------------+
       |              http://watchtheskies.wikidot.com              |
       |           Account creation is closed at this time.         |
       |                                                            |
       |              Existing accounts connect with:               |
       |              co(nnect) <username> <password>               |
       |                                                            |
       | If you have spaces in your username, enclose it in quotes. |
       |  Enter help for more info. look will re-show this screen.  |
       +------------------------------------------------------------+"""
