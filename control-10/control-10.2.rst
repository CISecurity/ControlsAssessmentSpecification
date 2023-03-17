10.2: Configure Automatic Anti-Malware Signature Updates
======================================
Configure automatic updates for anti-malware signature files on all enterprise assets.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 10.1: Deploy and Maintain Anti-Malware Software


Inputs
-----------
#. :code:`GV30`: Assets capable of supporting anti-malware software
#. :code:`GV31`: Assets with at least one authorized anti-malware software intalled
#. :code:`GV3`: Configuration standards

Operations
----------
#. For each asset in Input 2 :code:`GV31`, check configurations :code:`GV3` to determine if anti-malware software is configured to autmatically update signature files
	#. Identify and enumerate assets properly configured for automatic updates (M2)
	#. Identify and enumerate asets not properly configured for automatic updates (M3)

Measures
--------
* M1 = Count of :code:`GV30`
* M2 = Count of assets configured to automatically update signature files
* M3 = Count of assets not configured to automatically update signature files


Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly configured to automatically
	  - | update signaure files
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
