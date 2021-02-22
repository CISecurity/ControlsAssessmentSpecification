CIS Control 2: Inventory and Control of Software Assets
=======================================================

Actively manage (inventory, track, and correct) all software (operating systems and applications) on the network so that only authorized software is installed and can execute, and that unauthorized and unmanaged software is found and prevented from installation or execution.

**Why is this CIS Control Critical?**

A complete software inventory is a critical foundation for preventing attacks. Attackers continuously scan target enterprises looking for vulnerable versions of software that can be remotely exploited. For example, if a user opens a malicious website or attachment with a vulnerable browser, an attacker can often install backdoor programs and bots that give the attacker long-term control of the system. Attackers can also use this access to move laterally through the network. One of the key defenses against these attacks is updating and patching software. However, without a complete inventory of software assets, an enterprise cannot determine if they have vulnerable software, or if there are potential licensing violations.

Even if a patch is not yet available, a complete software inventory list allows an enterprise to guard against known attacks until the patch is released. Some sophisticated attackers use “zero-day exploits”, which take advantage of previously unknown vulnerabilities that have yet to have a patch released by the software vendor. Depending on the severity of the exploit, an enterprise can implement temporary mitigation measures to guard against attacks until the patch is released.

Management of software assets is also important to identify unnecessary security risks. An enterprise should review their software inventory to identify any enterprise assets running software that is not needed for business purposes. For example, an enterprise asset may come installed with default software that creates a potential security risk and provides no benefit to the enterprise. It is critical to inventory, understand, assess, and manage all software connected to an enterprise’s infrastructure.


.. toctree::
   :maxdepth: 1
   :name: toc-control-2

   2.1: Establish and Maintain a Software Inventory <control-2.1>
   2.2: Ensure Authorized Software is Currently Supported  <control-2.2>
   2.3: Address Unauthorized Software <control-2.3>
   2.4: Utilize Automated Software Inventory Tools <control-2.4>
   2.5: Allowlist Authorized Software <control-2.5>
   2.6: Allowlist Authorized Libraries <control-2.6>
   2.7: Allowlist Authorized Scripts<control-2.7>
   
.. history
.. authors
.. license
