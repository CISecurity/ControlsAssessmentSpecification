15.2: Detect Wireless Access Points Connected to the Wired Network
==================================================================
Configure network vulnerability scanning tools to detect and alert on unauthorized wireless access points connected to the wired network.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
-----------
#. The list of network vulnerability scanning tools
#. Approved configuration(s) for detecting unauthorized wireless access points (WAPs)
#. Approved configuration(s) for alerting on unauthorized wireless access points (WAPs)

Operations
----------
#. For each network vulnerability scanning tool in Input 1, check its configuration against the appropriate approved detection configuration in Input 2.
#. Make a list of those network vulnerability scanning tools that are configured correctly for detecting unauthorized WAPs (M1)
#. Make a list of those that are not configured correctly (M2) noting the deviations.
#. For each network vulnerability scanning tool in Input 1, check its configuration against the appropriate approved alerting configuration in Input 3.
#. Make a list of those network vulnerability scanning tools that are configured correctly for alerting on unauthorized WAPs (M3)
#. Make a list of those that are not configured correctly (M4) noting the deviations.

Measures
--------
* M1 = List of network vulnerability scanning tools correctly configured for detecting unauthorized WAPs
* M2 = List of network vulnerability scanning tools not correctly configured for detecting unauthorized WAPs
* M3 = List of network vulnerability scanning tools correctly configured for alerting on unauthorized WAPs
* M4 = List of network vulnerability scanning tools not correctly configured for alerting on unauthorized WAPs
* M5 = Count of network vulnerability scanning tools correctly configured for detecting unauthorized WAPs (count of M1)
* M6 = Count of network vulnerability scanning tools correctly configured for alerting on unauthorized WAPs (count of M3)
* M7 = Total count of network vulnerability scanning tools (count of Input 1)
* M8 = List of network vulnerability scanning tools correctly configured for both detecting and alerting on unauthorized WAPs (intersection of M1 and M3)
* M9 = Count of network vulnerability scanning tools correctly configured for both detecting and alerting on unauthorized WAPs (count of M8)

Metrics
-------

Detection Coverage
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network vulnerability scanning tools correctly configured for detecting
	    | unauthorized WAPs
	* - **Calculation**
	  - :code:`M5 / M7`

Alerting Coverage
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network vulnerability scanning tools correctly configured for alerting
	    | on unauthorized WAPs
	* - **Calculation**
	  - :code:`M6 / M7`

Full Coverage
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network vulnerability scanning tools correctly configured for both
	    | detecting and alerting on unauthorized WAPs
	* - **Calculation**
	  - :code:`M9 / M7`

.. history
.. authors
.. license
