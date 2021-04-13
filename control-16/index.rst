CIS Control 16: Application Software Security
=======================================================

Manage the security life cycle of in-house developed, hosted, or acquired software to prevent, detect, and remediate security weaknesses before they can impact the enterprise.

**Why is this CIS Control Critical?**

Applications provide a human-friendly interface to allow users to access and manage data in a way that is aligned to business functions. They also minimize the need for users to deal directly with complex (and potentially error-prone) system functions, like logging into a database to insert or modify files. Enterprises use applications to manage their most sensitive data and control access to system resources. Therefore, an attacker can use the application itself to compromise the data, instead of an elaborate network and system hacking sequence that attempts to bypass network security controls and sensors. This is why protecting user credentials (specifically application credentials) defined in CIS Control 6 is so important.
Lacking credentials, application flaws are the attack vector of choice. However, today’s applications are developed, operated, and maintained in a highly complex, diverse, and dynamic environment. Applications run on multiple platforms: web, mobile, cloud, etc., with application architectures that are more complex than legacy client-server or database-web server structures. Development life cycles have become shorter, transitioning from months or years in long waterfall methodologies, to DevOps cycles with frequent code updates. Also, applications are rarely created from scratch, and are often “assembled” from a complex mix of development frameworks, libraries, existing code, and new code. There are also modern and evolving data protection regulations dealing with user privacy. These may require compliance to regional or sector-specific data protection requirements.
These factors make traditional approaches to security, like control (of processes, code sources, run-time environment, etc.), inspection, and testing, much more challenging. Also, the risk that an application vulnerability introduces might not be understood, except in a specific operational setting or context.
Application vulnerabilities can be present for many reasons: insecure design, insecure infrastructure, coding mistakes, weak authentication, and failure to test for unusual or unexpected conditions. Attackers can exploit specific vulnerabilities, including buffer overflows, exposure to Structured Query Language (SQL) injection, cross-site scripting, cross-site request forgery, and click-jacking of code to gain access to sensitive data, or take control over vulnerable assets within the infrastructure as a launching point for further attacks.
Applications and websites can also be used to harvest credentials, data, or attempt to install malware onto the users who access them.
Finally, it is now more common to acquire Software as a Service (SaaS) platforms, where software is developed and managed entirely through a third-party. These might be hosted anywhere in the world. This brings challenges to enterprises that need to know what risks they are accepting with using these platforms; and, they often do not have visibility into the development and application security practices of these platforms. Some of these SaaS platforms allow for customizing of their interfaces and databases. Enterprises that extend these applications should follow this CIS Control, similar to if they were doing ground-up customer development. 


.. toctree::
   :maxdepth: 1
   :name: toc-control-16

   16.1: Establish and Maintain a Secure Application Development Process <control-16.1>
   16.2: Establish and Maintain a Process to Accept and Address Software Vulnerabilities <control-16.2>
   16.3: Perform Root Cause Analysis on Security Vulnerabilities <control-16.3>
   16.4: Establish and Manage an Inventory of Third-Party Software Components <control-16.4>
   16.5: Use Up-to-Date and Trusted Third-Party Software Components <control-16.5>
   16.6: Establish and Maintain a Severity Rating System and Process for Application Vulnerabilities <control-16.6>
   16.7: Use Standard Hardening Configuration Templates for Application Infrastructure <control-16.7>
   16.8: Separate Production and Non-Production Systems <control-16.8>
   16.9: Train Developers in Application Security Concepts and Secure Coding <control-16.9>
   16.10: Apply Secure Design Principles in Application Architectures <control-16.10>
   16.11: Leverage Vetted Modules or Services for Application Security Components <control-16.11>
   16.12: Implement Code-Level Security Checks <control-16.12>
   16.13: Conduct Application Penetration Testing <control-16.13>
   16.14: Conduct Threat Modeling <control-16.14>

.. history
.. authors
.. license
