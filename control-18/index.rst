CIS Control 18: Application Software Security
=======================================================

Manage the security life cycle of all in-house developed and acquired software in order to prevent,
detect, and correct security weaknesses.

**Why is this CIS Control Critical?**

Attacks often take advantage of vulnerabilities found in web-based and other application
software. Vulnerabilities can be present for many reasons, including coding mistakes, logic errors,
incomplete requirements, and failure to test for unusual or unexpected conditions. Examples of
specific errors include: the failure to check the size of user input; failure to filter out unneeded
but potentially malicious character sequences from input streams; failure to initialize and clear
variables; and poor memory management allowing flaws in one part of the software to affect
unrelated (and more security critical) portions.

There is a flood of public and private information about such vulnerabilities available to
attackers and defenders alike, as well as a robust marketplace for tools and techniques to
allow “weaponization” of vulnerabilities into exploits. In one attack, more than 1 million web
servers were exploited and turned into infection engines for visitors to those sites using SQL
injection. During that attack, trusted websites from state governments and other organizations
compromised by attackers were used to infect hundreds of thousands of browsers that accessed
those websites. Many more web and non-web application vulnerabilities are discovered on a
regular basis.

.. toctree::
   :maxdepth: 1
   :name: toc-control-18

   18.1: Establish Secure Coding Practices <control-18.1>
   18.2: Ensure That Explicit Error Checking Is Performed for All In-House Developed Software <control-18.2>
   18.3: Verify That Acquired Software Is Still Supported <control-18.3>
   18.4: Only Use Up-to-Date and Trusted Third-Party Components <control-18.4>
   18.5: Use only Standardized and Extensively Reviewed Encryption Algorithms <control-18.5>
   18.6: Ensure Software Development Personnel Are Trained in Secure Coding <control-18.6>
   18.7: Apply Static and Dynamic Code Analysis Tools <control-18.7>
   18.8: Establish a Process to Accept and Address Reports of Software Vulnerabilities <control-18.8>
   18.9: Separate Production and Non-Production Systems <control-18.9>
   18.10: Deploy Web Application Firewalls <control-18.10>
   18.11: Use Standard Hardening Configuration Templates for Databases <control-18.11>
   
.. history
.. authors
.. license