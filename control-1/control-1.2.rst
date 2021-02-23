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
#. Detailed Enterprise Asset Inventory from Safeguard 1.1
#. The list of discovered assets in the Aggregate Enterprise Asset Inventory that are not authorized (not in the Updated Enterprise Asset Inventory). 
#. The enterprise defined time frame for removing unauthorized assets (weekly or more often).

Assumptions
^^^^^^^^^^^
If the item is not reachable, it may be reasonable to assume it has been removed from the network and therefore dealt with.

Operations
----------
If the optional disposition list is provided, the checks would be tailored to those dispositions.  For the following, assume no disposition list is available:

#. At the time frame specified by Input 3, for each unauthorized asset in Input 2, check to see if the asset is present in the updated asset inventory from Input 1.
#. For those items in Input 2 that are not in Input 1, scan the network to determine if the item is still reachable on the network.

Measures
--------
* M1 = Count of Input 1
* M2 = Count of Input 2
* M3 = Timeframe in days for Input 3
* M4 = Count of items in Input 1 that are unreachable
* M5 = Count of items in Input 2 that are unreachable
 

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
	  - | If the value of M5 is 0, there are no unauthorized assets that remain unaccounted for.
	    | In this case, the value of the metric is 1.  Otherwise, the value is :code:`(M1 - M5) / M5`

.. history
.. authors
.. license
