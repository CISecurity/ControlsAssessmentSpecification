9.7: Deploy and Maintain Email Server Anti-Malware Protections
=========================================================
Deploy and maintain email server anti-malware protections, such as attachment scanning and/or sandboxing.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network 
	  - Protect
	  - 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
-----------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV3`: Configuration standard

Operations
----------
#. Use :code:`GV1` to identify and enumerate all email servers within the enterprise (M1)
#. For each email server identified in Operation 1, use :code:`GV3` to check if native or external anti-malware protections are configured
	#. Identify and enumerate email servers with configured anti-malware protection (M2)
	#. Identify and enumerate email servers without configured anti-malware protection (M3)

Measures
--------
* M1 = Count of email servers
* M2 = Count of properly configured email servers
* M3 = Count of improperly configured email servers

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of properly configured email servers
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
