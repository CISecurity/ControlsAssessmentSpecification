14.4: Encrypt All Sensitive Information in Transit
=========================================================
Encrypt all sensitive information in transit.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 13.1: Maintain an Inventory of Sensitive Information

Inputs
-----------
#. Inventory of Sensitive Information (for each type of information listed in the inventory, include a description of how the encryption of this information in transit is accomplished, along with a list of the components used to achieve that encryption)
#. Approved configuration(s) for each of the components identified in Input 1

Operations
----------
#. For each type of sensitive information listed in the inventory provided in Input 1, check each of the components used to encrypt that information in transit against the appropriate approved configuration(s) in Input 2.
#. Create a list of the sensitive information types for which all of the associated components are properly configured (M1) noting which configurations they were checked against.
#. Create a list of sensitive information types for which at least one of the associated components was not properly configured (M2) noting which configurations they were checked against and any deviations from the approved configurations.

Measures
--------
* M1 = List of sensitive information types for which all associated components were properly configured (compliant list)
* M2 = List of sensitive information types for which at least one associated component was not properly configured (non-compliant list)
* M3 = Count of compliant sensitive information types (count of M1)
* M4 = Total count of sensitive information types (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of sensitive information types properly configured to be encrypted in
	    | transit to the total set of sensitive information types.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
