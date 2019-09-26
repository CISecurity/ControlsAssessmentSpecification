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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain an Inventory of Authorized Software
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. The list of approved mobile devices (derived from endpoint inventory; sub-control 1.4)
#. The list of approved mobile device encryption software  (ideally derived from authorized software list; sub-control 2.1)
#. For each software in Input 2, the approved software configuration policy.

Operations
----------
#. For each mobile device in Input 1, determine if any of the approved encryption software from Input 2 is installed.
#. For each mobile device with installed approved encryption software, collect the software configuration information and compare it to the approved configuration policy (Input 3).

Measures
--------
* M1 = List of approved mobile devices
* M2 = Count of M1
* M3 = List of approved mobile devices with approved encryption software installed
* M4 = Count of M3
* M5 = List of approved mobile devices without approved encryption software installed
* M6 = Count of M5
* M7 = List of appropriately configured mobile devices
* M8 = Count of M7
* M9 = List of inappropriately configured mobile devices
* M10 = Count of M9

Metrics
-------

Installed Software Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of approved mobile devices are equipped with approved encryption
	    | software?
	* - **Calculation**
	  - :code:`M4 / M2`

Appropriately Configured Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of approved mobile devices equipped with approved encryption software
	    | meet or exceed the approved configuration policy?
	* - **Calculation**
	  - :code:`M8 / M2`

.. history
.. authors
.. license
