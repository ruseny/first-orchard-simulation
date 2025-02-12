# First Orchard game simulation

This is a toy project (pun intended) about a children's game: [First Orchard](https://www.haba-play.com/de-de/p/meine-ersten-spiele-erster-obstgarten--1004655#variationId=1004655001) by [HABA](https://en.wikipedia.org/wiki/Habermaa%C3%9F). The player rolls a 6-faced die: 4 colours correspond to 4 types of fruit, basket means the player can pick any remaining fruit, and crow is the main opponent who moves one tile. The objective is to collect all fruits, 4 of each type, before crow moves 6 times.

This helps to teach simple rules, among other things, to small children. As such, the crow should have a reasonable chance of winning, but not too high to be frustrating for kids. As I was playing with my kids, I wondered what this probability would be, and I thought the easiest way is to simulate the game and check the results.

The only strategic decision is when the player rolls basket. I also wondered how much of a difference does it make to play strategically. So I made it possible to play in two modes: smart or random.

According to my results from simulations, the crow wins 26% of the time in the random mode, and 23% of the time in the smart mode.