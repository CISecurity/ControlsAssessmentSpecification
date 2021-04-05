12.3: Securely Manage Network Infrastructure
=========================================================
Securely manage network infrastructure. Example implementations include version-controlled-infrastructure-as-code, and the use of secure network protocols, such as SSH and HTTPS. 

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure
* Safeguard 12.4: Establish and Maintain Architecture Diagram(s)

Inputs
-----------
#. :code:`GV36`: Segments within the enterprise network
#. :code:`GV35`: Assets that are part of the network infrastructure
#. :code:`GV37`: Network architectrure configuration standards

Operations
----------
#. For each asset in Input 2 :code:`GV35`, use Input 3 :code:`GV37` to check for the use of encrypted sessions
	#. Identify and enumerate assets using encrypted sessions (M2)
	#. Identify and enumerate assets not using encrypted sessions (M3)
#. For each network segment in Input 1 :code:`GV36`, check for the use of infrastructure-as-code
	#. Identify and enumerate network segments that use infrastructure-as-code for the whole segment or partial (M5)
	#. Identify and enumerate network segments that do not use infrastructure-as-code for any portion of the segment (M6)
#. For each network segements identified in Operation 1, use Input 3 :code:`GV37` to determine whether the infrastructure-as-code is managed using version control
	#. Identify and enumerate network segments covered by version controlled infrastructure-as-code (M7)
	#. Identify and enumerate network segments covered by infrastructure-as-code not managed through version control (M8)

Measures
--------
* M1 = Count of :code:`GV35` assets that are part of the network infrastructure
* M2 = Count of network infrastructure assets using encrypted sessions
* M3 = Count of network infrastructure assets not using encrypted sessions
* M4 = Count of :code:`GV36` segments within the enterprise network
* M5 = Count of network segments using infrastructure-as-code
* M6 = Count of network segements not using infrastructure-as-code
* M7 = Count of network segments covered by version controlled infrastructure-as-code
* M8 = Count of network sgements covered by unmanaged infrastructure-as-code

Metrics
-------

Encrypted Session Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of network infrastructure assets using encrypted sessions
	* - **Calculation**
	  - :code:`M2 / M1`

Infrastructure-As-Code Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of network segments covered by version controlled 
	  - | infrastructure-as-code
	* - **Calculation**
	  - :code:`M7 / M4`

.. history
.. authors
.. license
