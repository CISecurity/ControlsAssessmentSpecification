1.1: Utilize an Active Discovery Tool
=====================================

Utilize an active discovery tool to identify devices connected to the organization’s network and update the hardware asset inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 2, 3

Status
------
Draft

Inputs
-----------
#. The hardware asset inventory
#. The asset discovery tool(s) used by the organization
#. The most recent scan results from the asset discovery tool(s)
#. Configuration information for the asset discovery tool(s)
#. Approved configuration(s) to all tools to interface wtih the hardware asset inventory

Assumptions
^^^^^^^^^^^
#. The asset discovery tools on the provided list are active asset discovery tools, as opposed to passive asset discovery tools (verification of this is not performed during the following operations).
#. The asset discovery tools are used regularly (this is not verified during the following operations).

Operations
----------
#. Create a list of the assets discovered by the tools by enumerating the assets from the scans provided in I3, and creating a union of those enumerations (this list of discovered assets will be M1).
#. Use M1 and I1 to generate the list of assets that are on the Hardware Asset Inventory but were not discovered by any of the tools (this list will be M2).
#. Using the information in I4, check the configuration information of each tool against the appropriate approved configuration from I5 to verify that the tool is capable of interfacing with the hardware asset inventory to make automatic updates. Create a list of those tools that are compliant (M3), and a list of those that are not (M4).

Measures
--------
* M1 = List of discovered assets
* M2 = List of undiscovered assets
* M3 = List of compliant tools
* M4 = List of non-compliant tools
* M5 = Count of discovered assets (count of M1)
* M6 = Count of compliant tools (count of M3)
* M7 = Total count of hardware assets (count of Input 1)
* M8 = Total count of asset discovery tools (count of Input 2)

Metrics
-------
* If M8 is 0, then this Sub-Control receives a failing score and the other metrics don't apply.

Asset Discovery Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Asset Discovery Coverage
	* - **Calculation**
	  - :code:`M5 / M7`

Tool Compliance Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Tool Compliance Ratio
	* - **Calculation**
	  - :code:`M6 / M8`

.. history
.. authors
.. license