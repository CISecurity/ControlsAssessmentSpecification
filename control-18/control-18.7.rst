18.7: Apply Static and Dynamic Code Analysis Tools
=========================================================
Apply static and dynamic analysis tools to verify that secure coding practices are being adhered to for internally developed software.

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
#. The inventory of internally-developed software (from the organization's software inventory)
#. The inventory of static analysis tools (from the organization's software inventory)
#. The inventory of dynamic analysis tools (from the organization's software inventory)

Operations
----------
#. Map the inventory of internally-developed software to the applicable static/dynamic analysis tools which are used for verification.

Measures
--------
* M1(i) = (For each software "i" from Input 1) 1 if the software is verified by static analysis tool(s); 0 otherwise
* M2(i) = (For each software "i" from Input 1) 1 if the software is verified by dynamic analysis tool(s); 0 otherwise
* M3 = Count of internally developed software (the count of Input 1)

Metrics
-------

Static Analysis Tool Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of internally developed software verified by static analysis tools to the
	    | total number of internally developed software applications
	* - **Calculation**
	  - :code:`(SUM from i=1..M3 (M1(i))) / M3`


Dynamic Analysis Tool Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of internally developed software verified by dynamic analysis tools to the
	    | total number of internally developed software applications
	* - **Calculation**
	  - :code:`(SUM from i=1..M3 (M2(i))) / M3`

.. history
.. authors
.. license
