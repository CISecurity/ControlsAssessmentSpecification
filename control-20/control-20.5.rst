20.5: Create a Test Bed for Elements Not Typically Tested in Production
=======================================================================
Create a test bed that mimics a production environment for specific penetration tests and Red Team attacks against elements that are not typically tested in production, such as attacks against supervisory control and data acquisition and other control systems.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	* - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 20.1: Establish a Penetration Testing Program

Inputs
-----------
#. List of penetration tests and Red Team attacks and associated elements that are not typically tested in production (i.e. SCADA systems)
#. Description of test bed(s) that have been setup to mimic these production environments

Operations
----------
#. For each penetration test and Red Team attack in Input 1, manually review the Inputs to see that there is at least one appropriate test bed in Input 2 to cover that test or attack.
	#. Those tests/attacks that have at least one matching test bed will be included in list M1
	#. Those tests/attacks that do not have at least one matching test bed will be included in list M2

Measures
--------
* M1 = List of penetration tests and Red Team attacks that have at least one matching test bed
* M2 = List of penetration tests and Red Team attacks that do not have at least one matching test bed
* M3 = Count of tests/attacks that do have a matching test bed (count of M1)
* M4 = Total count of tests/attacks in Input 1

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of tests/attacks not typically tested in production that have a matching test
	    | bed
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
