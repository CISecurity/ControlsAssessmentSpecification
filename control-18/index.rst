CIS Control 18: Penetration Testing
=======================================================

Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses in controls (people, processes, and technology), and simulating the objectives and actions of an attacker.

**Why is this CIS Control Critical?**

A successful defensive posture requires a comprehensive program of effective policies and governance, strong technical defenses, combined with appropriate action from people. However, it is rarely perfect. In a complex environment where technology is constantly evolving and new attacker tradecraft appears regularly, enterprises should periodically test their controls to identify gaps and to assess their resiliency. This test may be from external network, internal network, application, system, or device perspective. It may include social engineering of users, or physical access control bypasses.

Often, penetration tests are performed for specific purposes:
•	As a “dramatic” demonstration of an attack, usually to convince decision-makers of their enterprise’s weaknesses
•	As a means to test the correct operation of enterprise defenses (“verification”)
•	To test that the enterprise has built the right defenses in the first place (“validation”)

Independent penetration testing can provide valuable and objective insights about the existence of vulnerabilities in enterprise assets and humans, and the efficacy of defenses and mitigating controls to protect against adverse impacts to the enterprise. They are part of a comprehensive, ongoing program of security management and improvement. They can also reveal process weaknesses, such as incomplete or inconsistent configuration management, or end-user training.

Penetration testing differs from vulnerability testing, described in CIS Control 7. Vulnerability testing just checks for presence of known, insecure enterprise assets, and stops there. Penetration testing goes further to exploit those weaknesses to see how far an attacker could get, and what business process or data might be impacted through exploitation of that vulnerability. This is an important detail, and often penetration testing and vulnerability testing are incorrectly used interchangeably. Vulnerability testing is exclusively automated scanning with sometimes manual validation of false positives, whereas penetration testing requires more human involvement and analysis, sometimes supported through the use of custom tools or scripts. However, vulnerability testing is often a starting point for a penetration test.

Another common term is “Red Team” exercises. These are similar to penetration tests in that vulnerabilities are exploited; however, the difference is the focus. Red Teams simulate specific attacker TTPs to evaluate how an enterprise’s environment would withstand an attack from a specific adversary, or category of adversaries.


.. toctree::
   :maxdepth: 1
   :name: toc-control-18

   18.1: Establish and Maintain a Penetration Testing Program <control-18.1>
   18.2: Perform Periodic External Penetration Tests <control-18.2>
   18.3: Remediate Penetration Test Findings <control-18.3>
   18.4: Validate Security Measures <control-18.4>
   18.5: Perform Periodic Internal Penetration Tests <control-18.5>
   
.. history
.. authors
.. license
