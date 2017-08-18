Title: My Diablo 2 Botting Phase
Date: 2016-6-26 15:10
Category: diablo 2
Tags: diablo 2, C#, hacking


My favorite project (ever) was a Diablo II botting system I made in 2008. The summer before sophomore year of college. 
If you have never played the game Diablo II, it's your typical 
nerdy Dungeons and Dragons kind of collect gear + level up + beat up 
monsters type of game. 

<p style="text-align: center;" class="image-wrapper">
    <a href="http://us.blizzard.com/en-us/games/d2/"><img src="images/d2/ingame.jpg" alt="Diablo 2" style="max-width: 500px;"></a><br>
    <span class="centered-label">Diablo 2 - Act 2 - Town</span>
</p>

## Diablo II Automation

 * started at 10-12 years old with [AutoIt](http://autoitscript.com) bots that moved based 
 on the pixels on the screen
 * then at ~15 got more complicated with an AutoIt OCR (which I'll cover in another article later) that helped 
 me pickup nice items
 * around ~17 moved onto C# bots that no longer used pixels, instead read/wrote memory and injected packets
 * around ~19 I made a clientless bot (no game required, entire state tracked in the bot)
 
 
<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/xqemOAJQBOU?rel=0" frameborder="0" allowfullscreen></iframe>
<p class="centered-label">
packet injecting bot
</p>

A clientless bot tracked the game state, replied to every packet appropriately, and did this 
all without a real game client running. Without the client running I could start thousands of bots on a regular 
computer, instead of at most 2-4 bots that soaked up all of the memory/CPU to display graphics.
 
 
Normally this wouldn't be possible, because most bots required the game to be 
running to see the map and path to the monsters. One of the secret ingredients to my bot was the ability
to generate the game map based on the seed received on game join.
I wrapped an API around this map generator and that's what made my bots extra special! 

I couldn't have done any of this without the amazing reverse engineers who shared their work
in the Diablo II hacking community. There were entire public wikis
dedicated to definitions for each packet and memory structure. Pretty
cool stuff to be noodling on when you're still in highschool!

## Undetectable maphack

Here's the neat little maphack that tested out the map generation API:

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/pL7K58Cdo5Y?rel=0" frameborder="0" allowfullscreen></iframe>
<p class="centered-label">
Maphack
</p>

A maphack is a tool that reveals unexplored areas in a game. StarCraft,
Counter-Strike, WarCraft, etc. all have similar tools that give
some players an advantage over others. It's pretty lame to do in Player vs
Player games like StarCraft, but in Diablo 2 it makes finding items less
tedious -- a little bit less cheaty :)

This maphack was novel in that it didn't do anything inside the game
that changed memory or hooked into anything in a strange way. Using the
map seed I was able to generate all the maps in the game, then 
stitch each area together. Not to mention with the API we could run the maphack on
a separate computer!

Also, the maphack could do some not-so-undetectable things like hook
into the game and inject "teleport to X, Y" packets until you reach
the destination.

## Finally, clientless bot

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/9epvPv-mD1Y?rel=0" frameborder="0" allowfullscreen></iframe>
<p class="centered-label">
Bot pathing around the map
</p>


Not only could the bot run without the client, that was pretty cool, but 
it also required no configuration. Normally with other bots, you'd have to edit some 
.ini or something similar outlining your character, where to put items, 
what skills to use, some kind of script to do attacks in a smart way 
(i.e. for ranged attacks position yourself far away).

What my bot did, instead of reading some .ini file, was look directly at 
your character and infer a good build! This was like [Heroku](http://heroku.com) for Diablo 
II bots. You just pointed my bot at your character and it took over. If 
you had, for example, the "lighting bolt" spell maxed out, the bot would 
assume the "RangedAttack" pattern and stay at a decent distance while 
staying in line of sight. If you had no items or skills, the bot would 
smartly be able to at least punch the monsters!

One of the other cool pieces of this bot was the task queue based module 
system. Every action in the game was fired off by some module, and 
executed by being pulled off the task queue. For example, I had modules 
Mover, Killer, Item Pickup, and Chicken. I could write a whole blog 
on Mover Module, but to summarize it I used the non-client based map 
generation to stitch together all of the required maps to get from 
point A to point B. Meaning, you could ask the Mover module to go to the 
last place in the game from the first point in the game, and it could 
stitch every map together giving you all of the waypoints + quests 
required to get to that location.

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/kGcE9SBIJ68?rel=0" frameborder="0" allowfullscreen></iframe>
<p class="centered-label">
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

