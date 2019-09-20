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

Dependencies
------------
* Sub-control 2.3: Utilize Software Inventory Tools

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
* M1 = Count of entries in software inventory (from Input 1)
* M2 = List of entries authorized for installation
* M3 = Count of M2
* M4 = List of entries not authorized for installation
* M5 = Count of M4
* M6 = List of entries with all detailed information
* M7 = Count of M6
* M8 = List of entries without all detailed information
* M9 = Count of M8

Metrics
-------

Inventory Quality
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of entries with all detailed information to the total number of entries
	* - **Calculation**
	  - :code:`M7 / M1`

Inventory Authorization Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of entries authorized to be installed to the total number of entries
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license
