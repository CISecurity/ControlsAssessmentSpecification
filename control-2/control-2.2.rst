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

Status
------
Draft

Inputs
------
#. The authorized software list with a notation of "supported" or "unsupported" for each entry.
#. Access to an authoritative source of information indicating supported/unsupported details by product.

Operations
----------
#. For each entry in Input 1, perform a lookup in Input 2 to verify.
#. For each entry in Input 1 labeled "supported", perform a lookup in Input 2.  From these lookups, note the list of authorized software labeled "supported" but are actually not supported based on the authoritative source lookup.
#. For each entry in Input 1 labeled "unsupported", perform a lookup in Input 2.  From these lookups, note the list of authorized software labeled "unsupported" but are actually supported based on the authoritative source lookup.

Measures
--------
* M1 = # of items in Input 1 that are unsupported (combination of Operation 1 results and those initially marked as unsupported in Input 1)
* M2 = Total # of authorized software (from Input 1)
* M3 = The number of items from Input 1 labeled "supported" but are actually not supported (from Operation 2)
* M4 = The number of items from Input 1 labeled "unsupported" but are actually supported (from Operation 3)

Metrics
-------

Percentage of Unsupported Software in Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of authorized software in use is unsupported?
	* - **Answer**
	  - | The calculation of this metric is determined by the ratio of 
	    | unsupported software to the total authorized software in use.
	* - **Calculation**
	  - :code:`(M2 - M1) / M2`

Rate of False Positives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of software listed as supported is actually not supported?
	* - **Answer**
	  - | The calculation of this metric is determined by the ratio of software labeled
	    |  "supported" but found to be unsupported, to the total authorized software in use.
	* - **Calculation**
	  - :code:`(M2 - M3) / M2`

Rate of False Negatives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of software listed as unsupported is actually supported?
	* - **Answer**
	  - | The calculation of this metric is determined by the ratio of software labeled
	    |  "unsupported" but found to be supported, to the total authorized software in use.
	* - **Calculation**
	  - :code:`(M2 - M4) / M2`

.. history
.. authors
.. license