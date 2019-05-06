CIS Control 3: Continuous Vulnerability Management
==================================================

Continuously acquire, assess, and take action on new information in order to identify vulnerabilities, remediate, and minimize the window of opportunity for attackers.

**Why is this CIS Control Critical?**

Cyber defenders must operate in a constant stream of new information: software updates, patches, security advisories, threat bulletins, etc. Understanding and managing vulnerabilities has become a continuous activity, requiring significant time, attention, and resources.

Attackers have access to the same information and can take advantage of gaps between the appearance of new knowledge and remediation. For example, when researchers report new vulnerabilities, a race starts among all parties, including: attackers (to “weaponize,” deploy an attack, exploit), vendors (to develop, deploy patches or signatures and updates), and defenders (to assess risk, regression-test patches, install).

Organizations that do not scan for vulnerabilities and proactively address discovered flaws face a significant likelihood of having their computer systems compromised. Defenders face particular challenges in scaling remediation across an entire enterprise, and prioritizing actions with conflicting priorities, and sometimes uncertain side effects.

.. toctree::
   :maxdepth: 1
   :name: toc-control-3

   3.1: Run Automated Vulnerability Scanning Tools <control-3.1>
   3.2: Perform Authenticated Vulnerability Scanning <control-3.2>
   3.3: Protect Dedicated Assessment Accounts <control-3.3>
   3.4: Deploy Automated Operating System Patch Management Tools <control-3.4>
   3.5: Deploy Automated Software Patch Management Tools <control-3.5>
   3.6: Compare Back-to-Back Vulnerability Scans <control-3.6>
   3.7: Utilize a Risk-Rating Process <control-3.7>
   
.. history
.. authors
.. license