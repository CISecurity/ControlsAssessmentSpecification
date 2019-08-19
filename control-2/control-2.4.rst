2.4: Track Software Inventory Information
=========================================================
The software inventory system should track the name, version, publisher, and install date for all software, including operating systems authorized by the organization.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 2, 3

Status
------
Draft

Inputs
------
#. Detailed software inventory

Operations
----------
#. For each entry in the software inventory, including operating systems, identify detailed information such as:
	* Software name (market name)
	* Software version (market version)
	* Software publisher
	* Installation date (timestamp)
#. For each entry in the software inventory, including operating systems, identify authorization state
#. Identify software with all detailed information identified

Measures
--------
* M1 = Count of entries in software inventory
* M2 = Count of entries authorized for installation
* M3 = Count of entries with all detailed information

Metrics
-------

Inventory Quality
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of entries with all detailed information to the total number of entries
	* - **Calculation**
	  - :code:`M3 / M1`

Inventory Authorization Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of entries authorized to be installed to the total number of entries
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license