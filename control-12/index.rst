CIS Control 12: Boundary Defense
=======================================================

Detect/prevent/correct the flow of information transferring across networks of different trust
levels with a focus on security-damaging data.

**Why is this CIS Control Critical?**

Attackers focus on exploiting systems that they can reach across the Internet, including not only
DMZ systems but also workstations and laptop computers that pull content from the Internet
through network boundaries. Threats such as organized crime groups and nation-states use
configuration and architectural weaknesses found on perimeter systems, network devices, and
Internet-accessing client machines to gain initial access into an organization. Then, with a base of
operations on these machines, attackers often pivot to get deeper inside the boundary to steal
or change information or to set up a persistent presence for later attacks against internal hosts.
Additionally, many attacks occur between business partner networks, sometimes referred to as
extranets, as attackers hop from one organization’s network to another, exploiting vulnerable
systems on extranet perimeters.

To control the flow of traffic through network borders and police content by looking for attacks
and evidence of compromised machines, boundary defenses should be multi-layered, relying on
firewalls, proxies, DMZ perimeter networks, and network-based IPS and IDS. It is also critical to
filter both inbound and outbound traffic.

It should be noted that boundary lines between internal and external networks are diminishing
as a result of increased interconnectivity within and between organizations as well as the rapid
rise in deployment of wireless technologies. These blurring lines sometimes allow attackers to
gain access inside networks while bypassing boundary systems. However, even with this blurring
of boundaries, effective security deployments still rely on carefully configured boundary defenses
that separate networks with different threat levels, sets of users, data and levels of control.
And despite the blurring of internal and external networks, effective multi-layered defenses of
perimeter networks help lower the number of successful attacks, allowing security personnel to
focus on attackers who have devised methods to bypass boundary restrictions.

.. toctree::
   :maxdepth: 1
   :name: toc-control-12

   12.1: Maintain an Inventory of Network Boundaries <control-12.1>
   12.2: Scan for Unauthorized Connections Across Trusted Network Boundaries <control-12.2>
   12.3: Deny Communications With Known Malicious IP Addresses <control-12.3>
   12.4: Deny Communication Over Unauthorized Ports <control-12.4>
   12.5: Configure Monitoring Systems to Record Network Packets <control-12.5>
   12.6: Deploy Network-Based IDS Sensors <control-12.6>
   12.7: Deploy Network-Based Intrusion Prevention Systems <control-12.7>
   12.8: Deploy NetFlow Collection on Networking Boundary Devices <control-12.8>
   12.9: Deploy Application Layer Filtering Proxy Server <control-12.9>
   12.10: Decrypt Network Traffic at Proxy <control-12.10>
   12.11: Require All Remote Logins to Use Multi-Factor Authentication <control-12.11>
   12.12: Manage All Devices Remotely Logging Into Internal Network <control-12.12>
   
.. history
.. authors
.. license