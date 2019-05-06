CIS Control 2: Inventory and Control of Software Assets
=======================================================

Actively manage (inventory, track, and correct) all software on the network so that only authorized software is installed and can execute, and that all unauthorized and unmanaged software is found and prevented from installation or execution.

**Why is this CIS Control Critical?**

Attackers continuously scan target organizations looking for vulnerable versions of software that can be remotely exploited. Some attackers also distribute hostile web pages, document files, media files, and other content via their own web pages or otherwise trustworthy third-party sites. When unsuspecting victims access this content with a vulnerable browser or other client-side program, attackers compromise their machines, often installing backdoor programs and bots that give the attacker long-term control of the system. Some sophisticated attackers may use zero-day exploits, which take advantage of previously unknown vulnerabilities for which no patch has yet been released by the software vendor. Without proper knowledge or control of the software deployed in an organization, defenders cannot properly secure their assets.

Poorly controlled machines are more likely to be either running software that is unneeded for business purposes (introducing potential security flaws), or running malware introduced by an attacker after a system is compromised. Once a single machine has been exploited, attackers often use it as a staging point for collecting sensitive information from the compromised system and from other systems connected to it. In addition, compromised machines are used as a launching point for movement throughout the network and partnering networks. In this way, attackers may quickly turn one compromised machine into many. Organizations that do not have complete software inventories are unable to find systems running vulnerable or malicious software to mitigate problems or root out attackers.

Managed control of all software also plays a critical role in planning and executing system backup, incident response, and recovery.

.. toctree::
   :maxdepth: 1
   :name: toc-control-2

   2.1: Maintain Inventory of Authorized Software <control-2.1>
   2.2: Ensure Software Is Supported by Vendor <control-2.2>
   2.3: Utilize Software Inventory Tools <control-2.3>
   2.4: Track Software Inventory Changes <control-2.4>
   2.5: Integrate Software and Hardware Asset Inventories <control-2.5>
   2.6: Address Unapproved Software <control-2.6>
   2.7: Utilize Application Whitelisting <control-2.7>
   2.8: Implement Application Whitelisting of Libraries <control-2.8>
   2.9: Implement Application Whitelisting of Scripts <control-2.9>
   2.10: Physically or Logically Segregate High Risk Applications <control-2.10>
   
.. history
.. authors
.. license