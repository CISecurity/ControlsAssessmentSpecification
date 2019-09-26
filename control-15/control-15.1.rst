15.1: Maintain an Inventory of Authorized Wireless Access Points
================================================================
Maintain an inventory of authorized wireless access points connected to the wired network.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Identify
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of wireless access points

Operations
----------
#. Utilize a discovery tool or process to examine the network topology to collect the "ground truth" list of wireless access points connected to the wired network.
#. Evaluate the complement of Input 1 and Operation 1 to obtain the list of non-inventoried wireless access points.
#. Evaluate the intersection of Input 1 and Operation 1 to obtain the list of inventoried wireless access points.
#. Compare the results of Operation 3 to the inventory to determine which access points in the inventory are noted as *not* authorized.

Measures
--------
* M1 = Count of wireless access points in the inventory (from Input 1)
* M2 = List of discovered wireless access points, from Operation 1
* M3 = Count of M2
* M4 = List of non-inventoried wireless access points, as discovered by Operation 2
* M5 = Count of M4
* M6 = List of inventoried wireless access points, as discovered by Operation 3
* M7 = Count of M6
* M8 = List of discovered, but unauthorized, wireless access points, as discovered by Operation 4
* M9 = Count of M8

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of discovered wireless access points to the total inventoried list of
	    | wireless access points.
	* - **Calculation**
	  - :code:`(M3 - M1) / M1`


Inventory Gap
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are there any discovered wireless access points that are *not* contained in the
	    | inventory?
	* - **Calculation**
	  - :code:`M5 > 0`

Unauthorized Usage
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are there any discovered wireless access points which are contained in the
	    | inventory but are noted as *not* authorized?
	* - **Calculation**
	  - :code:`M9 > 0`

.. history
.. authors
.. license
