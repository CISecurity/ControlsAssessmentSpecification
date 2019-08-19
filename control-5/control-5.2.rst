5.2: Maintain Secure Images
=========================================================
Maintain secure images or templates for all systems in the enterprise based on the organization’s approved configuration standards.  Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Status
------
Draft

Inputs
------
#. The list of the organization's approved configuration standards, per implementation of sub-control 5.1
#. The inventory of systems
#. The mapping of systems in the inventory to any secure configurations that should be applied. This input assumes that multiple configurations could apply to a single system in the inventory.
#. The inventory of images

Operations
----------
#. For each system in the inventory, determine the list of systems which have had an image taken and the list of systems without a corresponding image.
#. For each system with a corresponding image, compare the image's configuration with the configuration standard(s) mapped to that system.

Measures
--------
* M1 = The number of systems in the inventory
* M2 = The number of systems with a corresponding image taken
* M3 = 1 if an image is configured according to the standards mapped to that system; 0 otherwise.

Metrics
-------

Image Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of systems with a corresponding image taken to the total number of inventoried
	    | systems
	* - **Calculation**
	  - :code:`M2 / M1`

Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of all systems with a corresponding image taken to those configured according
	    | to the standards mapped to that system
	* - **Calculation**
	  - :code:`(SUM from 1..M2 (M3)) / M2`

.. history
.. authors
.. license