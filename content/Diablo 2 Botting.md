Title: The coolest app I've built: Diablo 2 Botting
Date: 2016-6-26 15:10
Category: diablo 2
Tags: diablo 2, C#, hacking


My favorite project (ever) was a Diablo II botting system I made ~10 
years ago. If you've never played the game Diablo II, it's your typical 
nerdy Dungeons and Dragons kind of collect gear + level up + beat up 
monsters type of game. 

<p style="text-align: center;" class="image-wrapper">
    <a href="http://us.blizzard.com/en-us/games/d2/"><img src="images/d2/ingame.jpg" alt="Diablo 2" style="max-width: 500px;"></a>
    <br><i><small>Diablo 2 - Act 2 - Town</small></i>
</p>

## Diablo II Automation Progression

I got to make a ton of automation tools for this game:
 
 * started with [AutoIt](http://autoitscript.com) bots that moved based 
 on the pixels on the screen
 * an AutoIt OCR (which I'll cover in another article later) that helped 
 me pickup nice items
 * bots that no longer used pixels, instead memory and packet injection
 
 
<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/xqemOAJQBOU?rel=0" frameborder="0" allowfullscreen></iframe>
<p style="text-align: center;">
packet injecting bot
</p>

But, the coolest bot I made was "clientless" meaning: it tracked the entire game 
state itself, replied to every packet appropriately, and didn't require 
a game running. That meant I could run 1000's of bots on a regular 
computer instead of 2-4 games that soaked up all of the memory/CPU. 
Normally this wouldn't be possible, most bots required the game to be 
running to generate the maps. I made an API wrapped around a map 
generator this is what powered my bots and made them special! 

This would have been impossible without the amazing reverse engineering techniques
in the Diablo II hacking community. There were entire public wikis
dedicated to definitions for each packet and memory structure. Pretty
cool stuff to be noodling on when you're still in highschool!

## Undetectable maphack

I made a neat maphack to test out the map generation API:

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/pL7K58Cdo5Y?rel=0" frameborder="0" allowfullscreen></iframe>
<p style="text-align: center;">
Maphack
</p>

This maphack was novel in that it didn't do anything inside the game
that changed memory or hooked into anything in a strange way. It simply
got the map seed (so it could run on a totally different computer) and
generated all the maps in the game, then stitching each together.

Also, the maphack could do some not-so-undetectable things like hook
into the game and inject "teleport this way" packets until you reach
the destination.

## Finally, clientless bot

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/9epvPv-mD1Y?rel=0" frameborder="0" allowfullscreen></iframe>
<p style="text-align: center;">
Bot pathing around the map
</p>


Not only could the bot run without the client, that was pretty cool, but 
also the bot required no configuration. Normally, you'd have to edit some 
.ini or something similar outlining your character, where to put items, 
what skills to use, some kind of script to do attacks in a smart way 
(i.e. for ranged attacks position yourself far away).

What my bot did, instead of reading some .ini file, was look directly at 
your character and infer a good build! This was like Heroku for Diablo 
II bots. You just pointed my bot at your character and it took over. If 
you had, for example, the "lighting bolt" spell maxed out, the bot would 
assume the "RangedAttack" pattern and stay at a decent distance while 
staying in line of sight. If you had no items or skills, the bot would 
smartly be able to at least punch the monsters!

One of the other cool pieces of this bot was the task queue based module 
system. Every action in the game was fired off by some module, and 
executed by being pulled off the task queue. For example, I had modules 
Mover, Killer, Item Pickup, and Chicken. I could write a whole paragraph 
on Mover Module, but to summarize it I used the non-client based map 
generation to stitch together all of the required maps to get from 
point A to point B. Meaning, you could ask the Mover module to go to the 
last place in the game from the first point in the game, and it could 
stitch every map together giving you all of the waypoints + quests 
required to get to that location.

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/kGcE9SBIJ68?rel=0" frameborder="0" allowfullscreen></iframe>
<p style="text-align: center;">
Bot picking stuff up
</p>

The task based queue was especially useful. Consider if you were moving 
from Point A to Point B and some monster smacks you to half health, how 
will the bot react? The Chicken module will add a "very high" priority 
task to get the hell out of that area! 

Other cool parts of this bot were: CD Key rotator for running many bots 
at once sharing a pool of keys, entire website payment gateway + API, 
and some pretty impressive API performance using fancy caching techniques
with IO pooling.

The whole project was built in about 2 months with C#, PHP and JS!

