1.1: Establish and Maintain Detailed Enterprise Asset Inventory
=====================================

Establish and maintain an accurate, detailed, and up-to-date inventory of all enterprise assets with the potential to store or process data, to include: end-user devices (including portable and mobile), network devices, non-computing/IoT devices, and servers. Ensure the inventory records the network address (if static), hardware address, machine name, data asset owner, department for each asset, and whether the asset has been approved to connect to the network. For mobile end-user devices, MDM type tools can support this process, where appropriate. This inventory includes assets connected to the infrastructure physically, virtually, remotely, and those within cloud environments. Additionally, it includes assets that are regularly connected to the enterprise’s network infrastructure, even if they are not under control of the enterprise. Review and update the inventory of all enterprise assets bi-annually, or more frequently.

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
#. Detailed Enterprise Asset Inventory - The organizations list of current approved inventory to include all assests as outlined in the safeguard. This list is a mix of manual and tool-generated endpoints that includes information such as authorized, non-authorized, IP address, device type and any other information as defined by the enterprise.
#. Bi-annual Aggregate Enterprise Asset Inventory - The organizations list gathering all all devices detected over the time period, manually or automated, preferrably not from a single scan. At a minimum twice a year but can be more frequent.
#. A write up of the procedure for adding or removing enterprise assets to or from the Detailed Enterprise Asset Inventory along with the required fields as part of the detail.
#. Date of last update to the Detailed Enterprise Asset Inventory

Assumptions
^^^^^^^^^^^
#. The asset discovery tools on the provided list are active asset discovery tools, as opposed to passive asset discovery tools (verification of this is not performed during the following operations).
#. The asset discovery tools are used regularly (this is not verified during the following operations).

Operations
----------
#. If Input 2 is not provided, no true accuracy measurement can be made for this safeguard.
#. If Input 3 is greater than six months, this safeguard is measured at a 0.
#. Calculate the intersection of Input 1 and Input 2, noting items in Input 1 that are not in Input 2 (M 3) and items in Input 2 not in Input 1 (M 1).
#. Identify and note items in Input 1 that lack any detailed information or information is incomplete (M 4).
#. Calculate the time (in months) since the last update to Input 1 by using current date and Input 4 (M 6).

Measures
--------
* M1 = Count of items in Input 1
* M2 = Count of items in Input 2
* M3 = Count of items in the intersection of Input 1 and Input 2
* M4 = Count of items in Input 1 not found in Input 2
* M5 = Count of items in Input 2 not found in Input 1
* M6 = Count of items in Input 1 that do not contain detailed information
* M7 = Months since the last update to Input 1

Metrics
-------
* If M1 is not provided or available, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
* If M7 is greater than six months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Accuracy Score
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of the Bi-annual aggregate endpoint inventory is accounted for in the current enterprise asset inventory?
	* - **Calculation**
	  - :code:`M3 / M2`
	* - **Metric**
	  - | What percentage of the current enterprise asset inventory contained necessary detailed information?
	* - **Calculation**
	  - :code:`M6 / M1`

Procedural Review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Manual review/rating of the inventory procedures, to include adding and removing assets, and the time allowable or expected, after acquisition or disposal of assets.

.. history
.. authors
.. license
