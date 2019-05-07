CIS Control 11: Secure Configuration for Network Devices, such as Firewalls, Routers, and Switches
==================================================================================================

Establish, implement, and actively manage (track, report on, correct) the security configuration of
network infrastructure devices using a rigorous configuration management and change control
process in order to prevent attackers from exploiting vulnerable services and settings.

**Why is this CIS Control Critical?**

As delivered from manufacturers and resellers, the default configurations for network
infrastructure devices are geared for ease-of-deployment and ease-of-use – not security. Open
services and ports, default accounts (including service accounts) or passwords, support for older
(vulnerable) protocols, pre-installation of unneeded software; all can be exploitable in their
default state. The management of the secure configurations for networking devices is not a onetime
event, but a process that involves regularly re-evaluating not only the configuration items
but also the allowed traffic flows. Attackers take advantage of network devices becoming less
securely configured over time as users demand exceptions for specific business needs. Sometimes
the exceptions are deployed and then left undone when they are no longer applicable to the
business needs. In some cases, the security risk of the exception is neither properly analyzed nor
measured against the associated business need and can change over time.

Attackers search for vulnerable default settings, gaps or inconsistencies in firewall rule sets,
routers, and switches and use those holes to penetrate defenses. They exploit flaws in these
devices to gain access to networks, redirect traffic on a network, and intercept information while
in transmission. Through such actions, the attacker gains access to sensitive data, alters important
information, or even uses a compromised machine to pose as another trusted system on the
network.

.. toctree::
   :maxdepth: 1
   :name: toc-control-11

   11.1: Maintain Standard Security Configuration for Network Devices <control-11.1>
   11.2: Document Traffic Configuration Rules <control-11.2>
   11.3: Use Automated Tools to Verify Standard Device Configurations and Detect Changes <control-11.3>
   11.4: Install the Latest Stable Version of Any Security-Related Updates on All Network Devices <control-11.4>
   11.5: Manage Network Devices Using Multi-Factor Authentication and Encrypted Sessions <control-11.5>
   11.6: Use Dedicated Workstations for All Network Administrative Tasks <control-11.6>
   11.7: Manage Network Infrastructure Through a Dedicated Network <control-11.7>
   
.. history
.. authors
.. license