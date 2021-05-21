1.1: Establish and Maintain Detailed Enterprise Asset Inventory
=====================================

Establish and maintain an accurate, detailed, and up-to-date inventory of all enterprise assets with the potential to store or process data, to include: end-user devices (including portable and mobile), network devices, non-computing/IoT devices, and servers. Ensure the inventory records the network address (if static), hardware address, machine name, enterprise asset owner, department for each asset, and whether the asset has been approved to connect to the network. For mobile end-user devices, MDM type tools can support this process, where appropriate. This inventory includes assets connected to the infrastructure physically, virtually, remotely, and those within cloud environments. Additionally, it includes assets that are regularly connected to the enterprise’s network infrastructure, even if they are not under control of the enterprise. Review and update the inventory of all enterprise assets bi-annually, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV1`: Detailed Enterprise Asset Inventory - The enterprise's list of current approved inventory to include all assests as outlined in the safeguard. This list is a mix of manual and tool-generated endpoints that includes information such as authorized, non-authorized, IP address, device type and any other information as defined by the enterprise.
#. Aggregate Enterprise Asset Inventory - The enterprise's list of all devices detected, manually or through automated scans, since the last update to :code:`GV1`. 
#. Date of last update to the Detailed Enterprise Asset Inventory

Assumptions
^^^^^^^^^^^
#. Devices belonging to the organization, but not connected to the organization’s network, require manual discovery in order to be included in the aggregate inventory.

Operations
----------
#. Calculate the intersection of :code:`GV1` and Input 2
	#. Enumerate items in :code:`GV1` that are not in Input 2 (M4) 
	#. Enumerate items in Input 2 not in Input 1 (:code:`GV2`: M5). These assets are considered unauthorized. 
#. Check items in Input 1 for complete or missing detailed information
	#. Enumerate items that have complete information (M6)
	#. Enumerate items that do not have complete information or missing information (M7).
#. Calculate the time (in months) since the last update to Input 1 by using current date and Input 4 (M8).

Measures
--------
* M1 = :code:`GV1`
* M2 = Count of items in Input 2
* M3 = Count of items in the intersection of :code:`GV1` and Input 2
* M4 = Count of items in :code:`GV1` not found in Input 2
* M5 = :code:`GV2`
* M6 = Count of items in :code:`GV1` that contain all necessary detailed information
* M7 = Count of items in :code:`GV1` that do not contain detailed information
* M8 = Months since the last update to :code:`GV1`

Metrics
-------
* If M1 is not provided or available, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
* If M8 is greater than six months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Accuracy Score
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of the aggregate endpoint inventory is accounted for in the current enterprise asset inventory?
	* - **Calculation**
	  - :code:`M3 / M2`

Completeness Score
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of the current enterprise asset inventory contains necessary detailed information?
	* - **Calculation**
	  - :code:`M8 / M1`

Procedural Review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Manual review/rating of the inventory procedures, to include adding and removing assets, and the time allowable or expected, after acquisition or disposal of assets.

.. history
.. authors
.. license
