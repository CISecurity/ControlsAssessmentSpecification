11.6: Use Dedicated Workstations for All Network Administrative Tasks
=====================================================================
Ensure network engineers use a dedicated machine for all administrative tasks or tasks requiring elevated access. This machine shall be segmented from the organization’s primary network and not be allowed Internet access.  This machine shall not be used for reading email, composing documents, or surfing the Internet.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The set of devices used for administrative purposes
#. The access control configuration

Operations
----------
N/A

Measures
--------
* M1(i) = (For each machine "i") 1 if an administrative device has internet access; 0 otherwise.
* M2(i) = (For each machine "i") 1 if administrative device can run any application that is not administrative; 0 otherwise.
* M3 = Count of administrative devices

Metrics
-------

Administrative Device Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of improperly configured administrative devices to the total number of
	    | administrative devices.
	* - **Calculation**
	  - :code:`(SUM from i=1..M3 (M1(i) AND M2(i))) / M3`

.. history
.. authors
.. license
