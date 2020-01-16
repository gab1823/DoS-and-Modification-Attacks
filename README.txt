This file describes the python programs used for DoS Attack and Modification Attack.

The programs are the following:

DoS Victim.py
	this is the program that is executed on victim's host in DoS attack. 
	It takes as argument the IPv6 address of the target website, i.e the website that the victim wants to communicate with.

DoS Attacker.py
	this is the program that is executed on attacker's host in DoS attack.
	It takes 2 arguments: the victim IPv6 address (that will be the sorurce address of the spoofed fragment) 
	and the IPv6 address of the target website.

Modification Victim.py
	this is the program that is executed on victim's host in Modification Attack.
	It takes as argument the IPv6 address of the target website.

Modification Attacker.py
	this is the program that is executed on attacker's host in Modification Attack.
	It takes 2 arguments: the victim IPv6 address and IPv6 address of the target website.
