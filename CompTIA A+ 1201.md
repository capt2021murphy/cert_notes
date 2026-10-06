### Section 1
###### **Mobile Device Management (MDM) 1.3**

- Manages company owned or personally owned mobile work devices
- BYOD, Bring your own device
	-Personal device used for work
	-Must meet company requirements
- Centralized Management
	-Set policies & controls devices
	-Partition storage for company use or entire device for work use
	-Manage security policies
- COPE, Corporate owned personally enabled
	-Company buys device
	-Used for work & can be allowed for personal use too
	-Company keeps full control of device
		-All policies set by company
- CYOD, Choose your own device
	-Similar to COPE but user picks device
- MDM policy enforcement
	-Pushes configuration to all devices
	-Security policies; multifactor authentication
	-Applications allowed/restricted
	-Network connections & policies 
- Mobile device synchronization
	-Many settings preconfigured
	-How data will be synced
		-WiFi, cell, combo
	-Data types; calendar, contacts, etc.
	-Date & Time sync
- Business Apps
	-Configured on account setting of device
	-Decides what to sync


###### **Mobile Connections 1.3/2.2**

- 3G
	-Released 1998
	-Several megabytes per second (MBPS)
- 4G LTE & LTE-A
	-Long term evolution (LTE), Advanced (A)
	-LTE Released in 2009 & LTE-A in 2012
	-GSM & EDGE used when out of 4G range
		-Also incorporated some GSM technology 
	-150 mbps LTE
	-300 mbps LTE-A
- 5G 
	-Released 2020
	-100 to 900 mpbs 
		-Eventually 10 GBPS (gigabytes per second)
- 802.11
	-WiFi 2.4/5/6/7 GHz (gigahertz)
	-WiFi calling 
- Hotspot
	-Phone acts a router
	-Extends cell network to all devices
	-5G network
	-Must be carrier enabled
- SIM/eSIM
	-Stores phone number, subscriber information, & has some storage 
	-Physical (SIM) or electronic (eSIM)
- Bluetooth
	-2.4GHz with band hopping 
		-Unlicensed Industrial Science Medical (ISM)
	-PIN to pair
	-Enable & discoverable
- GPS (Global Positioning System)
	-DOD created (department of defense)
	-30 satellites in orbit
	-Need 4+ satellites for precise navigation
		-Longitude, latitude, altitude
	-Can also use cell towers & WiFi for precision
- 802.11 extensions
	-802.11ac = WiFi 5
		-5GHz
	-802.11ax = WiFi 6 & 6E
		-Expands into 6GHz
	-802.11be = WiFi 7
		-Multiple GHz bands
	-Channels
		-Groupings of frequencies, IEEE standards
	-Bandwidth/Spectrum
		-Amount of frequency in use
		-20/40/80/160 MHz bands
		-6GHz has more bandwidth than 5GHz which has more than 2.4GHz, etc. 
- RFID (Radio Frequency Identification)
	-1 way communication
	-Used for tracking
	-No active power
		-Scanner with radio frequency (RF) powers tag
	-Some are active powered
- NFC (Near Field Communication)
	-2 way communication
	-Builds of RFID
	-Helps with bluetooth & wireless pairing
	-Used for access & payments

### Section 2
###### **Common Ports | TCP/UDP 2.1**

- FTP 
	-File Transfer Protocol
	-tcp/20, active data mode
	-tcp/21 control command
- SSH 
	-Secure Shell
	-Encrypted communication link
	-tcp/22
- Telnet 
	-tcp/23
	-Unencrypted communication
		-"In the clear"
- SMTP 
	-Simple Mail Transfer Protocol
	-Server to server email transfer
	-Or device to server 
	-tcp/25
- DNS 
	-Domain name system
	-Fully Qualified Domain Name (FQDN) to IP address
	-udp/53
- DHCP 
	-Dynamic Host Configuration Protocol
	-Auto configuration of IP address, subnet mask, default gateway, etc.
	-udp/67 & udp/68 
- HTTP 
	-Hypertext Transfer Protocol
	-Communication in web browser
	-Unencrypted
	-tcp/80
- HTTPS 
	-Hypertext Transfer Protocol Secure
	-Same as HTTP but encrypted traffic
	-tcp/443
- POP3 
	-(Post Office Protocol v.3)
	-1 device received email from mail server
	-tcp/110
- IMAP4
	-Internet Message Access Protocol v.4
	-Synchronizes to multiple devices
	-Management of email inbox from multiple clients (devices)
	-tcp/143
- SMB
	-Server Message Block 
	-Or old name, Common Internet File System (CIFS)
		-No encryption
	-Network communication protocol used for sharing printers, files, serial ports, etc.
	-tcp/445
- NetBIOS over TCP/IP 
	-Old LAN communication standard
	-Allows applications on separate computers to talk to one another
	-udp/137, name service like DNS
	-tcp/139 file transfer session service
- Direct SMB
	-Or SMB direct
	-Allows remote file servers to act like local storage 
	-Operates directly on TCP/IP without extra layers
		-Unlike NetBIOS
	-tcp/445
- LDAPs
	-Lightweight Directory Access Protocol/secure
	-LDAP unencrypted, LDAPs encrypted
	-Database of directory
	-Store & retrieve information on network directory
		-Usernames, passwords, other directory data
	-Common use in Microsoft Azure Directory 
	-LDAP tcp/389, LDAPs tcp/636
- RDP
	-Remote Desktop Protocol
	-Remote access to a computer
	-Primarily Windows but many other clients for other OSes
	-tcp/3389
- NTP
	-Network Time Protocol
	-Keeps all devices on network showing same time
	-udp/123
- Non-ephemeral ports
	-Meaning permanent or not changing ports
	-0 through 1,023
	-Usually used by server or service (application)
- Ephemeral ports
	-Temporary ports to communicate
	-1,024 through 65,535
	-Determined by client in real-time


###### **Network Host Services 2.3**

- Proxy Server
	-Intermediate server that sits between local device & internet
		-Client request > proxy > proxy performs request > proxy provides result to client
	-Used as a security tool, access control, caching, content control 
	-Usually invisible on the network
		-Users can't tell a proxy is querying internet for them
- System Log
	-Protocol that collects log files on 1 central database 
	-Integrated into Security Information & Event Manager (SIEM)
	-A lot of storage space needed
- Authentication Server
	-Authentication, Authorization, & Accounting (AAA) server
	-Login server
		-Username & Password
	-Centralized Management
	-Usually redundant
- Database Server
	-Stores information in tables
	-Tables are linked (relational) to other tables
	-Standard database language is Structured Query Language (SQL)
- NTP server
	-Network Time Protocol
	-Synchronizes time on all devices on the network
	-2 way communication between server & client
- SCADA/ICS
	-Supervisory Control & Data Acquisition System
	-Industrial control system
	-Controls large scale systems, manufacturing, energy, etc.
	-Uses network to control, operates in real time
	-Extremely segmented for security
- Print Server
	-Dedicated device or software application that manages print requests
	-Connects computers to printers over a network


###### **Domain Name Server (DNS) Configuration 2.4**

- DNS
	-Resolves name (domain) to IP address
	-Hierarchical structure
		-Generic Top Level Domains (gTLDs)
			-.com, .org, .net, .edu
		-Country Code Top Level Domains (ccTLDs)
			-.us, .ca, .es
	-Distributed database
		-13 root server clusters, over 1,000 servers
- Dig
	-Query DNS servers
	-Common to Linux & macOS
- NSLookup
	-Windows version of 'Dig'
- Resource Records
	-Database records providing information about domain name
	-Over 30+ records types (IP addresses, CNAME, MX, TXT)
- Address Record (A & AAAA)
	-Defines IP of a host 
	-A records are for IPv4
		-Modify A record to change host name to IP resolution
	-AAAA records are for IPv6
		-Modify records to change host name to IP resolution
- Time To Live (TTL)
	-How long a user will remember IP
	-Once TTL is up it refreshes
		-If you update a website it will show to user within TTL limit
- Canonical Name Records (CNAME)
	-One physical server with multiple services
	-Alias's pointing to same server
		-chat IN CNAME example.com
		-ftp IN CNAME example.com
- Mail Exchanger Record (MX)
	-Determines host for mail server
		-Not IP but a name
	-Used for inbound emails
- Text Records (TXT)
	-Public information, very useful
	-Can be configured to minimize spam email
		-SPF, DKIM, DMARC
	-Commands to see txt records
		-dig professormesser.com txt
		-nslookup -type=txt google.com
- Domain Keys ID Mail Record (DKIM)
	-Email authentication method 
	-Verifies email sent from domain & wasn't modified
		-Helps to reduce spam email
	-Public key in DNS TXT record
	-Private key on email server 
	-Receiver gets private key and matches to public key
		-If they match email verified from sender server 
	-Asymmetric cryptography
		-Process is a bit more complicated than above but that is the gist 
- Sender Policy Framework (SPF)
	-Email authentication protocol
	-List of servers authorized to send email for domain
		-IP addresses & servers
	-Prevents mail spoofing
- Domain based Message Authentication, Reporting, & Conformance (DMARC)
	-Advanced email protocol
		-Builds on SPF & DKIM
	-Emails that fail SPF/DKIM policies DMARC decides what to do with that email 
		-Spam folder, reject email, or accept
		-Can also send a compliance report to email admin


###### **Dynamic Host Configuration Protocol (DHCP) 2.4**

- IPv4 use to be configured manually 
	-IP address, subnet mask, default gateway, DNS, etc.
- Large networks require automatic configurations
- DHCP released in 1997
	-Automatically configures IP settings
- DORA process
	-Discover; client finds DHCP server; broadcast, udp/68 -> server
	-Offer; server sends offer to client; broadcast, udp/67 -> client
	-Request; client locks in offer from server; broadcast udp/68 ->server
	-Acknowledge; server confirms clients acceptance; broadcast, udp/67 -> client
- DHCP Scope 
	-Predefined list of IP addresses & all configuration settings
	-IP address range & excluded addresses 
	-Subnet mask
	-Lease duration
	-DNS, default gateway, VOIP servers, etc.
- DHCP Pool
	-Grouping of IP addresses
		-ex. 192.168.1.1 through 192.168.1.254
	-Can be contiguous or have exclusions/reservations
- DHCP Reservation
	-IP address that is reserved for a device
	-MAC address is what defines the device getting reserved IP 
		-In other words specific MAC gets specific reserved IP address
	-Other names: IP reserve, static DHCP, DHCP reserve


###### **VLANs & VPNs 2.4**

- Local Area Networks (LANs)
	-Group of devices in the same broadcast domain
	-Network connecting devices in a limited geographical area
		-Home, school, office, etc.
- Virtual Local Area Network (VLANs)
	-Logical group of devices in same broadcast domain
	-Can turn 1 switch into multiple virtual broadcast networks (domains)
	-VLANs can communicate with one another via a router or a layer 3 switch
- Virtual Private Network (VPN)
	-Encrypts data traversing a network (private or public)
	-Concentrator
		-Encrypts & Decrypts data
		-Creates & manages VPN tunnels 
		-Can be integrated into firewall
		-Hardware or software deployments
		-Sometimes built into OS
	-Client to Site VPN
		-On demand access from remote device; client software -> VPN concentrator
		-Can be configured as always on
		-Remote user->Internet->Concentrator->Corporate network
	-Site to Site VPN
		-Always or almost always on
		-Remote site to corporate network
		-Remote site->Concentrator->Internet->Concentrator->Corporate network


###### **Network Devices 2.5**

- Routers
	-Routes traffic between/based on IP subnets
	-Data forwarding based on IP address
	-Routers inside of switches, switch is called layer 3 switch
	-Connects different types of network connections & topologies
		-LAN, WAN, Copper, Fiber, etc.
- Switches 
	-Wired connections to endpoints
	-Forwards traffic based on MAC address
	-Network bridging done in hardware; Application Specific Integrated Circuits (ASIC)
		-Bridging is how a switch connects devices or network segments to a single unified LAN
	-Many ports & may have POE
	-Multilayer switch (routing function) layer 3
	-Unmanaged switch
		-Plug & Play
		-No VLANs
		-No Simple Network Management Protocol (SNMP), logs, or management protocols
	-Managed switch
		-VLAN support
			-Interconnect with other switches via 802.1Q
				-802.1Q is VLAN tagging
				-Also called Dot1q
				-4 bytes for protocol tag id & VLAN id
		-Traffic prioritization
			-You can configure priority of network traffic
		-Redundancy
			-Many switches redundant to each other
		-Port Mirroring
			-Also known as Switched Port Analyzer (SPAN)
			-Redirect traffic to a port then connect to that port with monitor device
			-External management using SNMP
				-Can use on a switch to alert of traffic bandwidth
				-Gives alerts and then use port mirroring to investigate traffic
- Access Point
	-Not a router
	-Extends wired networks to be a wireless network
		-Bridged communications
	-Forwarding decisions based on MAC address
- Firewalls
	-Filters traffic (allow/deny) based on port number, traditionally
		-OSI layer 4 (tcp/udp)
	-Modern firewalls based on application traffic
	-Can be used as VPN concentrators
		-Next-generation firewalls
		-Site to site, or, client to site 
	-Can act as a proxy server 
		-Common security technique
	-Most can be layer 3 devices
		-Acts like a router 
- Power Over Ethernet (POE)
	-POE 15.4 watts, 350mA
	-POE+ 25.5 watts, 600mA
	-POE++ 51 watts, 600mA; 71.3 watts, 960mA
		-With 10GBaseT cabling
			-10 gbps copper cabling
	-Not upward compatible; POE+ won't power POE++


###### **IPv4 & IPv6 2.6**

- IPv4
	-OSI layer 3 address
	-Has 32 bits which = 4 bytes = 4 octets
		-1 byte = 8 bits
		-Max byte value = 255
		-Example 198.168.1.1
			-198 (1 byte) =11000000 (8 bits in binary) 
			-4 bytes * 8 bites = 32 bits total
	-IPv4 supports 4.29 billion addresses
		-Over 20 billion devices on internet & growing
		-Network Address Translation (NAT) manages IPv4 demand
- Network Address Translation (NAT)
	-Multiple IPv4 addresses on a local network (LAN) get 1 public IPv4 address for internet                 access
	-Private IPs are not internet routable
		-Private IPs routed internally on LAN
		-NAT for public uses
		-Private LAN IP standards, RFC 1918
			-10.0.0.0 through 10.255.255.255/8 | 24 bits (Host ID)
			-172.16.0.0 through 172.31.255.255/12 | 20 bits  
			-192.168.0.0 through 192.168.255.255/16 | 16 bits
- IPv6 
	-128 bit address
	-Uses hexadecimal 
		-fe80:0000:0000:0000:5d18:0652:cffd:8f52
	-340 undecillion IPs
	-DNS more important since IP is difficult to remember
	-1st 64 bits are network prefix /64; your network
	-Last 64 bits are host network address
	-Less subnetting since networks are much larger 


###### **Assigning IP Addresses 2.6**

- Automatic Private IP Addressing (APIPA)
	-169.254.0.0 through 169.254.255.255
		-Functional 169.254.1.0 through 169.254.254.255
		-1st & last 256 IPs reserved 
	-When DHCP server isn't working APIPA address is given
	-Link local, communication is limited to local IP subnet 
- Loopback 127.0.0.1
	-Used to test device IP network stack
	-Loopback address
	-Local host; computer communication to talk to itself
- Every device has unique IPv4 address
	-Subnet mask to determine broadcast domain (subnet)
	-Subnet mask usually not transmitted on network
- Default Gateway
	-Router that allows communication outside of local subnet/s
	-Must be an IP on local subnet 
	-Serves as entry point/exit door for your local network
- Static IP 
	-IP address that doesn't change 
		-Usually manually configured
	-Not best practice, use DHCP reservation instead


###### **Internet Connection Types 2.7**

- Satellite
	- 100 Mbps down, 5 Mbps up
	- Mainly for remote sites or difficult to network sites
	- High latency — common 250 ms up, 250 ms down (1/2 sec total)
    - Starlink: 25–60 ms
	- Line of sight, so if it rains/cloudy get “rain fade”

- Fiber
	- Freq of light, high speed comms
	- Higher install costs v. copper
	    - Equipment & repairs cost more
	    - Fiber itself is expensive too
	- Can transmit much longer distances than copper
	- Common in WAN & MAN cores
	    - SONET ring, multiplexing

- Cable (Coax)
	- Multiple traffic types (Data, TV, etc.), broadband
	- Transmission across multiple frequencies
	- DOCSIS standard (Data Over Cable Service Interface Spec)
	- Asymmetrical 50–1,000 Mbps down

- DSL
	- Asymmetric Digital Subscriber Line, use telephone line
	- 200 Mbps down & 20 Mbps up, 10k foot distance limit from central office

**Int connection cont. 2.7**

- Phone (cell networks)
	- 1-1 called tethering; phone acts as wireless router
	- Mobile hotspot
	    - provides internet to multiple devices
	    - phone acts as wireless router

- WISP
	- Wireless internet service provider
	- Remote or rural sites; antenna to connect
	- Diff deployment tech
	    - Meshed 802.11
	    - 5G home internet
	    - Proprietary wireless
- 10 - 1,000 mbps down

**Network Types**

- LAN (Local Area Network)
	- Network or group of networks close to location
	    - 1 + building/s

- WAN (Wide Area Network)
	- Across cities, states, or worldwide ; slower than LANs
	- General connections LANs across distances
	- Diff WAN technologies
	    - Point to point serial, multiprotocol label switching (MPLS)
	    - Terrestrial & non

- PAN (Personal Area Networks)
	- Own private network
	- Bluetooth, IR, NFC
	- Car, phone, health devices

- MAN (Metro Area Network)
	- Network in a city
	    - WAN > MAN > LAN
	- Historically proprietary
	    - Now Metro-Ethernet
	    - Fiber as well
	- Gov owned, right of way

- SAN (Storage area Network)
	- Repository of storage
	- Very high speed to tx data in & out, feels like local storage
	- Block level access ; change small amount of data in large file
	- Requires a lot of bandwidth
	    - May use isolated network due to this

- WLAN 
	- wireless LAN ; 802.11 tech

###### **Network Tools 2.8**

- Loopback plug
	- For testing physical ports
	- Serial (RS-232) 9 or 25 pin, Ethernet, Fiber, T1
	- Not crossover cables, loops back into itself
	- Plug into port on device then put device into diag mode
	    - Send info out port in diag mode
	    - Compare sent info to received info
	- RJ-45 connector pinout 
		1 <========> 3
		2 <========> 6
		4 <========> 7
		5 <========> 8

- Taps & port mirrors
	- Intercept network traffic  
	    - Send copy to packet capture device
	- Physical taps  
	    - Active or passive ; inline of link path
	- Port mirror  
	    - Redirect port traffic, SPAN (Switched Port ANalyzer)  
	    - Software tap ; limited functionality but works

### Section 3
###### **Display Types 3.1**

 - LCD (Liquid crystal display)
	- Light source shines through filters & liquid crystals
	- TN LCD (Twisted Nematic)
		- Original LCD Tech
		- Fat response time (gaming), 
		- Poor viewing angles off center (color shifts)
	- IPS LCD (In Plane Switching)  
	    - Excellent color representation but more expensive
	- VA LCD (Vertical Alignment)  
	    - In-between TN & IPS  
	    - Good colors, but slower than TN

- OLED (Organic Light Emitting Diode)
	- Organic compound emits light when powered
	- No backlight, making it thinner/lighter
	- Very good color representation, more expensive than LCD

- Mini LED
	- Smaller LEDs w/same backlight tech as LED LCD
	- Individual LED control, color & intensity can vary
	- Better black representation as well as color

| Pros                | Cons                         |
| ------------------- | ---------------------------- |
| -Lightweight        | -True black are hard to get  |
| -Low power          | -Requires backlight & can be |
| -Fairly inexpensive | -Hard to replace             |

- Touchscreen
	- Digitizer input = touch & output = coordinates
	- No keyboard required but still available
	- Can use stylus (pen like) for input; mainly for graphics

- Inverter
	- LCD using fluorescent need ac
	- Inverter turn DC to AC

###### **Display Attributes 3.1**

- Pixel Density
	- Measured by pixel per inch/centimeter (PPI/PPCM)
	- Higher pixel density = better image
	- How will image be used; TV, print?  
	    - Printers (Dots per inch/DPI)
	- Pixel density comparison  
	    - number or pixels / # or inches  
	    * 27 inch TV (diag) 4k  
	    - 3,840 horizontal pixels /24 inches wide  
	    - = 160 pixels per inch

- Refresh rate
	- Many images viewed consecutively
	- Measured in Hertz (Hz)  
	    - Number of cycles per second, if = to FPS then called V-Sync  
	    - Frames per second

- Frame rates
	- Movies : 24 FPS (expected)
	- TV : 30 FPS
	- Games/sports : 60 + FPS

- Max Refresh
	- Determined by video card/adapter & connection
	- HDMI 2.1 max support 4k @ 144Hz
	- DisplayPort 2.1 max support dual 4k @ 144Hz

- Screen resolution
	- Number of pixels = width * height
    - More pixels = more detailed image
	- "Standards" resolution vary & 16:9 aspect ratio is common

- Color gamut
	- Range of available colors on display/output device
	- Less capable than human eye
	- Measured w/ CIE 1931 color space  
	    - Standards within CIE 1931  
		    * sRGB  
		    * Adobe RGB  
		    * International Telecomms Union (ITU) for HDTV
- Color Coverage
	- Display compared to color gamut standard
		- Color Gamut = 100% sRGB (example)
	- Gamut compatibility varies
		- Higher percentage = better colors, cost more
	- OLED 
		- Best color gamut support > IPS LCD

###### **Network Cables   3.2**

- Twisted pair copper
	- 2 wires w/ equal & opp signals  
	    - Tx+, Tx- / Rx+, Rx-
	- Twist is to move away from interference/noise
	- Pairs have diff twist rate
	    - Rx end compares signal to noise

- Cable categories (IEEE 802.3)
	- Min capabilities for cables (speeds)
	- Encoding determines speed (data transfer rate)
	- IEEE 802.3 ethernet cabling standards  
	    - Cat 5e, Cat 6A, etc.  
	    - ex. 1 gbps = 1000 BASE-T MIN Cat 5 cable

- Coax
	- 2 or more forms sharing common axis
	- RG-6 used in TV, digital cable, & high speed internet

- Unshielded & shielded twisted pair
	- UTP, no added shielding
	- STP, shield over individual pairs &/or overall cable  
	    - Requires cable to be grounded
	- Abbreviations  
	    - U, unshielded 
	    - F, foil shielding  
	    - S, Braided shielding

- Outside cable abbreviations
	- Overall cable / individual pairs (twisted pair) TP  
	    - S/FTP = Shielded (braided) overall / Foil around pairs  
	    - F/UTP = Overall foil / No shielding around pairs

- Direct Burial STP (Shielded twisted pair)
	- Sometimes overhead, usually in ground
	- Gel inside, waterproof, conduit optional
	- Provides ground, strength, & repels interference
	- Drain wire (ground)

- Plenum / Non-Plenum
	- Plenum airspace = Return air stays in drop ceiling
	- Non-plenum airspace = Forced return outside of drop ceiling
	- Plenum cabling must be used for plenum airspace  
	    - Fire rated cable jacket  
		    * Fluorinated Ethylene Polymer (FEP)  or Low smoke polyvinyl chloride (PVC)

###### **568A & 568B Standards   3.2**

- Standards
	- International ISO/IEC 11801 cabling  
	    - Defines classes of networking standard
	- TIA (Telecomms Industry Association)  
	    - ANSI/TIA-568 : Commercial Building & Telecomms cabling
	- Above referenced for pin & pair assignments of 8 conductor/100 ohm (Ω) balanced twisted pair cabling  
	    - T568A & T568B

-  Pinout: T568B
	  1 = White/Orange
	  2 = Orange
	  3 = White/Green
	  4 = Blue
	  5 = White/Blue
	  6 = Green
	  7 = White Brown
	  8 = Brown
	- for T568A swap: 1 → 3 , (orange for green) 2 → 6

###### **Fiber  3.2**

- Transmission by light
	- Uses visible spectrum
	- No RF (Radio freq), difficult to monitor or tap
	- Signal degrades slow, transmission of longer distances
	- Immune to radio interference (no rf)

- Multi-mode
	- Usually short distances, up to 2km, (inside buildings)
	- Short range comms
	- Due to short distance use inexpensive light source; LED
	- Different paths light can take as moving through fiber

- Single mode
	- Designed for long range comms, up to 100km w/o regen
	- Common to use lasers, to make sure it can travel  
	    - Expensive light sources
	- Moves in a single path, narrow core

###### **Fiber connectors      3.2**

- ST (Straight tip) interface
	- Bayonet connector (like a BNC connector)

- SC (Subscriber connector)
	- Square or standard connector, commonly known as
	- Push to lock in, very popular
	- Individual fibers or combine for a pair (Tx/Rx)

- LC (Lucent connector)
	- Locks w/ clip, local or little connector          
	- Individual or pair

###### **Copper Connectors    3.2**

- RJ-11
	- 6 position, 2 conductor  
	    - Some have 4 conductors
	- Telephone or DSL

- RJ-45
	- 8 position, 8 conductor  
	    - Modular
	- Known as ethernet but has more uses

- F connector
	- Coax, threaded connection
	- Cable tv, modem, DOCSIS

- Punchdown blocks
	- Wire to wire, NO intermediate interface
	- 110 block, etc.  
	    - Wires "punched" with a punch down tool

- Molex (AMP Mate-N-lok)
	- 4 pin power
	- +12v, +5v
	- For fans, storage, peripheral devices
	- Older version

###### **Cables      3.2**

- Peripheral (accessory)
	- USB 1.1, 2.0, 3.0, 3.1, 3.2

- USB 1.1/2.0 connectors
	- A plug
	- B "     "
	- Mini B "     "
	- Micro B "    "

- USB 3.0 connectors
	- Blue color  
	- A, B, & micro B (diff than 1.1/2.0)

- USB-C
	- Replaces all other usb connectors

- Serial Cables
	- DB-9/25 (2 diff cables)
	- DB9 is technically DE9
	- RS 232 standard (recommended standard)
	- Used before usb; 1969, for modem comms, printers, mouse, etc.
	- Now used as a config port
	- Console connection for config using CLI
	- RJ45 or usb to serial

- Thunderbolt
	- High speed serial, data & power on same cable
	- Mini display port standard for thunderbolt 1 & 2
	- Thunderbolt 3 & 4 use USB-C  
	    - Daisy chain up to 6 devices

- Video
	- HDMI, DisplayPort, DVI-D/I/A, VGA

- Display port
	- Digital info sent in packetized form
	- Passive adapter  
	    - DP → HDMI, DP → DVI

- DVI (single & dual link)
	- -A, Analog, backward compatible w/ VGA
	- -D, Digital
	- -I, Integrated, Both digital & analog
	- No audio support

- VGA (Video graphics array)
	- DB-15 / DE-15
	- Video only
	- Analog, blue color connector

###### **Storage cables     3.2**

- SATA (serial AT attachment)
	- SATA Revision 1.0, 1.5 Gbps / 1 meter
	-      "        "        2.0, 3 Gbps / 1 meter
	-      "        "        3.0, 6 Gbps / 1 meter
	-      "        "        3.2, 16 Gbps / 1 meter
	- eSATA, similar to internal SATA / 2 meters

- Cable (sata)
	- Power 15 pin, Data 7 pin
	- 1-1 relationship, no daisy chaining
	- eSATA cable is different than SATA cable

###### **Adapters & Converters   3.2**

- Usually temp use, sometimes permanent

- DVI-D → HDMI
	- No signal loss or conversion

- DVI-A → VGA
	- Only 640×480 officially supported
	- Analog, no conversion

- USB → Ethernet
	- Requires driver

- USB C -> USB A
	- For devices without a USB A connection

- USB Port Replicators
	- Hub for many connections

###### **Memory   3.3**

- RAM (Random access memory)
	- Not the only kind
	- NOT hard drive, SSD, or any storage
	- Temporary high speed storage for apps & calculations

- DIMM
	- Dual inline memory module has 2 sets of contact, 1 on each side
	- 64 bit data width

- SO-DIMM (small outline DIMM)
	- 1/2 size of normal DIMM
	- Used in laptops & mobile devices
	- Tend to be installed horizontal, not vertical

- Dynamic random access memory
	- Installed on DIMM card, memory chip
	- Dynamic  
	    - NO refreshing for data to disappear  
	    - Needs constant refreshing
	- Random access
	    - Any data can be accessed on any chip at any time; directly & instantly
	    - Not like magnetic tape

- SDRAM (synchronous dynamic RAM)
	- Synced to common system clock
	- Queue one process while waiting for another
	- Classic DRAM didn't sync to clock

- SDR v. DDR (Single data rate v. Dual data rate)
	- SDR 1 clock cycle = 1 data transfer
	- DDR 1 clock cycle = 2 data transfer  
	    - Double SDR

- DDR3 SDRAM (Dual Data Rate 3 Syn dynamic random access mem)
	- 2x data rate of DDR2
	- No backward compatibility

- DDR4
	- Faster freq's = speed over DDR3 but No backward comp.

- DDR5
	- Faster data transfer rate between memory module & motherboard
	- No backward comp., physical chip key moved

- Keys from different DDR versions always change position

###### **Memory Tech  3.3**

- Memory that checks itself
	- Predominately used in servers
	- Parity memory  
	    - Adds additional parity bit w/ each byte stored  
	    - Won't always detect err & can't correct an err.  
	    - Can tell you memory err & where it occurred
	- Error Correction Code (ECC)  
	    - Detects err & corrects on the fly  
	    - Looks the same as parity & standard memory

- Parity
	- Even parity, count up bits & if even 0, if odd 1
	- Recognize errors occurred by saving an extra bit

|Bit: 1|2|3|4|5|6|7|8|Parity (9)|
|---|---|---|---|---|---|---|---|---|
|0|1|0|1|0|0|1|1|0|
|1|0|0|0|1|1|0|0|1|

- Memory stores byte + parity bit, when retrieved byte is evaluated for parity bit & compared to saved parity bit. If identical NO issue if diff error present.

- CPU to RAM throughput
	- Memory bandwidth  
	    - Max throughput between CPU & RAM
	- Measured in Megatransfers / s (MT/s)  
		- Million transfers 
	    - ex. 32 GB DDR5, 5600 MT/s
	- Memory bandwidth on motherboard determines max

- Multi-channel Memory
	- Pathway might reach max bandwidth but CPU has IDLE time 
	- To increase throughput add channel between CPU & RAM
		- 2x throughput; 2 memories
		- 2, 3, 4 channel memories possible
			- Exact RAM matches are best
			- RAM color coded on motherboard

###### **Storage Devices     3.4**

- RAM is volatile, power off & data disappears
	- Storage device needed

- HDD (Hard Disk Drive)
	- Non-volatile magnetic storage, rapidly rotating platters (vinyl)
	- Random access  
	    - Access data from any part of disk at any time
	- Mechanical components limit speed & can break  
	    - Spinning platters & actuator arm

- Drive size varies
	- 3.5 in, 2.5 in, 22mm  
    - Mainly for laptops & mobile devices

- SSD (Solid State Drive)
	- Non-volatile & no moving parts
	- Many times faster than HDD due to no spinning drives

- PCIe storage interface
	- Faster than SATA, before M.2
	- High speed throughput for SSD comms
	- Connects to motherboard  
	    - Provides power & high throughput
	- PCIe data transfer 64 Gbps per lane

- AHCI (Advanced Host Controller Interface)
	- Moves drive data to RAM, used for SATA

- NVMe (Non-Volatile Memory Express)
	- Designed for SSD speeds, drive data to RAM
	- Low latency, higher throughputs, uses PCIe bus
	- M.2 interface into PCIe

- Serial attached SCSI
	- For improved throughput using HDD, upgrade from SATA
	- Useful for large storage arrays

- mSATA (mini SATA)
	- Smaller form factor of SATA
	- Higher speed bus, great for laptops & mobile devices

- M.2
	- Smaller form factor
	- No SATA data or power cables
	- Direct bus connection, PCIe connection
	- Different types of connectors for connectivity type  
	    - B, M, or B/M keys  
	    - Some M.2 support both keys
	- M.2 might use NVMe or AHCI  
	    - Check documentation for keys & protocols

- Flash drives
	- EEPROM (Electrically erasable programmable read-only memory)
	- Non-volatile & doesn't require power to retain data
	- Limited # of writes, can still read
	- Not archival or backup use

- Optical drives (CD's, DVD's, Blu-ray)
	- Laser beam reads small bumps, micro binary storage
	- Slow but archival/backup
	- Can hold a lot of info & take up little space


###### **Redundant Array of Independent Disks  (RAID)   3.4**  

- Raid 0 / Striping
- Raid 1 / Mirroring
- Raid 5 / Striping w/ 1 parity drive
- Raid 6 / Striping w/ 2 parity drives
- Nested RAID - Raid 1+0 (10) - A stripe of mirrors


- RAID 0 - Striping
	- File/s block are split between 2+ physical drives
	- Known for speed
	- No redundancy (0)
                 Stripe
        Block 1A                        " 2A
          "   3A                        " 4A
          "   5A                        " 6A
          "   7A                        " 8A
       ==========         ==========
         Disk 0                        Disk 1 

- RAID 1 - Mirroring
	- File blocks are duplicated on 2+ drives
	- High Storage req., double space requirements
	- High redundancy
	- 2 drive MIN
                 Mirror
        Block 1                         " 1
          "   2                         " 2
          "   3                         " 3
          "   4                         " 4
       ==========        ==========
        Disk 0                       Disk 1 

- RAID 5 - Striping with parity          
	- 3 drive MIN
	- Parity used to ID errors or correct them
	- Parity provides redundancy with striping 
	- Files aren't duplicated ; efficient
	- High redundancy, takes existing data + parity to recreate info
	- Parity calculation uses high CPU %, affects performance
	            <-Stripe->       <-Stripe->        <-Stripe->
          Disk 0                    D1                   D2                       D3
     Block   1A                       2A                    3A                   Parity A
            1B                       2B                 Parity B                  3B
            1C                    Parity C                 2C                     3C
         Parity D                    1D                    2D                     3D

- RAID 6 - Striping w/ 2x parity
	- Adds another parity, at least 4 drives required
	- Can lose up to 2 drives & still run all data
	- Not extra capacity
        <-Stripe->   <-Stripe->  <-Stripe->         <-Stripe-> 
Block  1A                2A                 3A               Parity A             Parity AA
       1B                2B              Parity B          Parity BB           3B
       1C             Parity C        Parity CC         2C                    3C
    Parity D       Parity DD          1D               2D                   3D
    =====        ====           ====           ====               ====
     Disk 0           D 1                D 2                D 3                  D 4   

- RAID is data redundancy, Not a backup!

- RAID 1+0 (10)
         Stripe                             Stripe               
    Mirror                          Mirror                    Mirror
Blk 1         Blk 1             Blk 2         Blk 2      Blk 3         Blk 3
--1--         --1--             --2--         --2--     --3--         --3--
--4--         --4--             --5--         --5--     --6--         --6--
--7--         --7--             --8--         --8--     --9--         --9--
--10-         --10-             --11-       --11-     --12-        --12-
=====    =====         =====   ===== =====    =====
Disk 0        D1                D2            D3         D4             D5


###### **Motherboards   3.5**

- Form factors
	- Case size, layout, power standardized connections, airflow
	- Over 40+ motherboard types!
	- ATX, microATX, & ITX (from largest → smallest)

- ATX (Advanced Technology Extended)
	- Intel standardized in 1995
	- Power 20 pin (classic), 24 pin ~~pin~~ + 4/8 pin connectors _(Scribble out in original)_

- microATX (μATX, M-ATX)
	- Similar layout but smaller than ATX ; exact same mounting points & power
	- Backward compatible w/ ATX

- ITX (also has mini-ITX version)
	- Low power, small form factor developed in 2001 by VIA Tech
	- miniITX mounting screw compatible w/ ATX
	- Single purpose computing (IPTV, etc)

**Motherboard Expansion Slots   3.5**

- Bus
	- Communication path connecting diff components of motherboard, can increase capabilities of system

- PCI bus (Peripheral Component Interconnect)
	- Created in 1994
	- 32 & 64-bit bus width over parallel comm
	- Different keys to tell between 32/64 bit cards

- PCIe Bus (PCI express)
	- Replaces PCI
	- Serial comms, Not parallel
	- x1, 2, 4, 8, 16, 32 full duplex lanes (by 1, or by 32)
	- Ex. of a PCIe x2 lane
	- Look similar to PCI but keys differ & added hook.
        PCIe        ========>
      Device A      <========       PCIe Device B
                ========>
                <========

**Motherboard Connections  3.5**

- 24 pin power (new), can connect to 20pin motherboard
	- 20pin original but 24 added for PCIe power
	- Provides +3.3v, +/- 5v, +/- 12v

- PCIe 6 & 8 pin power
	- Added power for PCIe adapters (graphics card)
	- 6 pin = 75 watts, 8-pin = 150 watts
	- 8 pin or 6 + 2 pin connector to use either way

- SATA (storage)
	- L shaped integrated connection

- eSATA
	- Some motherboards have an adapter card

- Headers (pins sticking up from motherboard)
	- Integrated to motherboard
	- Many uses ; power, lights, buttons, peripheral connections, etc.
	- Sometimes associated w/ single pair of wires, are marked

- M.2
	- Storage, modular connection ; small


**Motherboard Compatibility  3.5**

- 2 CPU manufacturers
	- Intel & AMD  
	    - Small differences but compatible
	- AMD tends to be cheaper
	- Motherboard Sockets designed for a specific CPU

- Server motherboards (19 inch rack, usually ATX form)
	- Multi socket ; multiple CPU support
	- Support 4+ memory (RAM) modules
	- Support multiple expansion slots

###### **BIOS    3.5**

- Basic Input/Output System (BIOS)
	- Software used to start your computer
	- Firmware, before OS starts
	- Also called sys BIOS, Flash BIOS, or Rom BIOS (old)
	- Initializes CPU & Memory
	- POST (Power on self test)  
	    - Checks for CPU, RAM, keyboard, & mouse  
	    - Any issues w/ post & err message  
	    - Once done loads OS or boot loader to select OS
	- Usually stored in Flash memory (contemporary)

- Legacy BIOS
	- Original BIOS (25+ years)
	- Older OS used this BIOS  
	    - OS communicated to hardware through BIOS, instead of directly
	- Limited hardware support, no modern drivers

- UEFI BIOS (Unified Extensible Firmware Interface)
	- Based on Intel's EFI
	- Standard on all modern systems

**BIOS Settings    3.5**

- BIOS launch keys
	- Del, F1, F2, Ctrl-S, Ctrl-Alt-S, enter, etc
	- Manufacturer specific
	- VM machines sometime allow this too  
	    - Hyper-V, vmware
	- Simulators available for VM w/o BIOS option

- WIN 10/11
	- NO BIOS key shortcut
	- Doesn't actually completely shut down  
	    - Called fast startup  
	    - Partial shutdown
	- To completely shutdown to reach BIOS  
	    - Hold Shift when restarting  
	    - Settings / update & security / Recovery / Advanced startup / restart now  
	    - Temp changes in sys config (msconfig)  
	    - Or interrupt boot process 3 times

- Changes to BIOS
	- Always have backup of BIOS ; pics, notes
	- Don't change unless you know

**BIOS Settings   3.5**

- Boot options
	- Disable hardware
	- Boot Options (order) on startup

- USB permissions
	- Can restrict usb usage
	- To prevent security issues

- Fans (& temp monitoring)
	- Motherboard temp sensors & fan controllers  
	    - CPU & case fans
	- Can change settings in bios if above is the case

- Secure boot
	- Prevent malware from taking over
	- Digitally signs known good software, cryptographically  
	    - Software (OS, drivers) wont run w/o proper signature
	- Not available for legacy OS due to lack of digital signature
	- UEFI BIOS protections  
	    - BIOS includes manufacturers public key  
	    - Digital sig. checked during BIOS update  
	    - Unauthorized writes wont go through to BIOS flash

- Secure boot verifies bootloader
	- Check OS's bootloader digital sig.
	- Bootloader must have digital signature of a trusted source (trust certificate)
	- Or manual trusted digital sig.
	- Otherwise wont boot OS

- Boot password management
	- Boot p/w or user p/w  
	    - System wont boot OS w/o password
	- Supervisor/BIOS p/w  
	    - Restrict BIOS startup / changes w/o password
	- Remember p/w or BIOS reset is a must!  
	    - Manufacturer specific

- Reset BIOS
	- (Old) CMOS (Complementary metal-oxide semiconductor) BIOS memory  
	    - Cleared w/ removal of battery
	- (Now) Flash memory stores BIOS  
	    - Reset w/ jumper of 2 pins on motherboard

- Virtualization support
	- Running multiple OS's within 1 physical comp.
	- Built into CPU ; check with manufacturer

###### **TPM & HSM  3.5**

- Trusted Platform Module (TPM)
	- Hardware that helps single device encryption functions
	- Specification for cryptographic functions
	- Cryptographic processor  
	    - Random number generator, key generator
	- Persistent memory ; unique keys burned onto during production
	- Versatile memory ; store keys & hardware config info
	- Password protected (No dictionary attacks)
	- Has a unique secret key  
	    - Only associated w/ your computer  
	    - If drive is encrypted you can't move drive to another computer  
	    - Key not avail outside of comp
	- Root of trust  
	    - Due to secret key, TPM, is a physical reference point for comp.  
	    - Has comp been modified or tampered w/
	- Can't use key of TPM on another comp.  
	    - Cryptography for 1 device
	- TCG — Trusted computing group ; org that manages standards for TPM
	- Single device management for security

- Hardware secure module (HSM)
	- Large scale security solution  
	    - Manages & maintains keys of all systems
	- Key backup (centralized)  
	    - Secure storage for servers  
	    - Personal / lightweight HSM  
		    * Crypto cold storage wallets
	- In datacenter a HSM is configured w/ cryptographic hardware for a high end server  
	    - Cryptographic accelerator  
		    * Webserver can use encrypt/decrypt process on a HSM instead of doing it.  
		    * Only HSM knows key

|TPM|v.|HSM|
|---|---|---|
|— Single sys||— Many sys|
|— Secure data on local dev||— Secure data across many devices|
|— Motherboard integrated or  <br>    add on module||— Often deployed as high end server  <br>    or appliance in data center|
|— Phone booting, screen lock,  <br>    encrypt storage||— Protect Certificate authority on  <br>    a secure central device|

###### **CPU Features   3.5**

- OS tech
	- 32 v. 64 bit, CPU
	- 32 bit processors store 2^32 or about 4.3 billion data values or 4GB (x86)
	- 64 bit processors store 2^64 data values or 17 billion GB (x64)
	- Hardware drivers are specific to 32 or 64 bit OS version
	- 64 bit OS backward compatible w/ 32 bit apps  
	    - 32 bit OS Not able to run 64 bit apps  
	    - 64 bit apps stored in :\Program Files  
	    - 32 bit apps stored in :\Program Files (x86)

- ARM (Advanced RISC Machine)
	- CPU architecture developed by Arm Ltd.
    - Faster & efficient processing ; less power & heat
	- Mainly used in IoT & mobile devices, starting to be used for desktops & laptops

- Processor cores
	- Within CPU there are Cores, each one is actually a CPU. so a CPU is really a package (CPU package)  
    - Dual-core / Quad-core / Multi-core, etc.
    - Multiple cores can perform multiple instructions at the same time

| Core 1 = CPU      | | Core 2 = CPU      |
|    L1 cache           | |    L1 cache           |
|    L2 cache           | |    L2 cache           | 
|-----------------------------------------|
|            Shared L3 cache                      | ----| Memory Bus |------|  RAM  |
|                                                            |

###### **Expansion Cards    3.5**

- Adapters that provide additional functionality to motherboard
	- Can get generic motherboard & add expansion cards
	- Install card, driver & usable

- Video card (GPU, discrete)
	- Many CPU's have integrated GPU
	- Discrete graphics is not part of CPU  
	    - Separate interface, high performance

- Capture card
	- To record video (live streaming, external cameras)  
	    - PCIe for high video bandwidths
    

- Network Interface Card (NIC) ; multiport ethernet
	- Added connections for : servers, routers, sec cams, etc

- Always check documentation
	- Motherboard type & # of slots
	- Order of install (hardware, driver) or inverse
	- Check device driver to confirm install


###### **Cooling   3.5**

- Airflow is important
	- Motherboard layout matters  
    - Component location matters too

- Adapter card fans
	- Used on larger adapter cards (graphics)

- Fan specs
	- 80mm, 120mm, 200mm, etc sizes
	- Variable speeds ; noise varies on fan manufacturer
	- Fanless / passive cooling  
	    - Silent, no fan  
	    - Specialized function (video server, TV STB, etc)  
	    - Use heat sinks to dissipate heat

- Heat sink
	- Dissipate heat through thermal conduction  
	    - Copper / alum alloy
	- Fins / grid increase surface area, tx to cooler air
	- Thermal paste for contact between component & heat sink

- Thermal paste
	- Thermal grease, conductive grease
	- Place between component & heat sink (pea size)
	- Improves conductivity & moves heat away from component

- Thermal pad
	- Conduct heat w/o mess ; cut to size & install
	- Won't leak or damage components
	- Not as effective as thermal paste, still very good
	- Not reusable

- Liquid cooling
	- Overclocking, gaming, high end system
	- Similar to car cooling system

###### **Computing Power  3.6**

- Power supply      (120vac or 230vac)
	- DC power to comp (AC in) ; manual or auto switching
	- 120vac to 3.3v, 5v, & 12v DC

- Wattage
	- Volt * amps = Watts
	- Ohm's law = V = I * R, I (A) = V / R, R = V / I (A)

- P.S output
	- +12v (dc) for PCIe, hard drive motors, cooling fan, most components
	- +5v for some motherboard components, + more
	- +3.3v for M.2, RAM, motherboard logic circuits
	- +5vsb, standby to motherboard to wake comp from sleep

- P.S output
	- -12v for Integrated LAN, old serial ports, old PCI
	- -5v for old ISA cards Not used in motherboards now

- 24 pin motherboard connector
	- Main power provides +3.3v, +/- 5v, & +/- 12v
	- 20+4 for new & old connections
	- Keyed connector

- Redundant power
	- Mainly used on servers
	- Each power supply can handle 100% of load, normally run @ 50% of load
	- Hot-swappable, replace w/o powering down

- Power Supply connectors
	- Fixed or modular connectors  
	    - Hybrid of both too.

- P.S wattage
	- Size of p.s tends to be standard regardless of watts
	- To calculate wattage add watts for all components  
	    - CPU, storage, video, etc.
	- Make sure P.S has 50% of capacity, for room to grow & operating efficiently, ex. total needed watts 500w get 1000w
	- Energy efficiency
		- 80-96% ratings
		- Ranges from: Standard 80 plus, bronze, silver, gold, platinum, titanium

###### **Multifunction Device   3.7**

- M.F.D
	- Printer, scanner, fax, Network connection, phone line, web print
	- Can be small or large
	- Printer drivers on all computers using MFD to print  
	    - 32 or 64 bit driver, depends on OS/device

- Page description language used by MFD
	- PCL ; printer command language  
	    - Created by Hewlett-Packard  
	    - Common across industry
	- PostScript  
	    - Created by Adobe sys  
	    - Popular w/ high end printers
	- Printer reads language & renders then prints page.
	- Driver must match printer language _(Scribbled out in original)_  
	    - PCL printer, pcl driver, etc.

- Firmware
	- NO OS but firmware
	- Starts sys, connect to network, interpret data, print process  
	    - Update firmware to fix bugs, avoid incompatibilities  
		    * Every device has diff process

- Direct connection
	- USB type B (printer), A (comp), or C
	- RJ45, ethernet
	- Or multiple options

- Wireless connection
	- Bluetooth, limited range
	- 802.11 (infrastructure mode)  
	    - MFD connects to AP & many devices can connect, as long as they're on same network
	- 802.11 Adhoc  
	    - Point to point, between 2 devices no access point connection.

- Printer share / Print server
	- Printer connected to computer, comp shares printer  
	    - Comp needs to be running to share connection  
	    - Share tab in printer properties (in connected comp)
	- Print server  
	    - Internal to printer or external  
	    - Jobs sent directly to printer  
	    - Server manages print jobs  
	    - Web-based front end management or client software

- Duplex printing
	- Print on front/back of same page auto
	- Not all printers can do this

- Orientation
	- Portrait █ or landscape ▄
	- Page doesn't turn/move

- Multiple trays
	- Letterhead, plain, etc. in diff tray
	- During print select tray.
	- Can configure auto tray to pick

- Quality
	- Resolution, color/greyscale, color saving
	- Lower saves toner

- User authentication
	- Either built into print sharing or setup on print server
	- Set rights & permissions

- Badging
	- Authenticate to use printer
	- Send job then use badge to print when @ printer

- Audit log
	- Monitors who is printing & how much
	- May be built into printer or print server
	- Cost management / Sec monitoring
	- Windows event viewer / sys events

- Secured prints
	- Define password to use printer
	- Send job then input p/w @ printer

- Scanner
	- Input device
	- Sometimes has ADF (auto document feeder)  
	    - Many pages scanned auto
	- Scan to email or shared drive/folder  
	    -  Scan to SMB for folders/drive
	- Scan to cloud to

###### **Laser Printer 3.8**

- High Quality, fast printing
- Many moving parts, needs on-printer memory & processing
	- Messy due to toner

- Operation
 ① corona wire charges drum (-)
        O———— laser neutralizes (-) charge
        |———— (-) charged toner sticks to laser mark
    8 — — — — — — — paper feed through
    L fuser uses heat to bind toner to paper

- Toner replacement
	- Message or paper w/no/missing toner
	- Sometimes toner/opc drum changed as a unit  
	    - Organic photoconductor drum  
	    - Photo (light) sensitive drum, keep in bag
	- Power down printer, don't touch fuser

- Maintenance
	- Kits sold w/all needed parts
	- Page counter to know when to do maintenance (check manufacturer)
	- Power down

- Might have to calibrate after toner change  
    — auto or manual check documentation

- Cleaning
	- Dust, wipe away _(Scribbled out in original)_
	- Water (cold), & isopropyl (IPA) alcohol
	- Outside vapor cloth

###### **Inkjet 3.8**

- Inexpensive, quiet, high-resolution  
- Costly ink (& proprietary), ink fades, clogs easy

- Ink cartridge
	- Cyan, Magenta, Yellow, Black (C, M, Y, K)
	- Drops of ink onto page
	- Print head sometimes on cartridge

- Feed rollers
	- Pull paper into printer & through printer, clean if stuck

- Duplex printing
	- Supported by some printers, some need extra parts

**Inkjet maintenance 3.8**

- Cleaning print heads
	- Streaks of color, clean print heads
	- Clogged heads is a big issue  
	    - Many printers clean everyday car
	- Cleaning process can be manually started

- Replacing cartridges
	- C, M, Y might be separate or combined
	- Plastic, "recycle"
	- Might need calibration, usually auto can nudge settings

- Paper Jam
	- Remove paper tray
	- Open printer cover & remove paper w/o ripping paper

###### **Thermal Printer 3.8**

- Receipts! (example)
- White paper (how it works), w/chemicals
	- Turns black when heated; why if left in heat (car)  turns all black
	- Very quiet
	- Heat/light sensitive (No clear tape)

- No ink/toner only special paper
- Simple construction
	- Feed Roller using friction to keep paper in place; remove debris!
	- Heating element, to clean IPA alcohol or cleaning pen

- Thermal Paper
	- Thermochromic paper  
    - Paper covered w/a chemical

###### **Impact Printers 3.8**

- Ink/toner on ribbon _(Scribbled out in original)_
- Dot Matrix printer
	- Printhead with small matrix of pins, moves back/forth
	- Presses against ribbon to mark paper
	- Good for carbon/multiple copies, low cost per page  
	    - NOISY, poor graphics  
	    - Niche uses

- Print ribbon, one long piece inside printer
	- Ribbon cartridge manufacturer specific, modular (1 piece)

- Tractor Feed page, holes on sides (tractor paper) perforated
- Multipart paper, carbonless, Ink on back of 1st sheet & clay 2nd
- Replace ribbon when ink is light looking
- Print head Need to be replaced, pins might not contact paper.

### Section 4
###### **Virtualization Concepts    4.1**

- One computer, many O.S.'s  
	     • macOS, Win11, Linux, all at once!  
	     • Each OS has own: OS, CPU, RAM, Network  
		     -Really 1 comp  
	     • Host based virtualization  
		     -Runs off OS desktop (primary OS + virtualization  
	     • Enterprise environment  
		     -Standalone server w/ multiple virtual machines  
	     • IBM introduced in 1967

- Sandboxing  
	     • Isolated testing environment, for code & on diff OS's  
	     • No connection to production sys  
	     • Have snapshot of working environment  
		          -If something you try breaks, rollback to known working config  
	     • Used to develop apps

- Legacy software  
	     • If software only runs on win xp you can VM older OS to run app

- Crossplatform virtualization  
	     • Run diff OS's on same comp, (win & macOS) & at same time. No Reboot!

###### **Virtualization Services   4.1**

- Hypervisor (Virtual machine manager)  
	     • Manages virtual program & physical system  
	     • Run on almost any sys but take advantage of CPU's built for virtualization  
	     • Allocated separate space for  
		- CPU, Network, security on each virtual OS

- Types of Hypervisor  
	     • Bare metal (Type 1)   
          +------------------------------------------+  
          | [Virtual Machine] | [Virtual Machine]     |  
          | App A                  |                       App B |  
          | Guest OS             |                  Guest OS |  
          +--------------------+---------------------+  
          | Hypervisor |  
          +------------------------------------------+  
          | Hardware |  
          +------------------------------------------+

     • Hypervisor acts as Primary OS  
          — Hyper-V, Xen project, etc.  
     • Each instance adds overhead & complexity; CPU  
       usage, etc.  
     • Hosted (Type 2)  
	          -Hypervisor runs in primary OS  
	          -Virtual machines run on top of current OS  
		  -VMware, Parallels, VirtualBox
          +--------------------+---------------------+  
          | [V.M] |                                           [V.M] |  
          | App A                    |                     App B |  
          | Guest OS               |                Guest OS |  
          +--------------------+---------------------+  
          | Hypervisor |  
          +------------------------------------------+  
          | OS |  
          +------------------------------------------+  
          | Hardware |  
          +------------------------------------------+

- CPU support  
	     • Intel: Virtualization Tech (VT)  
	     • AMD: AMD-V  
- RAM (memory)  
	     • Hypervisor allocates physical RAM to each VM OS  
- Disk space (HDD/SSD)  
	     • Each VM has own image, requires space for data  
- Network  
	     • Configurable for each VM OS (guest OS)  
	     • Virtual switch  
	     • Client side virtual managers have own internal networks  
		     -Hypervisor determines if guest OS can only communicate to self or comm outside of VM  
     • Shared Network address  
	     -VM shares same IP as physical host  
	     -Private IP internally / own subnet  
	     -Use NAT to convert to physical host IP  
     • Bridged Network address  
	     -VM (guest OS) acts like a device on physical network, NO NAT  
     • Private address  
	     -VM does not comm outside of virtual network

- Security  
	     • VM escape  
		     -Malware on VM, escapes VM, comms w/ other guest OS  
		     -Malware on 1 server can gather intel on another server or diff VM  
	     • Self contained OS gives traditional sec controls  
		     -Host based firewall, anti-virus / spyware  
	     • Attackers publish own VM w/ malware  
		     -Don't run published VM's  
		               • Create your own  
- VDI (Virtual Desktop Infrastructure)  
	     • Desktop as a service (DaaS)  
	     • Apps run on remote server, local mouse, keys, & screen  
	     • Local comp has minimal memory & CPU needs  
	     • Needs Network connectivity  
- Application Containerization                                            
	     • Only virtualize apps; NO OS component                    +---|---|---|---|---|---+  
	     • Container built for every app, self contained             | A | B | C | D | E | F | (App)  
	     • Can only run apps for 1 OS; No cross platform          +---|---|---|---|---|---+  
	     • Less overhead, (CPU, RAM, HDD/SSD)                         | container software |  
                                                                                            +-----------------------+  
                                                                                              | Host OS |  
                                                                                            +-----------------------+  
                                                                                             | Hardware |  
                                                                                            +-----------------------+

###### **Cloud Models   4.2**

- Deployment models  
	     • Public, available to everyone on internet. (Amazon AWS)  
	     • Private, your own virtual local data center  
	     • Hybrid, mix of public/private  
	     • Community, several orgs share same resources

- Infrastructure as a service (IaaS, HaaS)  
	     • Also known as Hardware as a Service (HaaS)  
	     • Renting time on piece of Hardware in cloud infrastructure  
	     • You're responsible for  
		   -OS, updates, sec  
	     • Provider has access to hardware but data is under your control only  
		      -Very secure for data, but more work  
	     • Web server providers (example)

- Software as a service (SaaS)  
	     • On demand software  
		     -Login to sys (usually web based) & use apps  
	     • No app management, No OS updates, No software or code management, No data              management  
		     -Your data is out in the open for provider  
	     • No app development work, provider handles everything  
		     -Gmail, Microsoft 365

- Platform as a Service (PaaS)  
	     • Middle of IaaS & SaaS  
	     • No OS, data management, data center  
		   - You DO have to build software (app)  
	     • Sec professionals watch your data, infrastructure.  
	     • Build app w/ building blocks available on platform.  
		    -Develop apps w/ modules (Microsoft Azure App Service)

- Responsibility matrix  
	- On prem = all customer managed
	- IaaS = from OS's up to Data customer managed provider handles physical
	- PaaS = Cx handles Accounts to data; provider handles physical to OS's. Hybrid handling of network control to directory infrastructure, & apps.
	- SaaS = Cx handles Accounts to data; provider handles physical to apps. Hybrid control of directory infrastructure.

###### **Cloud Characteristics  4.2**

- Costs  
	     • Private, only has up front costs  
	     • Public, up front or metered costs  
		   -Metered you pay what you use  
			  • Upload (ingress)  
			  • Storage  
			  • Download (egress)  
		  -Non-metered  
			   • Pay for block of storage  
			   • No cost to up/download
- Characteristics of cloud
	• Elasticity, seamless scale up/down on needs  
	• Availability, redundant systems always avail.  
	• File sync across world servers.  
	• Multitenancy, multiple clients using same cloud.  
     
### Section 5
###### **Hardware Troubleshooting  5.1**

- POST (Power On Self Test)  
	    • Checks CPU, BIOS, RAM, Video  
	    • Err & you get beeps/codes

- Boot & POST  
	    • Blank screen ON boot  
		-Bad video, RAM, &/or CPU  
		-BIOS config issue  
	     • Boot to incorrect device  
		-Boot order in BIOS config  
		 -Confirm valid OS in startup device

- Blue screen of Death (Windows)  
	     • Windows stop error  
	     • Contains info  
		-Stop code/err code or driver name  
	     • Also written to event log  
	     • Bad hardware, drivers, apps  
		-Startup & shutdown BSOD  
	     • If started after a change  
		-Use last good known config, sys restore, or  rollback driver  
	               • Try Safe mode (if BSOD on startup)
	 • If hardware related  
		 -Reseat RAM, PCIe cards, etc.
		 -Run hardware diagnosis
	               • Manufacturer or BIOS options

- Application crash screens  
	     • Every app has proprietary err messages  
		 -Some detailed, others vague  
	     • Document all info & check w/ manufacturer  
		 -Screenshot err message

- No video after Windows loads  
	     • F8 ; Video config issue; use VGA mode

- Power issues  
	     • Fan spins, no power elsewhere  
		-Check known good connections (device → power source)  
		-No video POST err.  
	               • Bad motherboard or graphics card  
		-If only fans work  
	               • Check all power supply outputs

- Slow performance (comp)  
	     • Check Task Manager for  
		      -CPU utilization, RAM, disk, Network %  
		      -App I/O data tx, or CPU usage  
	     • Generic & not app associated  
		     -Run Windows update  
	     • Disk space, if low runs slow  
		    -Run defrag  
	     • Laptop might be in power saving mode  
		   -CPU throttling  
	     • Run Anti-virus/malware  
		  -Verify no malicious software

- Overheating  
	     • Check fans, heat sinks, airflow, dust, & make sure its clean  
	     • Verify with monitoring software  
		  -Built into BIOS or HWmonitor (cpuid.com)

- Random shutdown  
	     • No warning, black screen / off  
		  -Check event viewer  
	     • Heat related issues commonly  
		  -Check overheating, failing hardware (diag)  
		  -Could be anything, process of elimination

- App crashes  
	     • Check event viewer, logs, and reliability monitor  
	     • Uninstall & reinstall app  
		 -Contact app support  
		 -If problem persists, not install issue

- Noises  
	     • Rattling - loose component  
	     • Scraping - HDD  
	     • Clicking - Fan  
	     • Pop 
		  - Blown capacitor (comes w/ unusual smell)

- Bad Date/Time  
	     • Motherboard batt is dead  
	     • Older comp BIOS reconfigure

- Smells / smoke  
	     • Burnt, immediately disco power  
	     • Look for bad components, sniff around  
	     • Most likely electrical

###### **Storage Troubleshooting   5.2**

- Extended read/write time  
	     • Path  
		 -RAM access, bus comm, HDD acess, read/write to drive  
	     • Delays occur anywhere  
	     • IOPS (Input/output operations per second)  
		 -Broad metric of performance  
		 -HDD : 200 IOPS, SSD : 1,000,000 IOPS

- Missing drives in OS  
	     • OS boots normal but drives missing  
		 -Check BIOS enable/disabled drives  
		 -Internal drives, check cables/bad drive  
		 -External drives, no power / bad cable or connection  
	     • Network shared drives  
		 -Usually connected during startup  
		 -"Map Network drive" - select reconnect at sign-in  
		 -Connect w/ login script

- Array missing  
	     • Drive controller going bad (RAID)  
		 -Missing or Faulty

- Data loss/corruption  
	     • Always have backup!!!

- RAID  
	     • Power, hardware, or comm issue  
	     • Usually obvious; err message, email, alarms  
	     • Storage/RAID Manager will tell you  
	     • RAID 0      2+ disk req  
		  -1 drive failure = data loss  
	     • RAID 1      2+ disk req  
		  -1 drive fail = no data loss  
	     • RAID 5      3+ disk req  
		  -Can lose 1 drive & still work  
	     • RAID 6      4+ disk req.  
		 -Can lose 2 drives & still work  
	     • RAID 1+0 (10)   4+ disk req  
		 -Can lose 1 drive from each mirror & still work.  
	               • So long as 1 drive from each mirror is up will work

- S.M.A.R.T.  
	     • Self-Monitoring, analysis, & reporting Tech  
	     • Tech inside that tracks performance of drive  
	     • 3rd party software, analysis for you of info  
	     • Warning signs = replace drive

- Failure symptoms  
	     • Read/write failure  
		-"Can't read from source disk"  
	     • Slow performance  
		-Keeps retrying, constant led ON  
	     • Loud clicking noise  
		-Click of death, as keeps retrying to get data

- Troubleshooting  
	     • Get backup asap once issues start  
	     • Reseat cables, check if damaged  
	     • Overheating?  
	     • Check power supply  
	     • Run HDD diagnosis

- Boot failure  
	     • Beeps/lights (always on or off)  
	     • Error messages  
		 -OS Not found message  
			 -Drive available / OS image Not  
	     • Check data & power cables  
		 -Try diff SATA interface  
	     • Check BIOS boot sequence  
	     • Try different computer

###### **Network Troubleshooting  5.5**

- No Network connectivity  
	     • Link light ON/flashing?  
		  -For ethernet/wired connection

- Ping Loopback 127.0.0.1  
	     • Pinging your own device  
	     • To test IP stack  
		  -Any issues w/ network config & no pingback will occur

- Ping local IP address  
	     • Your own IP to verify link & connected to lan

- Ping Default gateway  
	     • Check IPconfig for gateway IP & ping  
		  -Confirms comm between your device & another device on the network

- Ping outside of LAN  
	     • Ping DNS 1.1.1.1, 8.8.8.8, 9.9.9.9

- Slow internet speed  
	     • Confirm connectivity  
		 -Ping across network eval response times  
		 -Speed test  
	     • Evaluate each Network hop  
		 -Utilization on each link, errors, throughput, Firewall filter/ACL
	 • May require a packet capture  
		-Best verification  
	               • Network or app related

- Limited or No connectivity  
	     • Check local address  
		-If APIPA 169.254.0.1 - 169.254.255.254 only local connection  
		      • Could be DHCP problem  
		-If DHCP IP then ping gateway/remote IP  
		      • When you no longer get ping response troubleshoot

- Jitter  
	  • Time of data packet arrivals  
		   -If time between packet frames is large then info is missed; choppy calls

- Port flapping  
	     • Link light goes on/off on repeat  
	     • Usually cable/connector related  
		-Could also be a port issue

- Intermittent Internet connectivity  
	     • Ongoing Ping 1/sec  
	     • Traceroute to known location  
	     • Ongoing speed tests