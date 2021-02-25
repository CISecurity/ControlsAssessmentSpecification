1.2: Address Unauthorized Assets
=======================================

Ensure that a process exists to address unauthorized assets on a weekly basis. The enterprise may choose to remove the asset from the network, deny the asset from connecting remotely to the network, or quarantine the asset.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Respond
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
------
#. :code:`GV1`: Detailed Enterprise Asset Inventory 
#. :code:`GV2`: Unauthorized Assets
#. The enterprise defined time frame for removing unauthorized assets (weekly or more often).

Assumptions
^^^^^^^^^^^
#. If the item is not reachable, it may be reasonable to assume it has been removed from the network and therefore dealt with.

Operations
----------
If the optional disposition list is provided, the checks would be tailored to those dispositions.  For the following, assume no disposition list is available:

#. At the time frame specified by Input 3, for each unauthorized asset in :code:`GV2`, check to see if the asset is present in the updated asset inventory from :code:`GV1`.
#. For those items in :code:`GV2` that are not in :code:`GV1`, scan the network to determine if the item is still reachable on the network.
	#. Enumerate the items from :code:`GV2` that are unreachable (M4)
	#. Enumerate the items from :code:`GV1` that are unreachable (M5)

Measures
--------
* M1 = :code:`GV1`
* M2 = Count of :code:`GV2`
* M3 = Timeframe in days for Input 3
* M4 = Count of items from :code:`GV2` that are unreachable after scan
* M5 = Count of items from :code:`GV1` that are unreachable after scan
 

Metrics
-------
If M3 is greater than seven days, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of unaccounted for, unauthorized assets, to the total assets in the asset
	    | inventory.
	* - **Calculation**
	  - | If the value of M4 is 0, there are no unauthorized assets that remain unaccounted for.
	    | In this case, the value of the metric is 1.  Otherwise, the value is :code:`(M2 - M4) / M2 `

.. history
.. authors
.. license
