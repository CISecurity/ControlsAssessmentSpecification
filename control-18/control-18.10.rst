18.10: Deploy Web Application Firewalls
=========================================================
Protect web applications by deploying web application firewalls (WAFs) that inspect all traffic flowing to the web application for common web application attacks. For applications that are not web-based, specific application firewalls should be deployed if such tools are available for the given application type. If the traffic is encrypted, the device should either sit behind the encryption or be capable of decrypting the traffic prior to analysis. If neither option is appropriate, a host-based web application firewall should be deployed.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
-----------
#. The inventory of authorized software

Operations
----------
#. Enumerate all in-house owned and operated software (i.e. applications in the software inventory that are developed in-house and/or acquired) for which there is an application-level firewall technology exists
#. Enumerate all application-level firewalls (including WAF and host-based firewalls)
#. For each application-level firewall, enumerate covered software applications
#. Complement the set of software applications identified in the first operation with the covered software applications

Measures
--------
* M1 = Enumerated list of all software in the inventory for which an application-level firewall technology exists
* M2 = Enumerated list of all application-level firewalls
* M3 = Enumerated list of applications covered by application-level firewalls
* M4 = Enumerated list of applications not covered by software applications (fourth operation)
* M5 = Count of software for which an application-level firewall technology exists (count of M1)
* M6 = Count of application-level firewalls (count of M2)
* M7 = Count of applications covered by application-level firewalls (count of M3)
* M8 = Count of applications not covered by software applications (count of M4)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of the number of applications covered by an application-level firewall to the
	    | number of eligible applications in the enterprise.
	* - **Calculation**
	  - :code:`M7 / M5`

.. history
.. authors
.. license
