CIS Control 16: Account Monitoring and Control
=======================================================

Actively manage the life cycle of system and application accounts – their creation, use, dormancy,
deletion – in order to minimize opportunities for attackers to leverage them.

**Why is this CIS Control Critical?**

Attackers frequently discover and exploit legitimate but inactive user accounts to impersonate
legitimate users, thereby making discovery of attacker behavior difficult for security personnel
watchers. Accounts of contractors and employees who have been terminated and accounts
formerly set up for Red Team testing (but not deleted afterwards) have often been misused
in this way. Additionally, some malicious insiders or former employees have gained access to
accounts left behind in a system long after contract expiration, maintaining their access to an
organization’s computing system, and sensitive data for unauthorized and sometimes malicious
purposes.

.. toctree::
   :maxdepth: 1
   :name: toc-control-16

   16.1: Maintain an Inventory of Authentication Systems <control-16.1>
   16.2: Configure Centralized Point of Authentication <control-16.2>
   16.3: Require Multi-Factor Authentication <control-16.3>
   16.4: Encrypt or Hash All Authentication Credentials <control-16.4>
   16.5: Encrypt Transmittal of Username and Authentication Credentials <control-16.5>
   16.6: Maintain an Inventory of Accounts <control-16.6>
   16.7: Establish Process for Revoking Access <control-16.7>
   16.8: Disable Any Unassociated Accounts <control-16.8>
   16.9: Disable Dormant Accounts <control-16.9>
   16.10: Ensure All Accounts Have An Expiration Date <control-16.10>
   16.11: Lock Workstation Sessions After Inactivity <control-16.11>
   16.12: Monitor Attempts to Access Deactivated Accounts <control-16.12>
   16.13: Alert on Account Login Behavior Deviation <control-16.13>
   
.. history
.. authors
.. license