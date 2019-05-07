CIS Control 6: Maintenance, Monitoring and Analysis of Audit Logs
=================================================================

Collect, manage, and analyze audit logs of events that could help detect, understand,
or recover from an attack.

**Why is this CIS Control Critical?**

Deficiencies in security logging and analysis allow attackers to hide their location, malicious
software, and activities on victim machines. Even if the victims know that their systems have been
compromised, without protected and complete logging records they are blind to the details of
the attack and to subsequent actions taken by the attackers. Without solid audit logs, an attack
may go unnoticed indefinitely and the particular damages done may be irreversible.

Sometimes logging records are the only evidence of a successful attack. Many organizations keep
audit records for compliance purposes, but attackers rely on the fact that such organizations
rarely look at the audit logs, and they do not know that their systems have been compromised.
Because of poor or nonexistent log analysis processes, attackers sometimes control victim
machines for months or years without anyone in the target organization knowing, even though
the evidence of the attack has been recorded in unexamined log files.

.. toctree::
   :maxdepth: 1
   :name: toc-control-6

   6.1: Utilize Three Synchronized Time Sources <control-6.1>
   6.2: Activate Audit Logging <control-6.2>
   6.3: Enable Detailed Logging <control-6.3>
   6.4: Ensure Adequate Storage for Logs <control-6.4>
   6.5: Central Log Management <control-6.5>
   6.6: Deploy SIEM or Log Analytic Tools <control-6.6>
   6.7: Regularly Review Logs <control-6.7>
   6.8: Regularly Tune SIEM <control-6.8>
   
.. history
.. authors
.. license