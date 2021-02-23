2.2: Ensure Authorized Software is Currently Supported 

===========================================
Ensure that only currently supported software is designated as authorized in the software inventory for enterprise assets. If software is unsupported yet necessary for the fulfillment of the enterprise’s mission, document an exception detailing mitigating controls and residual risk acceptance. For any unsupported software without an exception documentation, designate as unauthorized. Review the software list to verify software support at least monthly, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 1, 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. The authorized software inventory with detailed information. deployment mechanism, and decommission date.
#. Authoritative source of information indicating supported/unsupported details by product.
#. Exception documentation for unsupported software that is necessary for the fulfillment of the enterprise’s mission.
#. Date of last update to the authorized software inventory

Operations
----------
#. For each item in Input 1, perform a lookup in Input 2 to verify supported/unsupported status.
	#. Note each item labeled "unsupported" but "supported based on Input 2 (M2)
	#. Note each item labeled "supported" but is "unsupported" based on Input 2 (M3).
#. Identify and note truly "unsupported" items from Input 1 after conducting Operation 1 (M4).
#. For each unsupported item identifed in Operation 2, conduct a check using Input 3.
	#. Note items that do not have appropriate exception documentation (M5).
	#. Note items that do have appropriate exception documentation (M6).
#. Compare date of last update to the authorized software inventory to the current date and note timeframe in weeks (M7).

Assumptions
--------
#. Authorized software inventory with detailed information exists for the enterprise. 

Measures
--------
* M1 = Count of Input 1
* M2 = Count of items in Input 1 that are mislabeled as unsupported
* M3 = Count of items in Input 1 that are mislabeled as supported
* M4 = Count of unsupported items
* M5 = Count of items in Input 1 with that are no longer supported but exception documentation exists
* M6 = Count of items in Input 1 with that are no longer supported and exception documentation does not exist
* M7 = Timeframe in weeks of last update to the authorized software inventory


Metrics
-------
* If M7 is greater than four, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Percentage of Unsupported Software in Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of authorized software inventory in use is unsupported?
	* - **Calculation**
	  - :code:`M4 / M1`

Rate of False Positives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of software listed as supported is actually not supported?
	* - **Calculation**
	  - :code:`M3 / M1`

Rate of False Negatives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of software listed as unsupported is actually supported?
	* - **Calculation**
	  - :code:`M2 / M1`

Percentage of unsupported software with exception documentation
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of software listed as unsupported but appropriate exception documentation exists?
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license
