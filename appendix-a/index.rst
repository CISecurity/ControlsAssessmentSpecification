Appendix A: Global Variable Listing
===================================

Several observables or artifacts specified by this document are used across two or more Sub-Controls, and from time to time across two or more top-level Controls. We have made every attempt to identify such global variables and list them here in the table below.

Global variables are denoted by a concatenation of :code:`GV` and a positive integer. For example, the Hardware Asset Inventory is identified by :code:`GV1`. The table below provides each global variable's identifier, name, description, source Sub-Control (when applicable), and any relevant notes.

We encourage you to report any missed global variables by creating a GitHub issue in our publicly available repository TODO: LINK.

.. list-table::
	:header-rows: 1

	* - Identifier
	  - Name
	  - Description
    - Source Sub-Control (if applicable)
    - Notes
	* - GV1
	  - Hardware Asset Inventory
	  - The collection of hardware assets managed by the enterprise.
    - 1.1
    - The hardware asset inventory is intended to include physical and virtual hardware and what is commonly referred to in the CIS Controls as systems.
  * - GV2
    - Count of Hardware Asset Inventory
    - The count of the collection of hardware assets managed by the enterprise.
    - N/A
    - None


.. history
.. authors
.. license
