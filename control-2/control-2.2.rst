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

Assumptions
-----------
The assumption is that a list of all authorized software is available, and that this list indicates whether or not the software is currently supported by the vendor.

Measures
--------
* M1 = # of authorized software
* M2 = # of tracked software (tagged as supported or unsupported)
* M3 = # of unsupported software in authorized list

Metrics
-------
.. list-table::

	* - **Question**
	  - What percentage of software installed in the enterprise are accounted for, as either supported or unsupported, in the organization's software asset inventory?
	* - **Answer**
	  - Ideally, all software installed in the enterprise should be accounted for, and tagged as either supported or unsupported.  When all authorized software is tracked (when M1 == M2), this metric illustrates the percentage of software tagged as unsupported.
	* - **Calculation**
	  - :code:`((M1 - M3) / M1)`

.. history
.. authors
.. license