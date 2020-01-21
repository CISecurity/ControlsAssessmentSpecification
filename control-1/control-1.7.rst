1.7: Deploy Port Level Access Control
=========================================================
Utilize port level access control, following 802.1x standards, to control which devices can authenticate to the network. The authentication system shall be tied into the hardware asset inventory data to ensure only authorized devices can connect to the network.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Assumptions
^^^^^^^^^^^
#. Use of an 802.1x network design to control network access
#. The 802.1x system can query the endpoint inventory system
#. The CMDB is a separate entity from the authentication server.

Inputs
------
#. List of 802.1x authenticators
#. List of 802.1x authentication servers (i.e. RADIUS/Diameter servers)
#. List of CMDB servers

Operations
----------
#. For each 802.1x authenticator, ensure proper configuration (becomes M5), noting those that are not appropriately configured (becomes M3) and why
#. For each 802.1x authentication server, ensure proper configuration, including connection to at least one CMDB server (becomes M9), and noting those that are not appropriately configured (becomes M7) and why

Measures
--------
* M1 = Boolean: 802.1x authenticators are in use
* M2 = Boolean: 802.1x authentication servers are in use
* M3 = List of inappropriately configured 802.1x authenticators
* M4 = Count of inappropriately configured 802.1x authenticators (count of M3)
* M5 = List of appropriately configured 802.1x authenticators
* M6 = Count of appropriately configured 802.1x authenticators (count of M5)
* M7 = List of inappropriately configured 802.1x authentication servers
* M8 = Count of inappropriately configured 802.1x authentication servers (count of M7)
* M9 = List of appropriately configured 802.1x authentication servers
* M10 = Count of appropriately configured 802.1x authentication servers (count of M9)
* M11 = Count of 802.1x authentication servers (from Input 2)
* M12 = Count of 802.1x authenticators (from Input 1)

Metrics
-------

802.1x Deployment
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Is 802.1x deployed?
	* - **Calculation**
	  - :code:`M1 AND M2`

Authenticator Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of improperly configured 802.1x authenticators to total number of 802.1x
	    | authenticators
	* - **Calculation**
	  - :code:`M4 / M12`

Authentication Server Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of improperly configured 802.1x authentication servers to total number of
	    | 802.1x authentication servers
	* - **Calculation**
	  - :code:`M8 / M11`

.. history
.. authors
.. license
