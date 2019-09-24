18.4: Only Use Up-to-Date and Trusted Third-Party Components
============================================================
Only use up-to-date and trusted third-party components for the software developed by the organization.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
-----------
#. The list of authorized software
#. Third-party component inventory (possibly from your automated build systems)

Operations
----------
#. Enumerate all third-party components in the inventory
#. For each component, verify:
	#. Latest component is being used
	#. The component is explicitly trusted by the organization
#. Enumerate compliant components
#. Enumerate non-compliant components

Measures
--------
* M1 = List of all third-party components being used
* M2 = List of all third-party components that are up-to-date and explicitly trusted
* M3 = List of all third-party components that are not up-to-date or not explicitly trusted
* M4 = The number of third-party components being used (count of M1)
* M5 = The number of third-party components that are up-to-date and explicitly trusted (count of M2)
* M6 = The number of third-party components that are not up-to-date or not explicitly trusted (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of compliant third-party components to the total number of third-party components
	    | in use
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license