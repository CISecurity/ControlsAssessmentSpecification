12.6: Use of Secure Network Management and Communication Protocols 
=========================================================
Use secure network management and communication protocols (e.g., 802.1X, Wi-Fi Protected Access 2 (WPA2) Enterprise or greater).

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
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure
* Safeguard 12.2: Establish and Maintain a Secure Network Architecture

Inputs
-----------
#. :code:`GV36`: Segments within the enterprise network
#. :code:`GV37`: Network infrastructure configuration standards
#. Authorized list of secure network management and communication protocols

Operations
----------
#. For each network segment in Input 1 :code:`GV36`, use Input 3 to identify communication protocols 
	#. Identify and enumerate segments using only communication protocols on the authorized list (M2)
	#. Identify and enumerate segments using communication protocols not on the authorized list (M3)
#. For each communication protocol identified in Operation 1.1, check configuration standards :code:`GV37`
	#. Identify and enumerate segments using properly configured communication protocols (M4)
	#. Identify and enumerate segments using improperly configured communication protocols (M5)
#. For each network segment in Input 1 :code:`GV36`, use Input 3 to identify network management protocols 
	#. Identify and enumerate segments using only network management protocols on the authorized list (M6) 
	#. Identify and enumerate segments using network management protocols not on the authorized list (M7)
#. For each communication protocol identified in Operation 1.1, check configuration standards :code:`GV37`
	#. Identify and enumerate segments using properly configured network management protocols (M8)
	#. Identify and enumerate segments using improperly configured network management protocols (M9)

Measures
--------
* M1 = Count of :code:`GV36`
* M2 = Count of segments using authorized communication protocols
* M3 = Count of segments using unauthorized communication protocols
* M4 = Count of segments using properly configured authorized communication protocols
* M5 = Count of segments using improperly configured authorized communication protocols
* M6 = Count of segments using unauthorized network management protocols
* M7 = Count of segments using unauthorized network management protocols
* M8 = Count of segments using properly configured authorized network management protocols
* M9 = Count of segments using improperly configured authorized network management protocols

Metrics
-------

Communication Protocol Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of network segments using properly configured 
 	  - | and authorized communication protocols
	* - **Calculation**
	  - :code:`M4 / M1`

Network Managememt Protocol Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of network segments using properly configured 
 	  - | and authorized network management protocols
	* - **Calculation**
	  - :code:`M8 / M1`

.. history
.. authors
.. license
