CIS Control 4: Controlled Use of Administrative Privileges
==========================================================

The processes and tools used to track/control/prevent/correct the use, assignment, and
configuration of administrative privileges on computers, networks, and applications.

**Why is this CIS Control Critical?**

The misuse of administrative privileges is a primary method for attackers to spread inside a target
enterprise. Two very common attacker techniques take advantage of uncontrolled administrative
privileges. In the first, a workstation user running as a privileged user is fooled into opening a
malicious email attachment, downloading and opening a file from a malicious website, or simply
surfing to a website hosting attacker content that can automatically exploit browsers. The
file or exploit contains executable code that runs on the victim’s machine either automatically
or by tricking the user into executing the attacker’s content. If the victim user’s account has
administrative privileges, the attacker can take over the victim’s machine completely and install
keystroke loggers, sniffers, and remote control software to find administrative passwords and
other sensitive data. Similar attacks occur with email. An administrator inadvertently opens an
email that contains an infected attachment and this is used to obtain a pivot point within the
network that is used to attack other systems.

The second common technique used by attackers is elevation of privileges by guessing or cracking
a password for an administrative user to gain access to a target machine. If administrative
privileges are loosely and widely distributed, or identical to passwords used on less critical
systems, the attacker has a much easier time gaining full control of systems, because there are
many more accounts that can act as avenues for the attacker to compromise administrative
privileges.

.. toctree::
   :maxdepth: 1
   :name: toc-control-4

   4.1: Maintain Inventory of Administratove Accounts <control-4.1>
   4.2: Change Default Passwords <control-4.2>
   4.3: Ensure the Use of Dedicated Administrative Accounts <control-4.3>
   4.4: Use Unique Passwords <control-4.4>
   4.5: Use Multi-Factor Authentication for All Administrative Access <control-4.5>
   4.6: Use Dedicated Workstations for All Administrative Tasks <control-4.6>
   4.7: Limit Access to Scripting Tools <control-4.7>
   4.8: Log and Alert on Changes to Administrative Group Membership <control-4.8>
   4.9: Log and Alert on Unsuccessful Administrative Account Logon <control-4.9>
   
.. history
.. authors
.. license