13.6: Encrypt Mobile Device Data
=========================================================
Utilize approved cryptographic mechanisms to protect enterprise data stored on all mobile devices.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of approved mobile devices
#. The list of approved mobile device encryption software
#. For each software in Input 2, the approved software configuration policy.

Operations
----------
#. For each mobile device in Input 1, determine if any of the approved encryption software from Input 2 is installed.
#. For each mobile device with installed approved encryption software, collect the software configuration information and compare it to the approved configuration policy (Input 3).

Measures
--------
* M1 = The number of approved mobile devices
* M2 = The number of approved mobile devices with approved encryption software installed, per Operation 1.
* M3 = The number of devices from M2 with configuration matching or exceeding the approved configuration policy.

Metrics
-------

Installed Software Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of approved mobile devices are equipped with approved encryption
	    | software?
	* - **Calculation**
	  - :code:`M2 / M1`

Appropriately Configured Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of approved mobile devices equipped with approved encryption software
	    | meet or exceed the approved configuration policy?
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license