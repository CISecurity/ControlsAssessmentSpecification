1.3: Utilize an Active Discovery Tool
=========================================================
Utilize an active discovery tool to identify assets connected to the enterprise’s network. Configure the active discovery tool to execute daily, or more frequently.


.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure

Inputs
-----------
#. The Detailed Enterprise Asset Inventory
#. The list of active discovery tool(s) used by the enterprise
#. List consisting of the union from scan results conducted using all active asset discovery tool(s) within the enterprise (discovered assets).
#. Timeframe between two active asset discovery tool scans.
#. Configuration information for the active asset discovery tools.
#. Approved configurations for all active asset discovery tools that interface with the Detailed Enterprise Asset Inventory.

Operations
----------
#. Identify enterprise assets not discovered by the active discovery tools by comparing Input 1 and Input 3 (M2).
#. Using the configuration information in Input 4, check the approved configurations from Input 5 to verify that the tools are capable of interfacing with the asset inventory to make automatic updates. 
	#. Create a list of those tools that are compliant (M3)
	#. Create a list of those that are not compliant (M4).

Assumptions
^^^^^^^^^^^
* The asset discovery tools on the provided list are active asset discovery tools, as opposed to passive asset discovery tools (verification of this is not performed during the following operations).

Measures
--------
* M1 = Count of all discovered assets from Input 3
* M2 = Count of undiscovered assets
* M3 = Count of properly configured tools
* M4 = Count of improperly configured tools
* M5 = Count of Input 2
* M6 = Count of Input 1
* M7 = Timeframe in hours for Input 4

Metrics
-------
* If M7 is greater than 24 hours, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
* If M5 is 0, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Asset Discovery Coverage
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Asset Discovery Coverage
	* - **Calculation**
	  - :code:`M1 / M6`

Tool Compliance Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Tool Compliance Ratio
	* - **Calculation**
	  - :code:`M3 / M2`

.. history
.. authors
.. license
