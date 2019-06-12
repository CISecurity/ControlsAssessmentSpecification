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
#. Access to a database containing supported/unsupported information by product.

Operations
----------
#. For each entry in Input 1 that is labeled "supported", perform a lookup in Input 2 to verify.

Measures
--------
* M1 = # of items in Input 1 that are unsupported (combination of Operation 1 results and those initially marked as unsupported in Input 1)
* M2 = Total # of authorized software (from Input 1)

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

.. history
.. authors
.. license