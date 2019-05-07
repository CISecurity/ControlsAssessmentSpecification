CIS Control 13: Data Protection
=======================================================

The processes and tools used to prevent data exfiltration, mitigate the effects of exfiltrated data,
and ensure the privacy and integrity of sensitive information.

**Why is this CIS Control Critical?**

Data resides in many places. Protection of that data is best achieved through the application
of a combination of encryption, integrity protection, and data loss prevention techniques. As
organizations continue their move towards cloud computing and mobile access, it is important
that proper care be taken to limit and report on data exfiltration while also mitigating the effects
of data compromise.

Some organizations do not carefully identify and separate their most sensitive and critical
assets from less sensitive, publicly accessible information on their internal networks. In many
environments, internal users have access to all or most of the critical assets. Sensitive assets
may also include systems that provide management and control of physical systems, such as
Supervisory Control and Data Acquisition (SCADA). Once attackers have penetrated such a
network, they can easily find and exfiltrate important information, cause physical damage, or
disrupt operations with little resistance. For example, in several high-profile breaches over the
past few years, attackers were able to gain access to sensitive data stored on the same servers
with the same level of access as far less important data. There are also examples of using access to
the corporate network to gain access to, then control over, physical assets and cause damage.

.. toctree::
   :maxdepth: 1
   :name: toc-control-13

   13.1: Maintain an Inventory of Sensitive Information <control-13.1>
   13.2: Remove Sensitive Data or Systems Not Regularly Accessed by Organization <control-13.2>
   13.3: Monitor and Block Unauthorized Network Traffic <control-13.3>
   13.4: Only Allow Access to Authorized Cloud Storage or Email Providers <control-13.4>
   13.5: Monitor and Detect Any Unauthorized Use of Encryption <control-13.5>
   13.6: Encrypt Mobile Device Data <control-13.6>
   13.7: Manage USB Devices <control-13.7>
   13.8: Manage System’s External Removable Media’s Read/Write Configurations <control-13.8>
   13.9: Encrypt Data on USB Storage Devices <control-13.9>
   
.. history
.. authors
.. license