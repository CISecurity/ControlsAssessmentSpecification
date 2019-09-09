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

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

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
* M1 = The number of wireless access points in the inventory
* M2 = The number of discovered wireless access points, from Operation 1
* M3 = The number of non-inventoried wireless access points, as discovered by Operation 2
* M4 = The number of inventoried wireless access points, as discovered by Operation 3
* M5 = The number of discovered but non-authorized wireless access points, as discovered by Operation 4

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of discovered wireless access points to the total inventoried list of 
	    | wireless access points.
	* - **Calculation**
	  - :code:`(M2 - M1) / M1`


Inventory Gap
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are there any discovered wireless access points that are *not* contained in the
	    | inventory?
	* - **Calculation**
	  - :code:`M3 > 0`

Unauthorized Usage
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are there any discovered wireless access points which are contained in the 
	    | inventory but are noted as *not* authorized?
	* - **Calculation**
	  - :code:`M5 > 0`

.. history
.. authors
.. license