3.3: Protect Dedicated Assessment Accounts
===========================================
Use a dedicated account for authenticated vulnerability scans, which should not be used for any other administrative activities and should be tied to specific machines at specific IP addresses.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 2, 3

Status
------
Draft

Assumptions
-----------
It is assumed that a pre-authorized list of scanning managers is known.

Measures
--------
* M1 [0|1]: scanning traffic is between a sanning manager and agent/machine
* M2 [0|1]: scanning managers (senders) are pre-authrized machines/IPs.
* M3 [0|1]: a dedicated account is used by the manager scanning process.
* M4 [0|1]: traffic has been authenticated (as subcontrol 3.2)

Metrics
-------

Designated Accounts
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - Does the enterprise use dedicated accounts for vulnerability scans?
	* - **Answer**
	  - Boolean.
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3 AND M4`

.. history
.. authors
.. license
