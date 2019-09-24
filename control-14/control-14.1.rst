14.1: Segment the Network Based on Sensitivity
=========================================================
Segment the network based on the label or classification level of the information stored on the servers, locate all sensitive information on separated Virtual Local Area Networks (VLANs).

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 13.1: Maintain an Inventory of Sensitive Information

Inputs
-----------
#. Sensitive Information Inventory including which systems store, process, or transmit that sensitive information.
#. Network Architecture information outlining network separation including VLANs

Assumption
^^^^^^^^^^
* A system's overall sensitivity level shall be the highest sensitivity level of the data it stores/processes/transmits. If a system contains any sensitive information, that system should be treated accordingly, and should be properly separated from networks or network segments that don't have a need to access that type of sensitive information.

Operations
----------
#. For each system that stores, processes, or transmits sensitive information identified in Input 1, use the information in Input 2 to identify any networks/VLANs the system is connected to and ensure that each of those networks/VLANs are adequately separated from less sensitive networks (note: this might be a manual review).
#. Use these results to create a list of systems that are adequately separated from less sensitive networks (M1)
#. Use these results to create a list of systems that are not adequately separated (M2) noting the less sensitive networks that they are connected to.

Measures
--------
* M1 = List of sensitive systems that are adequately separated from less sensitive networks (compliant list)
* M2 = List of sensitive systems that are not adequately separated from less sensitive networks (non-compliant list)
* M3 = Count of sensitive systems that are adequately separated from less sensitive networks (count of M1)
* M4 = Total count of sensitive systems (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of adequately separated sensitive systems to the total number of sensitive
	    | systems.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
