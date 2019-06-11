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
In Development

Inputs
------
#. The assumption is that a list of all authorized software is available, and that this list indicates whether or not the software is currently supported by the vendor.

Operations
----------
#. 

Measures
--------
* M = The list of software maintained in the software asset inventory (See control 2.1)
* M1 = # of unsupported software
* M2 = # of supported software
* M(U) = 1 if a software asset U is unsupported, but tracked as supported in M
* M(S) = 1 if a software asset S is supported, but tracked as unsupported in M

Metrics
-------

Supported Software Accuracy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to determine the ratio of software tracked as supported
	    | in the software inventory, but is not supported by the vendor.
	* - **Answer**
	  - | The calculation of this metric is made by summing the M(U) value for each software
	    | asset tracked in M, and the associated ratio of that sum to the # of unsupported
	    | software in the enterprise (M1).
	* - **Calculation**
	  - :code:`(SUM of all M(U) for all U) / M1`

Unsupported Software Accuracy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to determine the ratio of software tracked as unsupported
	    | in the software inventory, but is still supported by the vendor.
	* - **Answer**
	  - | The calculation of this metric is made by summing the M(S) value for each software
	    | asset tracked in M, and the associated ratio of that sum to the # of supported software
	    | in the enterprise (M2).
	* - **Calculation**
	  - :code:`(SUM of all M(S)) for all U) / M2`

.. history
.. authors
.. license