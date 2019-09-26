2.2: Ensure Software is Supported by Vendor
===========================================
Ensure that only software applications or operating systems currently supported and receiving vendor updates are added to the organization’s authorized software inventory.  Unsupported software should be tagged as unsupported in the inventory system.

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
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. ASL: The authorized software list with a notation of "supported" or "unsupported" for each entry (sub-control 2.1)
#. Access to an authoritative source of information indicating supported/unsupported details by product.

Operations
----------
#. For each entry in Input 1, perform a lookup in Input 2 to verify.
#. For each entry in Input 1 labeled "supported", perform a lookup in Input 2.  From these lookups, note the list of authorized software labeled "supported" but are actually not supported based on the authoritative source lookup.
#. For each entry in Input 1 labeled "unsupported", perform a lookup in Input 2.  From these lookups, note the list of authorized software labeled "unsupported" but are actually supported based on the authoritative source lookup.

Measures
--------
* M1 = List of items in the authorized software list that are unsupported (combination of Operation 1 and those initially marked as unsupported in Input 1)
* M2 = Count of M1
* M3 = List of authorized software
* M4 = Count of M3
* M5 = List of items in the authorized software list that are mislabeled as supported
* M6 = Count of M5
* M7 = List of items in the authorized software list that are mislabeled as unsupported
* M8 = Count of M7

* M1 = # of items in Input 1 that are unsupported (combination of Operation 1 results and those initially marked as unsupported in Input 1)
* M2 = Total # of authorized software (from Input 1)
* M3 = The number of items from Input 1 labeled "supported" but are actually not supported (from Operation 2)
* M4 = The number of items from Input 1 labeled "unsupported" but are actually supported (from Operation 3)

Metrics
-------

Percentage of Unsupported Software in Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of authorized software in use is unsupported?
	* - **Calculation**
	  - :code:`(M4 - M2) / M4`

Rate of False Positives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of software listed as supported is actually not supported?
	* - **Calculation**
	  - :code:`(M4 - M5) / M4`

Rate of False Negatives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of software listed as unsupported is actually supported?
	* - **Calculation**
	  - :code:`(M4 - M8) / M4`

.. history
.. authors
.. license
