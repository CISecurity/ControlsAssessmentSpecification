CIS Control 8: Audit Log Management
=======================================================

Collect, alert, review, and retain audit logs of events that could help detect, understand, or recover from an attack.

**Why is this CIS Control Critical?**

Log collection and analysis is critical for an enterprise’s ability to detect malicious activity quickly. Sometimes audit records are the only evidence of a successful attack. Attackers know that many enterprises keep audit logs for compliance purposes, but rarely analyze them. Attackers use this knowledge to hide their location, malicious software, and activities on victim machines. Due to poor or nonexistent log analysis processes, attackers sometimes control victim machines for months or years without anyone in the target enterprise knowing.

There are two types of logs that are generally treated and often configured independently: system logs and audit logs. System logs typically provide system-level events that show various system process start/end times, crashes, etc. These are native to systems, and take less configuration to turn on. Audit logs typically include user-level events – when  a user logged in, accessed a file, etc. – and take more planning and effort to set up.

Logging records are also critical for incident response. After an attack has been detected, log analysis can help enterprises understand the extent of an attack. Complete logging records can show, for example, when and how the attack occurred, what information was accessed, and if data was exfiltrated. Retention of logs is also critical in case a follow-up investigation is required or if an attack remained undetected for a long period of time.


.. toctree::
   :maxdepth: 1
   :name: toc-control-8

   8.1: Establish and Maintain an Audit Log Management Process <control-8.1>
   8.2: Collect Audit Logs <control-8.2>
   8.3: Ensure Adequate Audit Log Storage <control-8.3>
   8.4: Standardize Time Synchronization <control-8.4>
   8.5: Collect Detailed Audit Logs <control-8.5>
   8.6: Collect DNS Query Audit Logs <control-8.6>
   8.7: Collect URL Request Audit Logs <control-8.7>
   8.8: Collect Command-Line Audit Logs <control-8.8>
   8.9: Centralize Audit Logs <control-8.9>
   8.10: Retain Audit Logs <control-8.10>
   8.11: Conduct Audit Log Reviews <control-8.11>
   8.12 Collect Service Provider Logs <control-8.12>

.. history
.. authors
.. license
