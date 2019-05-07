CIS Control 20: Penetration Tests and Red Team Exercises
=======================================================

Test the overall strength of an organization’s defense (the technology, the processes, and the
people) by simulating the objectives and actions of an attacker.

**Why is this CIS Control Critical?**

Attackers often exploit the gap between good defensive designs and intentions and
implementation or maintenance. Examples include: the time window between announcement of
a vulnerability, the availability of a vendor patch, and actual installation on every machine. Other
examples include: well-intentioned policies that have no enforcement mechanism (especially
those intended to restrict risky human actions); failure to apply good configurations to machines
that come on and off of the network; and failure to understand the interaction among multiple
defensive tools, or with normal system operations that have security implications.

A successful defensive posture requires a comprehensive program of effective policies and
governance, strong technical defenses, and appropriate action by people. In a complex
environment where technology is constantly evolving, and new attacker tradecraft appears
regularly, organizations should periodically test their defenses to identify gaps and to assess their
readiness by conducting penetration testing.

Penetration testing starts with the identification and assessment of vulnerabilities that can be
identified in the enterprise. Next, tests are designed and executed to demonstrate specifically
how an adversary can either subvert the organization’s security goals (e.g., the protection of
specific Intellectual Property) or achieve specific adversarial objectives (e.g., establishment of
a covert Command and Control infrastructure). The results provide deeper insight, through
demonstration, into the business risks of various vulnerabilities.

Red Team exercises take a comprehensive approach at the full spectrum of organization policies,
processes, and defenses in order to improve organizational readiness, improve training for
defensive practitioners, and inspect current performance levels. Independent Red Teams can
provide valuable and objective insights about the existence of vulnerabilities and the efficacy
of defenses and mitigating controls already in place and even of those planned for future
implementation.

.. toctree::
   :maxdepth: 1
   :name: toc-control-20

   20.1: Establish a Penetration Testing Program <control-20.1>
   20.2: Conduct Regular External and Internal Penetration Tests <control-20.2>
   20.3: Perform Periodic Red Team Exercises <control-20.3>
   20.4: Include Tests for Presence of Unprotected System Information and Artifacts <control-20.4>
   20.5: Create a Test Bed for Elements Not Typically Tested in Production <control-20.5>
   20.6: Use Vulnerability Scanning and Penetration Testing Tools in Concert <control-20.6>
   20.7: Ensure Results From Penetration Test Are Documented Using Open, Machine-Readable Standards <control-20.7>
   20.8: Control and Monitor Accounts Associated With Penetration Testing <control-20.8>
   
.. history
.. authors
.. license