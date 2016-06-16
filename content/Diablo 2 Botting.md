Title: The coolest thing I've ever done: my Diablo 2 Bot
Date: 2014-5-15 15:10
Category: diablo 2
Tags: diablo 2, C#, hacking
Status: draft


To be honest my favorite project (ever) was a Diablo II bot I made ~10 years ago. If you've never played the game Diablo II, it's your typical nerdy Dungeons and Dragons kind of collect gear + level up + beat up monsters type of game. 

The bot I made was "clientless," meaning it tracked the entire game state itself, replied to every packet appropriately, and didn't require a game running. That meant I could run 1000's of bots on a regular computer instead of 2-4 games that soaked up all of the memory/CPU. Normally this wouldn't be possible, most bots required the game to be running to generate the maps. I made an API wrapped around a map generator and sold 1000 map generations for $1, this is what powered my bots and made them special!

Not only could the bot run without the client, that was pretty cool, but also the bot required 0 configuration. Normally, you'd have to edit some .ini or something similar outlining your character, where to put items, what skills to use, some kind of script to do attacks in a smart way (i.e. for ranged attacks position yourself far away).

What my bot did, instead of reading some .ini file, was look directly at your character and infer a good build! This was like Heroku for Diablo II bots. You just pointed my bot at your character and it took over. If you had, for example, the "lighting bolt" spell maxed out, the bot would assume the "RangedAttack" pattern and stay at a decent distance while staying in line of sight. If you had no items or skills, the bot would smartly be able to at least punch the monsters!

One of the other cool pieces of this bot was the task queue based module system. Every action in the game was fired off by some module, and executed by being pulled off the task queue. For example, I had modules Mover, Killer, Item Pickup, and Chicken. Mover module could get it's own whole paragraph, but to summarize it used the non-client based map generation to stitch together all of the required maps to get from point A to point B. Meaning, you could ask the Mover module to go to the last place in the game from the first point in the game, and it could stitch every map together giving you all of the waypoints + quests required to get to that location.

The task based queue was especially useful. Consider if you were moving from Point A to Point B and some monster smacks you to half health, how will the bot react? The Chicken module will add a "very high" priority task to get the hell out of that area! 

Other cool parts of this bot were: CD Key rotator for running many bots at once sharing a pool of keys, entire website payment gateway + API, and an undetectable maphack that can reveal the map on a completely separate computer.

The whole project was built in about 2 months with C#, PHP and JS!

