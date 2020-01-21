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

Dependencies
------------
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. :code:`GV1`: The hardware asset inventory
#. :code:`GV3`: The asset discovery tool(s) used by the organization - derived from :code:`GV12`, Software Inventory
#. The most recent scan results from the asset discovery tool(s)
#. Configuration information for the asset discovery tool(s) - derived from :code:`G8`, Approved Security Configurations
#. Approved configuration(s) to all tools to interface with the hardware asset inventory (may be derived from :code:`GV8`)
# :code:`GV2`: Count of Hardware Assets

Assumptions
^^^^^^^^^^^
#. The asset discovery tools on the provided list are active asset discovery tools, as opposed to passive asset discovery tools (verification of this is not performed during the following operations).
#. The asset discovery tools are used regularly (this is not verified during the following operations).

Operations
----------
#. Create a list of the assets discovered by the tools by enumerating the assets from the scans provided by Input 3, and creating a union of those enumerations (becomes M1).
#. Use M1 and Input 1 (:code:`GV1`) to generate the list of assets that are on the Hardware Asset Inventory but were not discovered by any of the tools (becomes M2).
#. Using the information in Input 4
  #. Check the configuration information of each tool against the appropriate approved configuration from Input 5 to verify that the tool is capable of interfacing with the hardware asset inventory to make automatic updates.
	#. Create a list of those tools that are compliant (becomes M3), and a list of those that are not (becomes M4). We recommend noting why each tool included as part of M4 has been included.

Measures
--------
* M1 = List of discovered assets
* M2 = List of undiscovered assets
* M3 = List of compliant tools
* M4 = List of non-compliant tools
* M5 = Count of discovered assets (count of M1)
* M6 = Count of compliant tools (count of M3)
* M7 = Total count of asset discovery tools (count of Input 2 (:code:`GV3`))

Metrics
-------
* If M8 is 0, then this Sub-Control receives a failing score and the other metrics don't apply.

Asset Discovery Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Asset Discovery Coverage
	* - **Calculation**
	  - :code:`M5 / GV2`

Tool Compliance Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Tool Compliance Ratio
	* - **Calculation**
	  - :code:`M6 / M7`

.. history
.. authors
.. license
