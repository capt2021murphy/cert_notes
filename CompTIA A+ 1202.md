[[CompTIA A+ 1201]]
                                               

#### **Section 1**
###### **OS Overview      1.1**

- Operating systems  
	     • Link between Apps & physical hardware  
	     • Control interactions between hardware components  
	     • Human interaction w/ comp.

- Standard OS features  
	     • File management  
		   -Add, delete, rename  
	     • App support  
		  -RAM management, file swap from RAM to storage  
	     • I/O support  
		  -Printers, key & mouse, USB, video, storage, etc  
	     • OS config & management tools  
		  -Utilities to maintain OS/hardware

- Microsoft Windows  
	     • Many versions ; Win 10/11, Win Server  
	     • PROS                                                       • CONS  
	          — Large support base                         — Large group of attackers, sec  
	          — Variety of OS options                            exploitation  
	          — A lot of software & support           — Supports a lot of hardware  
	          — Large sec experts for OS                      can cause integration issues

- Linux  
	     • UNIX-like, not UNIX  
		  -Written in C like Unix  
	     • Many different distributions  
		  -Ubuntu, Debian, Red Hat / Fedora  
	     • PROS                                                       • CONS  
	          — Free!                                              — Limited driver support, especially laptops  
	          — Works on a lot of hardware          — Limited distro support options  
	          — Active user community

- Apple MacOS  
	     • Desktop OS only for Apple Hardware  
	     • PROS                                                       • CONS  
	          — Easy to use, easy GUI                      — Need Apple hardware  
	          — Very compatible, Hardware/OS all  — Higher initial cost  
	              by Apple                                          — Less support than PC platform  
	          — Less security concerns

- Chrome OS  
	     • Created by Google  
		 -Based on Linux Kernel  
	     • Most of OS based on Chrome web browser  
		 -Most apps are web based  
	     • Many Manufacturers, less expensive hardware  
	     • Relies on Int & cloud ; cloud based apps  
		 -Needs good internet connection

- Apple iPad OS  
	     • Variant of Apple phone iOS  
	     • Tablet features  
		  -Safari (Desktop version)  
		  -Sidecar (2nd monitor)  
		  -Keyboard support  
		  -Multitasking

- Apple iOS (iPhone)  
	     • No access to source code  
		 -Closed-source; all apple iOS are  
	     • Unix based  
	     • Only runs on apple hardware

- iOS Apps  
	     • Apps developed w/ Apple's SDK on MacOS  
		 -SDK = software developers kit  
	     • Apps must be approved by Apple before release  
	     • Apps on app store

- Google Android  
	     • Mobile device OS ; supported by many manufacturers  
	     • Open source, Linux based  
	     • Maintained by Open Handset Alliance  
		 -Many companies put together

- Android Apps  
	     • Can develop apps from Windows, macOS, & Linux w/ Android SDK  
	     • Apps available from google play store & 3rd party sites

- Vendor-specific limitations  
	     • End of life (EOL)  
		 -Policies vary by company  
	     • Updating OS/software  
		 -iOS, Android, & Windows check & prompt for updates  
	               • Can manually change settings as some OS  
		 -Chrome OS auto updates  
	     • Compatibility between OS's  
		 -File extensions for media can be similar/compatible  
			 • Movies, music, documents, etc.  
	     • Almost no direct app compatibility  
		 -Can't run .exe files in macOS or Linux  
		 -App must be built to run on OS  
		 -Pros to this issue  
			  • Many apps built to operate on many OS's  
			  • Web-based apps bridging gap

###### **File systems    1.1**

- Formatting partition  
	     • Done before data can be written to partition (storage)  
	     • Determines file system for partition  
	     • All data will use formatting type by OS  
		   -OS's use specific formatting types  
		   -Some file systems used by many OS's (read/write)  
			   • FAT, FAT32, NTFS, exFAT, etc.

- NTFS = NT File System  
	     • Improvements over FAT32  
		     -Features like file compression, encryption, recoverability, large file support, quotas, other management features  
	     • Mainly used ON Windows  
		     -Not very compatible across OS's  
			   • Many OS's read but don't write NTFS  
			   • Some OS's do write NTFS ; beside windows

- Resilient File System (ReFS)  
	     • Nextgen Windows file system  
		   -Upgrade to NTFS  
	     • Limited integration in  
		   -Server 2012 & later & Windows 8.1 & later  
	     • Huge storage requirements  
		   -Support for very large drives & storage arrays  
		    -Designed for desktop & server environments
	   • Constant data avail (Resiliency)  
		    -Self-repairing, constant integrity checks, no chkdsk!  
		    -RAID like redundancy is built in  
	     • Not widely installed  
		     -Measured rollout ; updates currently ongoing

- FAT / FAT32 (File Allocation Table)  
	     • FAT one of 1st pc based file systems (circa 1980)  
	     • FAT32 more recent version  
		    -4TB volume (drive) sizes  
		    -Max file size of 4Gb  
	     • exFAT (extended FAT)  
		    -Microsoft flash drive file sys  
		    -Files larger than 4Gb  
		    -Compatible across many OS's  
			      • Windows, Linux, macOS

- ext4 (4th extended file system)  
	     • Update to ext3 ; common to Linux & Android OS

- Extended File System (XFS)  
	     • High performance Linux file system ; most Linux distro's  
	     • Designed for large scale computing & high speed processing  
	     • Enterprise features  
		      -Large file system size support          
		      -Minimal fragmentation  
		  -Built in Journaling ; Min data corruption

- APFS (Apple File System)  
	     • Available from macOS High Sierra (10.13.4) on  
	     • Also included in iOS & iPadOS  
	     • Optimized for SSD's  
		   -Built in encryption, save/restore from snapshot, & increased data integrity

###### **Installing OS's     1.2**

- Boot Methods  
	     • How to install an OS w/o an OS on comp?  
		  -Boot to install barebones OS program using USB, external HDD, etc.  
	     • USB storage  
		  -Must be bootable  
		  -Comp must support booting from USB  
	     • Network Boot  
		  -PXE (Pixie) Preboot eXecution Environment  
		  -Computer must support booting w/ PXE  
		   -Remote network install  
			   • Start comp & it looks for PXE server then boot & install  
	     • Store in SSD/HDD (OS's)  
		    -Store OS's
	  • Internet boot/install  
		    -Linux distros, macOS recovery install, Windows updates  
	     • External/ hot swappable  
		    -Optical disc can mount from ISO image (cd)  
	     • Internal hard drive  
		    -Install files avail on partition in storage  
		             ↓
		    -Install to separate partition on same storage  
	     • Multiboot  
		    -Multiple OS's on same comp  
			      • Different partitions or drives (usually partitions)  
		    -Select OS to boot ; Windows, Linux, etc.

- Types of Installations  
	     • Clean install  
		     -Wipe partition/drive clean & install OS  
		           • No saved files will remain  
		     -Migration tool can help  
	     • In place upgrade  
		    -New version of OS  
		    -Keeps all data, apps  
	     • Image deployment  
		   -Install OS, apps, & config on 1 comp  
		   -Clone by creating an image (ISO)  
		   -Install image on all other comps  
		   -Can be automated! (PYTHON!)
	 • Remote Network Install  
		   -Put install files on network drive, shared drive, or local server  
		   -Install across Internet instead of local media  
	     • Recovery Partition  
		   -Usually hidden w/ install files  
	     • Repair install  
		   -Leaves base config but copies all else  
			    • Only replaces corrupt, missing sys files & fixes broken registry entries  
		   -Doesn't modify user files  
			   • Overwrites OS files  
		   -Fix major OS problems that can't be fixed another way  
		   -May cause driver/hardware issues  
			   • 3rd party drivers will fix issue

- Zero touch deployment  
	     • Many systems & users on varying hardware  
	     • Almost or entirely auto install, streamlines w/ no to minimal prompts ; script install  
		 -Config files injected to ISO ;  
		 -Has company spec configs  
	     • Once laptop is set up send anywhere

- Disk partition
    • Physical drive split into logical sections, not always needed
    • Useful to separate data
    • Used for having separate OS's
        - Linux, Windows, etc.
    • Formatted partitions
        - Called volumes by Windows

- GPT partition style
    • Globally Unique Id partition table (Guid Partition Table)
        - latest partition format standard
    • UEFI Bios is required
        - 128 max partitions
        - Max partition size of 9 billion TB
        - Windows max partition 256 TB

- MBR partition style (Master Boot Record)
    • Old standard; max partition of 2 TB
    • Primary partition
        - only bootable partition, 4 max per drive
        - Only 1 is active at a time, changed in partition software
    • Extended
        - 1 ext partition per drive, within can have many logical parti.
        - logical partitions are not bootable
- Disk partition continued
    • 1st step to OS install
        - may be done already
        - partitions may not be compatible w/ OS
    • GUID partition needs UEFI BIOS or BIOS-compatibility mode
        - BIOS compatibility mode disables secure boot

- Quick vs. Full format
    • Quick creates file table
        - Doesn't physically check storage
        - Erases file sys table as if no prior data installed
            • Old data could be recovered
            • Not secure install
        - Default setting for Win 10/11
            • Use diskpart to change for full format
    • Full format
        - Writes 0's to entire disk, time consuming
        - Data is unrecoverable; secure
        - Checks for bad drive sectors (storage)

###### **Upgrading Windows     1.2**

- Upgrade vs. install
    • Upgrade keeps files in place; apps too. (inplace upgrade)
    • Install deletes files & starts fresh from 0%. (clean install)

- Reasons to upgrade
    • Many local users
    • Custom configs
    • OS upgrades all else remains (apps, documents, settings)
        - No backup/restore
        - Faster to get backup & running

- Clean install
    • Wipes everything & reloads
    • Must backup wanted files
    • Install by booting from install media

- Prepare boot drive
    • Check drive 1st; is it formatted? How many & what partitions?
    • Back up any & all old data needed
        - may need old data & user settings/preferences.
    • Most partitioning & formatting can be done during install

- Prior to install
    • Check OS min. requirements & recommended req:
        - RAM, storage, etc.
    • Microsoft has a compatibility check
        - Run before upgrade or manually
        - "PC Health Check" for Win 11
    • Plan for install q's
        - What drive? & partition configs
        - App & OS license keys
    • Some apps & drivers not compatible in new OS

- Life cycle calenders (Windows)
    • Says: when OS is in support & when support is stopped
    • Quality Updates
        - Monthly sec update & bug fixes
    • Feature updates
        - New capabilities; every 6/12 months
            • used to be 3-5 years
    • Support life after release
        - 18 to 36 months; OS version & edition dependent
    • More info lookup "Modern Lifecycle Policy"

- Win 11 hardware req.
    • Added req. from Win 10
    • ex. TPM 2.0 (Trusted Platform Module)
        - must be 2.0
        - Used for Bitlocker, Windows Hello, & other Win features
    • - to check TPM details
        • run tpm.msc
    • UEFI Bios required
        - must be able to secure boot
        - To enable secure boot
            • Sys info utility -> Sys summary -> Secure Boot state
    • Not available on legacy BIOS systems

###### **Windows Overview     1.3**

- A+ core 2 exam
    • Win 10/11; in support Windows on exam
        - 10/11 are very similar

- Win 10
    • Release July 29, 2015; Win 9 skipped
    • Single platform for:
        - Desktops, laptops, tablets, a-i-o devs, & phones
            • Didn't exactly pan out like that
    • Win 10 support ended 10/14/2025
        - Last update v. 22H2 released 7/14/2026
        - Extended Sec Updates (ESU) program get sec patches
          until 10/12/2027

- Win 10 Home (retail)
    • Integrates Win w/ Microsoft acct &
        - Microsoft OneDrive backup (auto backup)
    • Windows Defender; anti-virus/malware
    • Cortana; voice interaction

- Win 10 Pro (Business)
    • Added management features
    • Remote Desktop host
        - Any pc (Windows) can access host pc
    • Full Disk Encryption (FDE) through Bitlocker

    • Join Win domain
        - Group Management policy

- Win 10 Pro for Workstations
    • High end edition desktops (gaming, etc)
        • Up to 4 CPU's supported
        • Max 6TB of RAM
        • ReFS support
            - Resilient file sys ; used in Win Server

- Win 10 Enterprise
    • Volume licensing
        - Used for large implementations (100-1000's)
    • AppLocker
        - Admin feature controlling what apps can run
    • BranchCache
        - Remote site does file caching
        - Reduces WAN bandwidth
        - User request -> retrieved from main server ->
          -> stored in local cache for future requests
    • Granular User Experience (UX) control
        - Define what users see on desktop
            • What features are available
        - Useful for kiosk's & workstations

###### **Win 10 Overview    1.3**

- Win 10 edition    Domain      Remote      Group Policy    Max       MAX
-                             Access       Desktop                           x86 RAM   x64 RAM
    • Home                X                 X                  Client          4GB       128gb
    • Pro                    ✓               ✓              Client/Host     4gb        2TB
    • Pro Wrkstation ✓               ✓                   C/H             4gb       6TB
    • Enterprise         ✓               ✓                   C/H             4gb       6TB


- Win 11
    • Released 10/5/2021
    • No 32 bit CPU support ✯
    • Updated user interface (desktop)
        - New start menu & taskbar widgets
    • Usability updates
        - Snap layouts
        - Integrated Microsoft Teams
        - Better touch based integration (tablets) -> (easier to use)
    • Copilot AI assistant

- Win 11 Home (retail)
    • Integrated with Microsoft acct
        - Can run w/ local acct
    • No Active directory support ; limited management functionality
    • Includes Device Encryption
        - Retail version of Full Disk Encryption (FDE)
        - Recovery info in user's Microsoft acct

- Win 11 Pro
    • Designed for business ; large scale management
    • integrates w/ Microsoft directory services
        - Active directory ; centrally managed from 1 place
    • BitLocker (FDE) available
    • Integrated virtualization capabilities
        - Microsoft Hyper-V
    • Remote Desktop as client/Host

- Win 11 Enterprise
    • Volume licensing for large deployments
        - Server features
    • Device Management included
        - Mobile device management (MDM)
        - Mobile App Management (MAM)
    • ReFS support (resilient file sys)

- Win 11 version    Domain      BitLocker   Remote          Group Policy    Max x64 RAM
-                              Access                        Desktop

    • Home         X           X     Client          X          128 gb
    • PRO          ✓           ✓   Client/Host       ✓          2TB
    • Enterprise   ✓           ✓       C/H           ✓          6TB

- Windows N (EU Commission only)
    • "NO" -> Win Media player ; due to EU Commission anti trust investigation
    • No multimedia utilities built in can be added later
    • Settings -> Apps -> Optional features -> Add optional ft -> Media ft Pack

###### **Windows Features      1.3**

- Windows @ work
    • Large scale support
    • Sec concerns

- Domain Services
    • Active Directory Domain Services
        - Central Database ; documents everything
        - User names, permissions, security info, etc.
            • Printers, servers, volumes
        - Distributed architecture topology
            • Can have multiple versions across network
            • Provides scalability & redundancy
        - Many uses
            • Authentication
            • Shared drives
            • Central management

- Windows Workgroup
    • Logical group of network devices @ home / small office
    • Each device is a standalone system ; all are peers
        - Workgroup manages each device as a single unit

- Windows Domain
    • Business Network
    • Centralized authentication & device access
    • Supports thousands of devices across many networks

- Work Desktop
    • Standard among active directory ; common user interface
    • Easier to manage & can work on any comp
    • Limited customization ; unlike home comps
- Home
    • Customizable desktop ; background, fonts, colors, UI sizing, etc.

- Remote Desktop Protocol
    • View & control desktop of a remote device
    • RDP client needed to connect to remote device
        - Software that connects to a remote desktop service
        - Clients available for almost all OS's
    • Remote Desktop Service
        - Software on remote device that allows connection
        - Provides access for RDP client
        - Available on Win 10/11 Pro & ENT ; NOT Home
- BitLocker encrypts everything on storage drive ; even OS (FDE)
    • Full Disk Encryption (FDE)
- Encrypting File Sys (EFS) protects individual files/folders
    • Built into NTFS file system

- Group policy editor
    • Centralized management of users & systems
    • Policies can be part of Active Directory or local sys
    • Local group policy ; 1 comp - manages local device
        - gpedit.msc (group policy editor)
    • Work (Business) Group policy management console
        - Active Directory Integrated
        - gpmc.msc


###### **Task Manager      1.4**

- Real time stats
    • CPU, RAM, disk access, etc.
- To access:
    • Alt + Ctrl + Del -> select task man. , Shift + Ctrl + ESC , 
    & right click taskbar -> select task Manager.

- Services tab (within Task Manager)
    • Background processes ; non-interactive apps
    • Manage services ; start, stop, restart
    • To open services -> right click a service -> open services

- Startup apps tab
    • Toggle on/off apps that start on boot

- Processes tab
    • All currently running apps & background processes
    • Shows how much each app is using in terms of
        - CPU, RAM, Disk, Network, power, etc IN %

- Performance tab
    • Utilization % displayed in graph (60 sec)
    • CPU, RAM, Disk, Network in realtime (& more (GPU))

- Users Tab
    • Shows active users & what apps/resources are
      being used
    • If others connected across network, they'll show
      up here

###### **Microsoft Management Console (MMC)  1.4**

- Build custom utility view (of console)
    • mmc.exe
    • Empty lot can add utilities like :
        - Event viewer, disk management, local users/groups, & more
    • To add utilities (snap-ins)
        - Ctrl + M or File -> Add/Remove snap in
        - Will ask local comp or another -> browse
            • another looks for comps on network group
    • Save console! then can pull up

- Event Viewer
    • Consolidated view of everything happening in Windows
        - Windows log viewer
            • App, security, setup, system
            • Level mark:
                - Info, warning, err, critical, success audit
                  failure audit
    • eventvwr.msc ; to start app

- Disk Management
    • See storage drives, partitions, & file sys.
    • diskmgmt.msc ; to start app
    • ✯ Can erase data!!! Always backup

- Task Scheduler
    • Plan to run apps or scripts
    • Predefined tasks/schedules built in ; easily to automate
    • taskschd.msc ; to run app

- Device Manager
    • See device drivers & associated hardware
    • Device drivers tend to be associated w/ OS
        - Win 10 drivers wont work on Win 11
    • devmgmt.msc ; to open app

- Certificate Manager
    • Certs authenticate & encrypt data
    • View user & trusted certs
    • certmgr.msc ; to open app

- local users & groups
    • Many user accts & privilege types
        - Admin : super user, Regular : Normal, Guest : limited
    • Groups
        - Admins, Users, Backup operators, Power Users, etc.

- Performance Monitor (Not task manager performance)
    • Gathers long term stats of comp
    • Disk, RAM, CPU, etc.
    • Analyze & store statistics. Build reports too!

- Group policy editor
    • Features avail for users
    • Central management of users/sys
        - Policies part of Active Directory or local sys
    • Local group policy editor
        - gpedit.msc
    • Group policy management console
        - Active directory integration
        - gpmc.msc

###### **Additional Windows Tools     1.4**

- System overview
    • msinfo32.exe ; to open app
    • View RAM, Direct memory (RAM) Access (DMA) ->
        -> Bypasses CPU and frees up CPU processing), IRQ's
        (Interrupt Request) (hardware signal to CPU causing
        pause to deal w/ urgent matter, conflicts.
    • Components
        - Multimedia, displays, Network, input, ports (serial), etc.
    • Software environment
        - Drivers, print jobs, running tasks
    • No changing but gives detailed info in one place

- Resource monitor
    • Detailed real time statistics separated by category
        - Overview, CPU, RAM, Disk, & Network
    • resmon.exe ; to open app

- System Configuration
    • Manages boot processes, startup, services, etc.
    • msconfig.exe ; to open app
    • Can completely configure boot, startup, services,
      on starting comp
        - can also use tools (Resource monitor, etc.)

- Disk cleanup
    • Quick / efficient way to clean/free up space
    • cleanmgr.exe ; to open app

- Disk Defrag
    • For spinning drives ; NOT for SSD's
    • Storing files are separated into sections
        - Defrag moves file fragments so they are contiguous
        - Improves read/write times
    • GUI interface located in disk properties or
        - Command line :
            • defrag (volume) (format)
              defrag c:        (example)

- Windows Registry editor
    • Config options apps, OS settings, sys policies, etc.
    • Huge Master Database
        - Hierarchical structure
    • Used by everything
        - Kernels, device drivers
        - User interface
        - Services and more!
    • Always Backup! (Export whole or section (hive))
        - Especially if you make changes
        - Best practice just in case
    • regedit.exe ; to open app

###### **Windows Command Line Tools   1.5**

- Privileges on command prompt
    • Standard users
        - No changes to OS config or apps
    • Admin
        - Allows all commands
        - Run as admin, Ctrl + Shift + Enter
        - cmd ; to open app

- "Help"
    • Gives description of commands
    • Help with a specific command
        - help dir
        - help chkdsk, etc. or
        - chkdsk /? , dir /?

- Navigation
    • "dir"
        - Lists files & directories
    • "cd" or "chdir"
        - change working directory
        - \ to specify volume or folders
    • ".."
        - 2 dots to go back 1 directory

- Editing
    • Make directory "mkdir" or "md"
        - create a folder/directory
    • change dir "cd" or "chdir"
    • remove directory "rmdir" or "rd"; "del" for files
        - delete folder/directory ; "del" for files

- Check disk
    • Fixes errors for logical file sys corruption
        - chkdsk /f  (/f is to fix)
            • needs admin privilege
    • Sector by sector diagnosis of entire drive
        - chkdsk /r  (recover readable data)
            • implies /f w/(/r)
    • Can only perform chkdsk on startup

- "format"
    • Formats a disk w/ file sys to use w/ Windows
        - e.g. : "format e: /fs:refs"
            • Format drive e: w/ file sys "ReFS"
    • careful when using, erases data!

- "diskpart"
    • Manage disk partitions, "list volume", format partition, diagosis

- "copy"
    • "/v" or "/y"
        - "/v" or "copy /v" verifies new files written correctly
        - "/y" or "copy /y" verifies you want to overwrite
          existing destination file & suppresses confirm prompts

- Robust copy
    • "robocopy"
        - Better copy with more options

- "hostname"
    • Tells you name of device you are connected to
        - useful when working on multiple terminal tabs
    • Shows Windows device name

- "winver"
    • displays windows version

- "whoami"
    • User, device name, groups, & security permissions (SID)
                             (s)       (ID)
    • "whoami /all"

- Managing group policies
    • Usually updated at login
    • Manage comps in Active Directory domain
    • "gpupdate" to force a group policy update
                                ▲
        - "gpupdate /c : {comp/user} /force"
                            or "target"
        - "gpupdate /target:user /force"
    • "gpresult"
        - verifies policy settings for comp/user
          or
        - "gpresult /r" shows active policies
        - "gpresult /user (target username) /v"

- "SFC"
    • System file checker
        - Scans integrity of core Windows files
        - Checks for changes & can correct errors/changes

###### **Windows Network Command Line     1.5**

- "ipconfig"
    • Will give info on Network config
        - Your IP, subnet, default gateway, type of connection
        - DNS servers, DHCP, etc.
    • "ipconfig /all"
        - Gives more info; DNS, mac addy, protocols, etc.

- "ping"
    • Verifies IP is connected to network, reachability
        - Determines round-trip time, packets sent/received/
          lost
    • Uses ICMP, Internet control message protocol

- "netstat"
    • Shows network connections to your comp
    • "netstat -a" ; shows all active connections
    • "netstat -b" ; shows what binaries using connections
        - binaries means .exe, so what apps using internet
        - requires admin or elevated privileges
    • "netstat -n"
        - Avoids DNS resolution showing IP instead of domain

- "nslookup"
    • Finds info on DNS servers you're connected to
        - Canonical names, IP's, cache timers, etc.
    • ex. nslookup ://professormesser.com

- "net"
    • Windows OS info on how it connects to other devices
    • "net view"
        - view network resources
        - "net view \\(servername)" or
          "net view /workgroup:(workgroupname)"
    • "net use"
        - connect to network resource
        - "net use drive: \\(servername)\(sharename)"
    • "net user"
        - View acct info & reset passwords
        - "net user (username)" or "net user (username) *
          /domain"

- "tracert"
    • To see all connections between your comp & destination IP
        - shows route packet takes to destination, maps path
    • Uses ICMP & features like Time to live exceeded
        - TTL refers to # of hops, not sec or MIN
        - TTL=1 is 1st router, TTL=2 is 2nd router
    • ICMP can be firewall filtered causing request time out.

- "pathping"
    • Combines ping & traceroute
        - Windows NT & later is included
    • 1st phase runs tracert
        - Builds map between comp & destination IP
    • 2nd phase
        - Round trip to each hop (time)
        - Packet loss per hop


###### **Windows Control Panel    1.6**

- To open:
    • Search -> type control panel -> click

- Internet options
    • Options for built in int browser
        - From general to sec, privacy, proxy, content (certs), addons, default programs, & advanced.

- Devices & printers
    • Devices on network & connected physically to comp
        - Desktops, printers, storage, etc.
    • Faster than device manager
        - Configuration, properties

- Programs & features
    • Shows all installed apps on comp
    • Can uninstall, repair, or reinstall
    • Can turn Windows features on/off from here too

- Network & sharing center
    • Shows all network adapters
        - Wired, wireless
    • Shows all network configs
        - Good to troubleshoot

- System
    • Computer, version, OS, RAM, CPU, etc. info

- Windows Defender Firewall
    • Protects from malicious software, attacks, & scans.
    • 2 sec policies for private networks & Guest/public Nets.
    • Integrated into OS ; control panel -> firewall (to open)

- Mail ; might not show unless you have supported app (Outlook)

- User Accounts
    • Local users ; domain (active dir) stored elsewhere
    • Acct name & privilege
        - Change password, icon, & manage encryption certification

- Device Manager
    • Device drivers & associated hardware
    • Manage devices ; add, remove, disable

- Indexing options
    • Modify Windows file index (for search queries)

- Admin / Windows tools
    • Sys tools for admins & techs
        - Not commonly used utilities
            • Registry editor, system config, task scheduler, etc.

- File explorer options
    • Privacy, click behavior, browse folder behavior, + more options

- Power Options
    • Power saver, hibernate, sleep, & associated settings
        - Fast startup, lid, usb, time to sleep/hibernate, etc.

- Ease of Access center
    • Accessibility features
        - Narrator, magnifier, on screen keys, high contrast

###### **Windows Settings    1.6**

- One place for config settings
    • Migration from control panel

- Date & Time settings ; Language
    • Time zone, auto time, etc.
    • Set different languages, & region

- update & Security
    • Auto update options
    • Security patches, bug fixes

- Personalization ; background, wallpaper, color, etc.
- Apps ; config apps. Install, uninstall, modify & on/off win ft.s
- Privacy & sec.
    • share or not app activity, language, speech recognition.
- Bluetooth & devices ; manage devices, connections, mouse, etc.
- Network & int ; Network settings, int status, proxy, VPN, IP, etc.
- Gaming ; Xbox gaming
- Accts ; modify Microsoft & local user accts.
    • Email, SIGN-IN(PIN / password), etc.

###### **Windows Network Technologies ✯   1.7**

- Shared resources
    • Folder or printer avail on network
        - Or any other resource
    • To access a share from another comp ON network
        - Assign a drive letter to share
            • Either from file explorer or (map network drive)
            • Command line "Net use"
    • To hide share add $ at end of name
        - Not sec feature, just hides it
    • To see all shares on comp
        - Computer Management -> Admin tools -> Shared
                                 (sys)

- Organizing network devices
    • Windows workgroups (local)
        - Logical grouping of network devices (home)
        - Each device is standalone, all are peers
            • Each dev maintains own u/n & p/w
    • Windows Domain (Active Dir Domain Services)
        - Business Network, consolidates credentials
        - Centralized management, authentication, & device access
        - Supports thousands of devices across many networks.
    • To view: System -> about -> Domain or workgroup 
    • Share Printer
	    -Similar to sharing a folder
	    -Printer properties to configure ->sharing

###### **Configure Windows Firewall  1.7**

- Windows defender firewall
    • Built into OS
    • Always enabled ; ideally configured too
    • May need to disable to troubleshoot
    • Can custom config for public vs. private network
        - Block all incoming ; including exception list
        - Can notify when new incoming is blocked
        - Allowed apps -> for granular control of apps allowed
          on which network (public/private)
        - Can block or allow port #
    • Advanced settings to add, modify, etc. rules
        - Can change, add, or delete
            • In, out bound rules
            • Connection sec rules
            • Or monitor active rules


###### **Windows IP address Configuration     1.7**

- DHCP (Dynamic host config protocol)
    • Auto IP addressing, default

- APIPA (Auto Private IP addressing)
    • No manual address or DHCP server, local connect only (No WAN)
    • 169.254.1.0 - 169.254.254.255, No internet connection
    • Static address
        - IP doesn't change
        - manually assign all parameters (IP, subnet, etc.)

- TCP/IP host addresses
    • Most important for config (static)
        - IP, unique id
        - Subnet mask, subnet id
        - Gateway (default gateway), route from subnet -> WAN
- DNS
    • Domain Name server (9.9.9.9) resolves to IP
    
- Loopback ; 127.0.0.1 ; internal IP of comp
    - Checks IP stack of local comp.

- *DHCP for business use multiple ; redundancy
    - If DHCP isn't available
        • Windows has alternate config (APIPA default)

###### **Windows Network Connections  1.7**

- Network setup
    • Control Panel -> Network & sharing -> Set up
      new network
    • or Settings -> Network & internet
    • Step by step wizard

- VPN concentrator
    • VPN client connects to VPN concentrator which decrypts data & sends it to target network.
      
        - ex. / Corporate \   / CONCENTRATOR \   / INT \   / Laptop w/  \

             |   Network  |---|     (VPN)      |---|     |---| VPN client |
              \          /     \              /     \   /     \          /
               ----------       --------------       ---       ----------

                    |                 ▲               ▲            |
                    |_________________|_______________|____________|
                                  "In clear"            L Encrypted

- VPN connection
    • VPN client, 3rd party or built in
        - Proton, Mullvad
        - Windows built in
    • Control Panel -> network & sharing -> Set up new connection or network -> connect to a       workplace-> use my internet connection (VPN)
            - Smart card is added authentication
                • Multi factor like password, bio, or smart card

- Wireless connections
    • Name(SSID), Sec type (Encryption WPA2/3), Encrypt type (AES, (older) TKIP), Sec key                (password) (Personal) -> pre-shared key or (Enterprise) -> 802.1X auth
        - Enterprise uses central auth server to check
- Wired connection
    • Fastest ; ethernet cable
    • Fastest = default connection
    • To edit default settings : Control panel -> Network &
      Sharing -> Network connections -> right click ethernet-> properties -> IPv4 -> properties

- WWAN connection
    • Wireless wide area network ; cell networks (5G)
    • Hardware adapter, usb ; antenna connections
        - Tether or Hotspot w/ phone
- Proxy settings
    • Internet middleman between device & WAN
    • To setup: Control panel -> Internet options -> Connections
      -> LAN settings -> Proxy server
    • Auto or manual proxy setup (Settings -> Net & int -> Proxy)
        - Can also add exceptions to apps that break w/ proxy
- Network locations
    • Private ; share & connect to devices
    • Public ; no sharing or connectivity. High security

- Network paths
    • To connect to network shares/drives
        • File explorer to, map a drive letter, to share
            - File explorer -> top right 3 dots -> map network drive
                ▲
              Must be on "This PC" page

- Metered connection
    • Network that charges based on usage
    • Change to metered connection.
        - Settings -> Network & internet -> Ethernet -> metered
        - Can set a data limit

- Setting up a share folder on my pc ran into issue
    • Firewall set up right but blocking cx file explorer(phone)
        - Inbound rule for File/printer share on for private
            • Echo IPv4, NB-session-IN, SMB-IN
        - Tried custom rule to allow all phone IP in, no go
        - Only worked when disabling firewall.
    • Very interesting keep troubleshooting another day

###### **MacOS Overview   1.8**

- File Types
    • .dmg
        - Apple disk image, similar to .iso
        - mountable as a drive in folder
    • .pkg
        - installer package, distributes software
        - Runs through installer script
    • .app
        - Application bundle
        - contains needed files to use app
        - to view; right click -> view package contents
          from finder

- App store
    • Centralized update & patches for OS & apps
    • Auto or manual update

- Uninstall process
    • Move .app bundle to trash & DONE
        - Some apps do include uninstall program

- macOS sys folders
    • /Applications
        - Folder for all apps

• /Users
    - Folder name of User
        • User documents saved inside folder tree
• /Library
    - Support files, fonts, scripts, etc.
    - Used by all users in sys
• ~/Library
    - Individual library for user
    - Similar info but specific to user
    - Hidden, users don't really need this data
• /System
    - OS files, similar to \Windows directory

- Apple ID
    • Associated w/ personal data & digital purchases
    • Managed Apple IDs
        - Business use
        - Integrate w/ Active directory
        - Connect to existing MDM (mobile dev manager)
- Backups
    • Time machine, hourly backups / daily / weekly
    • Deletes oldest info when disk full
- Anti-virus/malware
    • Not natively included, 3rd party only

- Updates
    • System settings -> general -> software updates
        - Not part of apple store
    • Auto updates
        - Individual control of
            • macOS, app update (Mac store), sec response & sys files
    • Beta updates
        - Not best practice
        - Could cause issues

- Rapid Security Response (RSR)
    • Auto update section
        - Security response toggle
    • Very important patches
        - Zero-day update & widespread sec issues
    • Available on iOS & iPadOS
    • Letter on update version denotes RSR.
        - macOS 13.3.1 (a)
        - 
###### **MacOS System Preferences     1.8**

- macOS "control panel"
    • Access to customize & config personalization/utilities

- Displays
    • Configure multiple displays, menu location &
    • Individual settings : resolution, brightness, colors, etc.

- Network
    • Configure Network interfaces ; similar to windows

- Printers & scanners
    • Add/remove, share, view status, config devices

- Privacy & sec
    • Limit app access to private data
        - location, photos, files, etc.
    • Asks for permissions when apps installed

- Accessibility
    • Modify for hearing, vision, etc & allows apps to system input & access to                                  scripting/automation
        - Keys, mouse, a/v

- Time machine
    • Add/remove storage drives or network drive
    • Auto backups hourly, daily, weekly
                (24)       (30)   (all months)
        - Deletes oldest data

###### **MacOS Features    1.8**

- Mission Control & spaces
    • View everything running (mission control)
        - Ctrl + Up arrow or trackpad 3 fingers up
    • Spaces
        - Multiple desktops, add inside mission control

- Keychain
    • Password management
        - Also stores notes, certificates, etc.
    • OS integrated
    • All info encrypted w/ login p/w

- Spotlight
    • Search OS to find apps, images, etc.
    • Command + Space or top right magnifying glass
    • Enable/disable in sys preferences -> spotlight

- iCloud
    • Integrates across all apple tech (macOS, iOS, iPadOS)
    • Shares calendars, email, pics, documents, etc.
    • Backup iOS process
        - & store files, app info, imessages/messages
    • Config sync options : sys preferences -> iCloud

- Trackpad
    • Gestures to customize how it operates w/ movements

- Finder
    • Central OS file manager
    • File management
        - Launch, delete, rename, etc.
    • Integrated across
        - File servers, remote storage, screen share

- Dock ; fast access to launch apps & view running apps
    • Keep folders in dock too

- Continuity ; integrates all iOS devices to work together
    • Software & hardware, synced through iCloud

- Disk Utility
    • Manages disks/images (resolve issues w/ as well)
    • File sys utilities (repair, modify partition, erase disk)
    • Create, convert, restore disk images (& manage)

- Full disk encryption (FDE) FileVault
    • Local key or iCloud authentication

- Terminal (command line)

- Force Quit ; stops app from running
    • Command + option + escape
    • Hold option + right click on app icon -> force quit

###### **Linux Overview      1.9**

- Free UNIX-like OS (Linux)
    • Unix compatible
    • Diff distros
        • Ubuntu, Debian, Red Hat / Fedora
    • Pros
        - Free, variety of hardware, big user community
    • Cons
        - limited driver support, support options

- Bootloader
    • Loads (boots) OS from storage dev
    • BIOS (basic in/out sys) knows which dev is used for booting
        - Configure in BIOS menu
        - BIOS -> Boot device -> bootloader

- UEFI boot loading
    • UEFI BIOS -> boot dev -> EFI bootloader
        - EFI sys partition has OS kernel to select OS to run
            • if you have multiple OS's

- Kernel
    • Core of OS                                      ____________
        - Sees & controls sys                       
    • Manages app execution
	    -Start sys processes, interact w/ devices, & end user   

												 |    Apps    |
                                                       ▲        ▲
                                         |           Kernel          |
                                         |___________________________|
                                           ▲              ▲       ▲
                                      _____|_____      ___|___ ___|___
                                     |   Memory  |    |  CPU  | Devices|
                                     |___________|    |_______|________|

• Kernel space
    - own area to operate in ; protected
    - Apps run in user space
• Kernel upgrades
    - bug fix, sec patch, added device support

- Systemd
    • System & service manager
    • background processes/services = daemons
        - systemd responsible for : start, stop, & manage of daemons
    • Logging, network, user session, login
    • Not 1 utility but a suite of software
    • kernel starts -> systemd
        - All daemons launched by systemd
    • Created to start & manage sys daemons
        - Common set of tools

- Root account
    • Root user similar to Windows "Administrator"
    • Full control of OS
        - User ID of 0, run any command, mod any file
        - Change rights & permissions

- Configuration Files
    • Linux can be used/managed at command line
        - GUI not required, most servers don't install GUI desktop
    • Applications and service parameters are configuration in text file

- User parameters (/etc/passwd)
    • stored in /etc/passwd (important data but not all)
    • list of registered users
        - Parsed w/ ":" (colon)
    • Config parameters saved:
        - Username, password, User ID (UID), Group ID (GID), UID info, home directory, command or shell
        - Password listed as x ; put in /etc/shadow file
            • Shadow is protected

- /etc/shadow
    • All acct p/w ; text file
    • Protected file storing p/w as hashed p/w
        - Need elevated rights & permissions to view
    • File format similar to /etc/passwd
        - U/N, p/w hash, date p/w last changed, min days,
          max days, warning days, inactive days, expiration date
    • Password hash can be
        - Reverse engineered or brute force
        - Which is why its protected

- /etc/hosts
    • Resolves FQDN to IP address
        - Fully qualified domain name (google to = 10.x.x.x)
        - Before DNS

- /etc/resolv.conf
    • List of DNS servers used on dev
    • To confirm DNS details
        - check /etc/resolv.conf

- /etc/fstab
    • Lists sys disks & partitions
        - Linux File System table (FS tab)
    • Sys startup references fstab to mount OS drives
        - Mount command reads /etc/fstab config file
        - Runs auto on startup
        - If file or directory missing check /etc/fstab

###### **Linux Commands Pt. I  1.9**

- Command line
    • Terminal, xTerm, mate, or similar
    • Commands are almost identical in Linux & macOS
        - macOS derived from Berkeley Soft distro (BSD) UNIX

- "man"
    • Command for help
    • Online manual ; to use
        - "> man grep" ; command for help on grep

- "ls"
    • List directory contents (Windows "dir" command)
    • May be color coded: blue=dir, red=archive, etc.
    • For long output: "ls -l | more"
        - use "q" of ctrl+c to exit
    • "ls -la" lists all info on files in directory
        - Lists permissions, rights, & ownership of files
        - "ls -la | more" space bar moves to next page ;
          not just list it all

- "pwd"
    • Print working directory ; displays current working dir path
    • Useful to know what dir you're in when running commands

- "mv"
    • You don't rename in Linux you move from 1name to another
        - "renames" files ; move
        - example: "mv first.txt second.txt"
                     ▲         ▲          ▲
                    move     source  destination

- "cd"
    • change dir, like windows
    • "cd" by itself goes back 1 dir/folder/step
    • "cd (destination)" to move to specific dir
    • "cd ~" to go to home dir

- "cp"
    • Copy a file or dir
    • ex. "cp test.txt test1.txt"
            ▲      ▲          ▲
          copy   source   destination

- "rm"
    • removes (deletes) files or directories
    • won't delete directories by default
        - directories must be empty or add "-r"
            • ex. "rm (dir) -r"

- "chmod"
    • change mode (& permissions) of a file sys object
        - r = read, w = write, x = execute
        - Set perms for file owner (u), group (g), all (a), or others (o)

- "chmod" cont.
    • after chmod : made #'s determine permissions
        - read = 4 , write = 2 , execute = 1 so 7 = r/w/x
        - if you only want to read (r) use 4 and add after that
    • "chmod 777 (file)"
        - would give full perms for everyone
    • to determine class of user look at :
        - | r w x | r w - | r - - | = "chmod 764 (file)"
            ▲       ▲       ▲
        file type  User   Group  others
        - 1st determines file, dir, etc. (- = file, d = dir)
        - 1st set of 3 after file type is user perms (owner)
        - 2nd set of 3 is group perms
        - 3rd set of 3 is others
    • another way to do above is :
        - "chmod a , +/- , r/w/x (file)"
                 ▲    ▲      ▲
             all users add or remove read, write, execute
        • first letter defines which target class (owner, group, etc)
        • +/- denotes to add or remove perm
        • r/w/x denotes which type of perm
        - "chmod a+x (file)"
            • would add execute perms for all users
        - u=user, g=group, a=all for target class

- "chown"
    • change file owner & group
        - format "chown (owner : group) (file)"
        - "sudo" for elevated rights

- "grep"
    • Find text in a file ; can search many files at once
    • format "grep (text to find) (file)"
        - ex. "grep failed auth.log"
        - lists every line w/ searched keyword
- "find"
    • Looks for a file by name or extension
        - Searches through any or all directories
    • Format "find (start_dir) (criteria) (action)"
        - ex. "find . -name "test.txt""
             1        2           3
         1.current dir  2.search by name  3.name to look up
                    (case sensitive)

- "fsck"
    • File system check, checks for logical errors
    • Looks for inconsistencies, "orphaned" files & repairs
    • Repair runs during startup
        - Checks as non-mounted, before OS mounts

- "mount"
    • Associates a storage dev w/ file system
    • Similar to Windows "net use"
    • View all mount points ; lists (dev) & (mount poin)
        • Common use : manually mount USB (if OS doesn't auto do it)

- "su" or "sudo"
    • Some commands need elevated rights
    • "sudo"
        - Execute as superuser or diff user ID (UID)
    • "su"
        - Become super user, continue as that user until "exit"

- "apt"
    • Advanced packaging tool
        - Management of app packages / utilities too
    • Install, update, remove
        - "sudo apt install wireshark"
        - "sudo apt update"

- "dnf"
    • Dandified YUM package manager (like apt)
    • Install, delete, update apps

    • replaces Yellowdog Updater, Modified (yum)
        - almost identical syntax/use
    • Manages RPM packages
        - Red Hat / RPM Package Manager


###### **Linux Commands Pt. II    1.9**

- "ip"
    • Manage network interfaces
        - Enable, disable, config addresses, manage routes, Arp cache, etc.
    • "ip address" to view interface address
    • "ip route" view IP routing table
    • To config IP on interface "ip address add x.x.x.x dev eth0"
        - ex. "sudo ip address add 192.168.1.249/24 dev eth0"

- "ping"
    • Continues until ctrl+c to end pings
        - "ping <(IP)x.x.x.x>"

- "curl"
    • Client url (a webpage)
    • Way to request & receive info from web server
        - Can access : webpages, FTP, emails, databases, etc.
    • Receive raw data, html & can : search, parse, automate
    • Ex. "curl ://professormesser.com"


- "dig"
    • Lookup info from DNS servers
        - Canonical names, IP addresses, cache timers, etc.
    • Same as "nslookup" on Windows
    • Domain Info Groper (DiG)
        - Detailed domain info
        - "dig ://profmesser.com" ; example

- "traceroute"
    • Find path a packet takes from source to destination
    • Same as "tracert" on Windows
        - Look at Windows "tracert" info ; same thing

- "cat"
    • Concatenate ; to link items together
    • Copy file/s to screen
        - "cat file.txt file2.txt"
    • Copy file/s to another file
        - "cat file.txt file2.txt > both.txt"

- "top"
    • View CPU, RAM, & resource utilization
    • The "task manager" for Linux
    • Summary of overall load ; 3 numbers
        - 1 min, 5 min, 15 min averages

- "ps"
    • View all current processes ; similar to task manager
        - & process ID (PID)
    • "ps" user processes
    • "ps -e" all processes
    • If looking for a specific process
        - "ps -e | grep cpu"

- "df" or "df -h"
    • Disk Free
        - Shows all file sys & space avail ("df -h") for bytes

- "du" or "du -h"
    • Disk usage ; scans current (pwd) directory & space used shows

- "nano"
    • A lot of configs in Linux stored in .txt files
    • Is a full screen text editor
        - Select, mark, copy/cut, & paste text
        - Similar to GUI editors
    • Must be in dir of file you want to open & edit or will create a new file.

###### **Installing Applications 1.10**

- Extend functionality of OS
    • Make sure app is compatible w/ OS & hardware requirements

- Apps must be same bit size as OS (32, x64) (generally)
    • Hardware drivers specific to OS version
    • x64 bit OS can run x32 (x86) bit apps

- Graphics req.
    • Integrated or dedicated (not on motherboard)

- RAM ; App has req but make sure you have more for OS
- CPU reg's for apps too (GHz)
- Physical hardware token for apps (iLOk)
- Disk storage req's
- Distro methods ; download, usb, cd's/dvds, etc.
    • Avoid 3rd parties ; avoid malicious code
- ISO files ; disk image containing all OS files
    • Has own file sys ; ISO 9660 file sys
    • Mount ISO appears as separate drive
- Image deployment
    • Copies 1 sys dev entire config
        - OS, apps, network config, etc.
    • Allows to install on multiple devices after faster w/ common setup
        - Hardware should be identical or very similar
	          - Or will cause problems

###### **Cloud Productivity Tools   1.11**

- Some don't have data centers anymore
    • Systems that are over cloud now
        - Email, storage, etc.
- Collab tools (work from anywhere)
    • Excel, video conference, im, etc.

- Identity sync
    • Used to have 1 single directory
    • Now cloud (multiple locations) everywhere
        - Microsoft entra
        - ID, Okta, etc.
    • Directory sync ID

- Licensing
    • Instead of local keys
    • Central management on cloud
        - Manage (add, change, remove) keys to users centrally

### **Section 2**
###### **Physical Security     2.1**

- Door access control (vestibule) / Door locks (multifactor)
    • Doors unlocked
        - Opening 1 door locks others
    • Doors locked
        - Opening 1 door prevents others being unlocked
    • 1 door open / other locked
    • Manage access & ID check to enter (Badge, Pin, Bio, etc.)

- Badge reader
    • RFID, NFC, mag swipe, etc.
    • Can also use to clock in/out, sec guard protocols, etc.

- Video
    • CCTV, flock cameras, etc.
        - Motion detection, passive infrared
    • Many cams for diff locations ; Network & record
        - 1 person monitoring

- Alarms
    • Normally open/closed circuit based
    • Motion detection, panic button

- Equipment locks
    • Rack locks to prevent theft
    • Need keys for access

- Security guards / access list
    • ID badge to verify person / access
    • Sec guard
        - Physical protection of area
        - Verify access / guest list
        - Maintain visitor log


###### **Physical Access Security     2.1**

- Keys ; physical ; ID to get key
- Key fob
    • RFID ; replaces physical key
- Smart card
    • Cert-based auth ; usually added sec factors (multifactor)
- Mobile digital keys
    • Use phone to unlock ; cars, doors, etc.
    • More auth factors on a phone
- Biometrics ; yourself becomes a key (Fingerprint, facial reg, retina, etc)
    • Retina scans capillaries in back of eye
    • Palm shape & size of hand / fingers
    • Facial recognition tech (FRT) ; uses laser dot projector
        • Creates a 3D facial map used as digital key
    • Voice recognition ; trained by speaking phrases
        • Questionable security
- Lighting ; helps w/ all other sec measures
- Magnetometer ; metal detector

###### **Logical Security      2.1**

- Rights & permissions
    • Least privilege
        - Rights & perms should be set to bare min.
            • limits hackers/malware ability to take over
        - Only get exactly what's needed to complete objective
    • All user accounts must be limited
        - Apps should run w/ min. privileges
        - Don't allow users to run w/ admin privileges
            • limits scope of malicious behavior

- Zero Trust
    • Many networks have all security on border & inside/middle
      of network susceptible to attacks
    • 0-trust means NO device is trusted in/out of network
        - "holistic" approach
        - Everything must be verified/auth
            • Multifactor auth, data encryption, system permissions, added firewalls inside of       network, monitor & analytics, etc.

- Access control list (ACL)
    • Allow/deny traffic on a point of network
        - Also used for NAT, QoS, etc.
    • Commonly used for ingress/egress of router interface
        - Can apply almost anywhere on network

    • ACLs commonly evaluate traffic on:
        - Source/destination
            • IP's, TCP/UDP port #'s, ICMP, & combos.
    • Deny or Permit
        - What happens when traffic matches ACL criteria?
    • Also used in OS
        - Rights & perms to file sys

- Multifactor auth
    • Prove ID
        - Apps, p/w, GPS
    • Factors are:
        - Something you know, have, are, or somewhere you are.

- Email auth
    • Associate a person w/ email ; registration
        - Confirmation emails
    • Use instead of p/w
    • Useful for p/w reset, validation code for p/w reset

- Auth apps
    • App that provides auth token
        - Pseudo-random token generator
    • Or physical hardware token generator

- SMS
    • Text message w/ code for auth
    • Sec issues
        - Phone spoofing, sms message intercept

- Voice call
    • Call provides auth token
    • Call can be intercepted, phone spoofing, forwarded

- Apps token
    • TOTP, Time based one time Password algo
        - Code changes every 30 secs, secret key token
    • Very popular, synced to time of day w/ NTP

- OTP, one time p/w
    • 1 time use, Never again
    • Key token based on secret key & counter
    • Hash token is diff every time
    • Hardware & software available

###### **Authentication & Access      2.1**

- Security Assertion Markup Language (SAML)
    • 1 common method of app authentication
    • Open standard for auth & authorization
        - Authentication through a 3rd party to gain access
        - Well for web based auth
            • Not designed to use w/ mobile apps
    • SAML Auth Flow

      Resource             Client              Authorization
       Server             Browser                 Server
       | 💻 |               | 💻 |                 | 🔑 |
       [___]                [___]                   [___]

        ① <-User access app URL |
        ② ->Send signed/encrypted SAML Request|
        Redirects to Auth server |
                            ③ -----------------> User logs in |
                            ④  <-- Auth success, SAML token generated| 
        ⑤ <-User presents SAML token |
        ⑥ ->SAML token verified, access given|

- SSO, Single sign on
    • Often integrated w/ SAML
    • Provide credentials 1 time within time limit
        - Usually 24 hrs before auth again
        - No need to login after sso login, until time expires (out)
    • Underlying auth infrastructure must support SSO

- Just in time access
    • Usually IT personnel has admin/root acct privileges
        - Makes IT admin acct a target
        - IT person w/ admin rights to acct just had to login
    • Instead of above, Just in time access an acct get elevated admin privilege for limited time
        - No permanent admin rights, principle of least privilege
        - Breached user acct doesn't have elevated rights
            • Narrows scope of a breach
    • User request access from central clearinghouse
        - Allow/deny based on predefined sec policies
    • Admin password stored in p/w vault
        - Primary credentials stored in p/w vault
        - Vault controls who gets access to credentials
    ★ • Instead of granting access to user acct:
        - Just in time process creates a time limited acct
        - Admin receives temporary credentials
        - Primary password never released
        - Credentials used for 1 session then deleted

- Privileged access management (PAM)
    • Process of managing superuser account/s access (Admin/ROOT)
        - Just in time is part of PAM

    • Privileged accts stored in a digital vault
        - access granted from vault by request
        - privileges are temporary
    • PAM pros
        - Centralized password management
        - Enables automation
        - Manages access for each user
        - Extensive tracking & auditing

- Data loss prevention (DLP)
    • Policy to manage sensitive info (transfer, storage, etc)
        - SSN #, C.C #, Medical records, etc.
    • Used to stop data "leaks"
        - Multiple types of DLP
            • Endpoint clients
            • DLP in cloud based sys (email, storage, etc)
            • DLP in firewall

- Identity & Access management (IAM)
    • Give right perms to right users @ right time
        - Apps & data located and avail anywhere
        - Many diff users; give right perms. prevent otherwise
    • ID lifecycle management
        - Every entity gets a digital identity (human, device)
    • Access control; entity gets access on what they need
    • Auth & authorization; entity must prove who they claim to be
    • ID governance; track entity resource access & auditing

- Directory services
    • Database of every entity on network
        - Comps, user accts, file shares, printers, groups, etc.
    • Primarily Windows based (Active Directory) (AD)
    • Manage auth
        - User login w/ AD creds
    • Central access control
        - Determine users access to resources
    • Commonly used by help desk
        - Reset passwords, add/remove accts


###### **Defender Anti-Virus    2.2**

- Microsoft defender built into OS
    • Anti-virus/malware, operates in real-time
    • Included in Windows sec app, may be listed under slightly diff name
        - No 3rd party required
        - Virus & threat protection (in security app, under settings)

- Activate or disable (Defender)
    • Disable for temp troubleshooting
        - Increases risk
        - Win sec app -> virus & threat protect -> Manage settings -> Real time protection

- Updated definitions
    • Signatures that ID malicious virus/malware
    • staying up to date is important
    • To update
        - Virus & threat protection -> virus & threat protect updates
          -> click protection updates -> check for updates
        - Auto process always on ; can change

###### **Windows Firewall    2.2**

- Enable/disable firewall
    • Firewall should always be enabled
        - Turn off to troubleshoot
    • Enable/disable through Control panel -> Firewall -> Turn on/off
      - or Windows security -> Firewall & network -> click on Network
        • Requires admin perms.

- Firewall config
    • To block all incoming connections
        - Within firewall profile under "Incoming connections" ->
          -> Click "Block all incoming connections, including allowed list"
    • Useful for added security
        - Unknown network, public wireless connection, etc.

- added firewall setting
    • Notifications from firewall / Network protections
        - Toggle on/off by firewall profile
    • Win security -> Firewall & network protection ->
      -> Firewall notification settings -> Manage notifications
    • Security providers
        - Found under : "Firewall notification settings" -> under
          "Security providers" -> manage providers
        - Shows antivirus, firewall, web protection

###### **Windows Security Settings      2.2**

- Windows authentication
    • To login to Windows desktop & access Network resources
    • User Local account
        - Associated only on a local windows device
    • Microsoft acct
        - Sync settings between devices, integrated apps, OneDrive, & more
    • Windows Domain accounts
        - Centrally managed accts from Active Directory

- Users & groups
    • Default user accts
        - Admin (superuser), Guest (limited access), standard users
    • Default groups
        - Admin, Guests, Power users, much more
            • Power users: almost same control as regular user but included for backward compatibility

- Login options
    • Username & password
        - PIN, Biometrics, SSO, other p/w options
            • SSO are Windows Domain credentials, sign in once every time out limit. (usually 24 hrs)

- Sign in password options
    • Facial recognition, Fingerprint recognition, PIN, security key, password, picture password

- Share vs. NTFS permissions
    • 2 ways to provide access to files/folders on local comp
    • NTFS is access to rights & permissions to groups/users
        - Folder properties -> security tab
        - NTFS access to file system
    • Share is access to files/folders over Network connections
        - Called a "Windows / network share"
        - Different set of rights & perms for share than NTFS
    • Since NTFS & share perms have 2 diff set of policies most restrictive setting WINS
    • NTFS permissions inherited from parent directory
        - All files/folders in directory/folder
        - Only time it changes is if you move from original parent directories to a new one, file/folder keeps original permissions

- Explicit & inherited permissions
    • Explicit permissions
        - When you config perms for a folder
    • Inherited perms
        - Any dir/folder within a parent folder receives perms from parent dir

    • Explicit perms take precedence over inherited perms

- User account control (UAC)
    • Limits software access to protect comp
    • Standard users
        - Don't need elevated rights
    • Admin
        - Install apps, config remote desktop
    • Change levels of prompt notifications
        - Prompt box asking "Do you want to allow app to make
          changes to your device?"

- BitLocker (FDE)
    • Encrypt entire volume
        - Protects all data, including OS
        - Not avail in home edition
    • Even if drive is physically moved to another comp still
      encrypted
    • "BitLocker to go" for USB drive encryption

- EFS, Encrypting file sys
    • Encrypt at file sys level, NTFS required
    • Folder properties -> General -> under "Attributes" -> advanced-> Encrypt options
    • U/N & P/W to encrypt key
        - Admin reset of p/w you lose encrypt access, backup!

###### **Active Directory       2.2**

- Database of every entity on the network
    • Comps, user accts, groups, file shares, printers, etc.

- Manage authorization
    • Users login w/ AD credentials

- Central access control
    • User acct control
    • Used by help desk
        - P/W reset, add/remove accts, etc.

- Domain
    • Name of Domain is core of AD
        - Related group of users, comps, resources, etc.
        - Each domain has a name, ex "Microsoft" domain
    • Domain controllers (server) store central domain database
        - AD is service that manages directory
        - AD has distributed databases so any change on 1 directory controller is copied to all other directory controllers
    • AD console open to troubleshoot
        - Is comp on domain?
        - Can you reset domain p/w?

- Joining the domain
    • Manage devices/users
        - Must be added to AD domain
    • Add devices from System properties or settings ->System or (about) command line scripting
        - Comp name, add domain info, part of domain!
        - Needs domain admin u/n & p/w to join

- Organizational Units (OU)
    • Keeps very large AD databases organized
        - Users, computers
    • Create your own hierarchy
        - Separate (OU) by countries, state, buildings, departments, etc.
    • Applying policies to a (OU)
        - Very important to organize (OU) to apply policies
        - Can be applied large scale
            • Domain users
            • Specific groups:
                - Marketing (department), N.America (location), etc.

- Move device/users within Organizational Unit's
    • Use AD users & computers (ADUC) tool
    • Right click object to be moved -> click move -> move to target OU -> ok

- Applying group Policy
    • Group policy management editor
        - Manage comps/users w/ group policies
        - Local & domain policies
    • Central console for:
        - Login scripts, Network config (QoS), security parameters
    • Force update a client
        - Client gets updated policy when restart
        - To force an update use "gpupdate" utility:
            • "gpupdate /force"
        - Then log off / restart for change to take effect

- Login Script assignment
    • Automate a series of tasks during login
        - Assign to user, group, or OU
    • Create login scripts for diff OU's
        - Customize script based on needs
    • Associate script w/ a group policy
        - In group policy editor -> user config -> Policies -> Windows settings -> scripts

- Assigning home folders
    • Assign a user a home folder to a network folder
        - Avoids storing files locally
        - Manage & backup files from the network
    • Directories auto created when added to user
        - Proper perms are assigned
    • AD users & comps -> users -> right click properties-> Profile (tab) -> Home folder section


- Configure folder redirection
    • Redirecting local user/apps from Windows library folders
      to a network share
        - Desktop, Downloads, music, docs, etc.
    • Create group policy to accomplish folder to network share
      redirect
        - User config -> Policies -> Windows settings -> Folder redirect
    • Paired w/ Windows offline files feature
        - When reconnected updates Network share

- Security groups
    • Create group & assign perms
        - After assigning rights & perms, add users
        - already some built in groups (users, guests, etc.)
    • Saves time by adding user to sec policy group, instead of individual
        - avoids mistakes too!

###### **Wireless Encryption    2.3**

- Securing wireless networks
    • Authenticate users to grant access
        - Username, password, Multi factor authentication
    • Encrypt wireless data
        - In case someone is "listening" to network
            • Can see network traffic
    • Verify integrity of comms
        - Receive (rx) data same as transmit (tx) data (original)
        - Method: Message Integrity check (MIC)

- Wireless encryption
    • All wireless comps are radio tx & rx
        - Anyone can listen in
        - So: Encrypt data
            • Associated encryption key
    • Only right key can tx & listen
        - WPA2 / WPA3

- WPA (Wi-Fi Protected Access)
    • 2002 WPA replaces WEP (Wired equivalent Privacy)
        - WEP had serious cryptographic weaknesses, Don't use!
    • WPA was short term stopgap
        - TKIP encryption method
        - Allowed use of existing hardware

- WPA2 (Wifi protected access II)
    • Cert began in 2004, replaced WPA
    • Used AES for encryption
        - Advanced encryption standard (AES)
        - Stronger than TKIP
        - AES needs more CPU, new hardware needed

- WPA3
    • Certification began in 2018
    • Upgrades on WPA2
        - Stronger AES cryptographic strength options
        - Increased security for initial key exchange
    • Provides encryption on open networks
        - Any traffic over air is still encrypted

- Wireless security modes
    • Configurate authentication on wireless router or access point
        - Open system when no password is required
    • WPA 2/3 - Personal // WPA 2/3 - PSK
        - PSK = pre-shared key = password
            • Everyone uses same 256-bit key
    • WPA 2/3 - Enterprise // WPA 2/3 - 802.1X
        - Authenticate users individually with authentication server (e.g. RADIUS)
            • If someone leaves job, disable acct & no more access.

###### **Authentication Methods  2.3**

- Auth process
    • Remote client process

          ① 💻login request                              ④ creds allow/access
            [ client ] -------> [ Firewall/VPN concentrator ] -------> [ 💻nternal                                                                        file server ]
                                 |              ▲
                  ② Auth user?     |              |  ③ creds allow/deny
                                 ▼              |
                             [      Auth server 💻    ]

- Radius (Remote Auth Dial-In User Service)
    • Common AAA protocol
        - AAA server = Authentication, Authorization, & Accounting
    • Used on any standard network, not just dial in
    • Radius server stores auth creds for users (commonly)
        - Central auth for:
            • Routers, switches, firewalls, server auth, Remote VPN access,
              802.1X network access.
        • Radius services avail on almost any server OS

- TACACS (Terminal Access Controller Access Control Sys)
    • Early form of remote auth protocol
    • Created access control to ARPANET dial up lines
    • TACACS+ (latest version)
        - Added auth capabilities & more auth requests/response codes
        - Released as open standard in 1993
        - Many associate this protocol w/ Cisco (widely used)

- kerberos
    • Network auth protocol
        - widely used w/ Windows Domain
    • Auth once, trusted by system
        - No need to re-auth for diff resources
        - Mutual auth: client -> server, server -> client
            • added protection against onpath/relay attacks
    • Standard since 1980s (dev in MIT)
    • Microsoft started using Kerberos in Windows 2000
        - based on kerberos 5.0 open standard
        - compatible with other OS's & devices

- SSO w/ kerberos
    • Auth 1 time (no constant u/n, p/w input)
        - Cryptographic tickets
    • Only works w/ Kerberos
        - Windows mainly, not everything is kerberos friendly
    • Many SSO methods (SAML, smart-cards, etc)
    • Process: see pg.85 of notes for graphic or online

- Which method/protocol to use?
    • Many auth protocols
        - Tech being used decide which protocols should be used
            • ex. VPN concentrator can talk to Radius server
                - we have a RADIUS server
            • TACACS+
                - Probably Cisco
            • Kerberos
                - Probably Microsoft network

- Multifactor auth
    • Something you are, have, know or
    • Somewhere you are or
    • Something you do
    • Can be expensive
        - Separate hardware tokens, specialized scanning equip


###### **Malware   2.4**

- Malicious software
    • Broad term for many types of bad software
    • Gather info (keystrokes)
    • Participate in a group (controlled by net)
    • Show advertising (make money)
    • Virus/worms
        - Attack sys/data, encrypt your data

- How you get malware
    • Start with a known/unknown vulnerability
        - Malware then embeds into sys to install diff malware
          which includes remote backdoor access
        - Bot may be installed later or attacker can install
          software, delete files, or modify info on comp
    • To get malware comp must run a program
        - Email link, web page pop-up, drive-by download,
        - Worms find itself to comp w/o human interaction (rare)
    • Update system & apps!
        - Avoid vulnerabilities

• Trojan Horse
       - Software that acts to be something else
       - Really malicious software
       - Antivirus can catch trojan horse
           • Since your are installing it bypasses antivirus
               - & has same access & privileges as user acct that installed
       - Once inside free reign

- Rootkits
    • Attackers want to be invisible / avoid antivirus
    • Root = Superuser (UNIX) / (Linux)
    • Modifies core system files, hiding from anti-virus/malware
        - Part of OS kernel
    • Can be invisible to OS, task manager
    • UEFI BIOS secure boot wont boot if OS is modified

- Finding & removing rootkits
    • Many anti-virus/malware have rootkit scanning
    • Rootkit remover
        - Every rootkit is different + need a remover specific to rootkit
    • Secure Boot with UEFI BIOS limits scope of rootkits

- Virus
    • Malware that can reproduce itself
        - Needs you to execute program
    • Propagates itself through file sys or network.
        - Running a program can spread virus
    • May or may not cause issues
        - Some are invisible, some not (obvious)
    • Anti-virus signature file update
        - Thousands of new viruses every week.

- Spyware
    • Malware that spies on you
        - Ads, ID theft, documenting/reporting
    • Trojan horse that tricks you to installing
    • Embeds in browser
        - Monitors browsing habits, documents history, & reports to attacker

- Keylogger
    • Malware that logs all keystrokes
        - URL's, p/w, U/N, emails, etc.
    • Save all Keystrokes
        - Send to "bad guys"
    • Other data logging
        - Clipboard, screen, im, mouse, search queries
- Ransomware
    • Nasty malware that:
        - Encrypts data until you pay attacker
            • Once you pay you get encrypt key
        • OS runs but no data availability
- Boot sector virus
    • Most virus run after OS is mounted/loaded; like apps.
    • Some malware embeds on bootloader & runs when you start comp
        - UEFI BIOS secure boot checks bootloaders.
            • Any signature changes & secure boot WONT boot system
              preventing malware from running
- Cryptominers
    • Attackers want to use CPU to mine
        - Visit website & CPU utilization% goes up
        - Malware installed & always running

- Stalkerware
    • Software designed to surveil
        - Intentionally tracking another's activity
    • Many commercial products avail
        - Not an accident; someone you know
    • Broad sys access
        - location, screenshots, mic, camera, etc.
    • Used for gov spying
        - countries used to spy on other countries

- Fileless virus
    • Doesn't install in files sys
        - Stealth attack; avoids antivirus detection
    • Operates in memory (RAM)
        - Never installed; once done disappears
    • Starts w/ user clicking link, etc.
    • Process:
        Click link -> Exploits Java/Flash/Windows vulnerability ->
        -> Launch powershell & download payload to RAM ->
        -> Runs PS scripts & executables in RAM (damage files / exfiltrate data) ->
        -> Adds auto-start to Registry (to repeat process)

- Potentially Unwanted Program (PUP)
    • ID'd by antivirus/malware
        - often installed w/ other software
    • Usually adware to make money
    • Aggressive browser toolbar (hidden PUP)
    • Backup utility that displays ads
    • Browser engine hijacking (PUP)

###### **Anti-malware tools     2.4**

- Windows Recovery Environment
    • Command prompt that gives file sys access before OS loads
    • Complete control
        - Fix problems, remove malicious software
        - Use, copy, rename, or replace OS sys files/folders
        - Enable/Disable services or device startup
        - repair file sys boot sector or master boot record (MBR)
    • Hold shift key while clicking restart
    • WIN 10 settings -> update & sec -> Recovery -> Advanced startup
    • WIN 11 Sys -> Recovery -> Advanced startup -> Restart now

- Endpoint detection & response (EDR)
    • Detects malicious code w/o signatures
        - Behavioral analysis, does machine learning & process monitor
        - Stops any abnormal software from running
    • Root cause analysis
        - Determine origin
    • Respond to threat
        - Iso sys, quarantine threat, rollback to previous config
        - API driven; no need for user/tech intervention

- Managed detection & Response (MDR)
    • 3rd party Managed sec service provider (MSSP)
    • Manage entire process
        - Monitor all EDR endpoints & detect threats

• Respond to all issues
    - Contain malware, investigate incident
    - provide guidance to prevent future issues.
    - Supplement orgs sec team
- Extended Detection & Response (XDR)
    • Evolution of EDR
        - Attacks involve more than endpoint
        - XDR improves missed detections, false positive, & long investigation
    • Adds network based detection
    • Central database correlate all endpoint, network, & cloud data
        - Improve detection rate, simplify sec event investigation
- Email security gateway
    • Evaluates email inbound for sources/malware
    • If ok goes to user on internal mail server
    • Onsite or cloud based
    • Inbound email process:
        Internet ① -> Firewall ② -> Internal mail server
                ↑
                |                     ▼
            mail gateway (screened subnet)
- OS reinstall
    • Only way to guarantee malware removal
    • Restore from backup
    • Manual install
    • Image system
        - User data on network share, prebuilt image with applications

★ skipped notes for social engineering... watch! (2.5)

###### **Denial of Service (DoS)   2.5**

- Force a service to fail
    • Overload service
    • Take advantage of a design failure/vulnerability
        - Keep system patched!
    • Cause sys to be unavailable
        - Competitive advantage
    • Create a smokescreen for other exploits
        - Precursor to a DNS spoofing attack
    • Attack doesn't have to be complex
        - Turns off power

- "Friendly" DoS
    • Unintentional DoS
    • Network DoS
        - Layer 2 (physical) loop by connecting 2 switches w/ 2 separate cables
            • Happens if you aren't running spanning tree protocol (STP)

- Bandwidth DoS
    • Limited internet connection bandwidth if you download large gb files
        - Use up all bandwidth avail making connection slow/unusable to others

- Distributed Denial of Service (DDoS)
    • Multiple sys (army of comps) often worldwide to bring a service down
        - Use all bandwidth or resources causing traffic spike
    • "Botnets" thousands to millions of comps, usually infected w/ malware
        - Zeus malware infected 3.6 million PC's
        - Can be used for coordinated attacks
        - Attackers are "zombies"
            - Malware operating in background & user doesn't even know

- Mitigating DDoS attacks
    • Some DDoS can be determined by packet info
        - If packets are similar can be filtered at firewall
    • Some ISP's have anti-DDoS sys
        - Ask ISP to turn on DDoS Mitigation
            • Stops traffic from reaching LAN
    • 3rd party tech to stop DDoS
        - Cloudflare
            • Has reverse proxy capabilities or can turn on DDoS prevention stopping traffic from reaching local servers

###### **On path Attacks       2.5**

- Formerly known as man-in-the-middle
    • Attacker gets between 2 devices to see, manipulate, or monitor traffic
    • Traffic is redirected then passed to destination
        - You never know traffic was redirected
    • ARP poisoning (spoofing)
        - On path attack on local IP subnet
        - ARP has no security in address resolution protocol (ARP)
        - Attacker sits in middle of traffic flow & sees all data.
- ARP spoofing
    • Attacker sends arp reply (unsolicited) to both client & router
    • Client & router update local ARP cache w/ attackers MAC
    • Attacker then IP forwards traffic & sits in middle of traffic path

- On path browser attack (man in the browser)
    • Malware/Trojan hooks into browsers API
    • Browser traffic is redirected before encryption
    • Malware in browser just waits until it gets wanted info
        - Controlled by attacker

- Wireless evil twin
    • Usually used on open WLANs
    • Separate access point w/ same (or similar) SSID, sec settings, &
      auth portal
    • Boost signal strength or place ap on edge of existing network
    • Always use HTTPS & a VPN to encrypt traffic

###### **Zero-day attacks      2.5**

- Vulnerabilities that are not yet known (apps, OS, etc)
    • Pentesters look for these to share w/ developers
        - Attackers keep this info to themselves
    • Zero-day
        - Brand new vulnerability w/ no mitigation or limited mitigation
            • Attackers create exploits before patches
        - Common vulnerabilities & exposure (CVE) database
          to track zero-day exploits
            • https://mitre.org
    • Usually affect small # of os's or apps
        - Log4j remote code execution affected millions
          of servers. (Java based logging utility as a Apache server)
            • Exploit discovered 12/9/2021
            • Vulnerability introduced on 9/14/2013
            • Patch released 12/14/2021
            • 2 added bugs fixed 12/17/2021

###### **Password attacks      2.5**

- Unencrypted p/w
    • Some apps store in the clear
        - No hashing
    • Don't store plaintext
    • If app stores unencrypted password, dont use app or modify

- Password hashing
    • Represents data as a fixed length string of text
        - Referred to as "a message digest," or "fingerprint"
    • Different inputs wont have same hash
    • 1 way hash (not same as encryption)
        - Impossible to recover original p/w from "digest"
    • 1 type of hashing protocol SHA-256 hash

- Password file
    • Different on OS's/applications
    • Diff hash algorithm 
    • ON LINUX /etc/shadow stores password's
    • If you know hash you can try to determine password

- Brute force
    • Try every possible password combo until hash is matched
    • Strong hash algo takes long time ; even w/o strong algo takes time
    • Offline vs. online attacks
        - Offline obtain user/hash file
            • Run through hash matches faster
            • Use scripts, cloud computation, multiple comps
        - Online is simply retrying login process
            • Slow & lockout after # of failed attempts

- Dictionary attacks
    • Paired w/ brute force
    • Find common words
    • Custom wordlist by language or line of work
    • Password cracker can sub letters for symbols/#'s
    • Takes time Distributed & GPU cracking is common

- Using p/w w/ #'s, symbols, etc jumbled up makes
  strong p/w against attacks

###### **Insider threats   2.5**

- Perimeter protection doesn't protect internal network.

- Inside worker may become attacker
    • Know systems, vulnerabilities
    • Being recruited to do so (paid for attacker middleman)
        - Ransomware attackers target employees
    • Maintain good sec fundamentals &
    • Always Backup!
###### **SQL Injection Attacks 2.5**

- Code Injection 
	-Adding your own info (code) into a data stream (into the code)
		-Adding code in authentication process to bypass login and get access
	-Happens due to bad programming
		-Application should handle input/output validation 
	-Different data types that can be injected:
			-HTML, SQL, XML, LDAP, etc.
			
- Structured Query Language (SQL)
	-Most common relational database management system language 
	-SQL Injection
		-Modify SQL queries (requests)
		-App shouldn't allow this 
		-Bypasses authentication/security measures and gives full access to all data
	-If you can manipulate database, you control application
		-Significant vulnerability

- Building a SQL injection
	-SQL query form:
		-"SELECT * FROM users WHERE name = ' "username" ' ";    * = everything
	-Actually query:
		-"SELECT * FROM user WHERE name = ' Professor' ";
	-Injected SQL query:
		-"SELECT * FROM users WHERE name = 'Professor' OR '1' = '1' ";
		-that injected code bypasses auth methods 
	-Bypassing auth methods allows attacker to:
		-View database info, delete database info, add users, denial of service, etc. 

###### **Cross-site Scripting (XSS) 2.5**

- XSS
	-Not CSS because that abbreviation is already in use; cascading style sheets (CSS)
- Originally named this due to browser security flaws
	-One site could share information with another site within the same browser 
	-Browsers now prevent information passing between websites
		-Instead now we can inject scripts to achieve this 
	-Very common web application development error
		-Take advantage of the trust a user has for a website to gain access
			-example: logins
- Malware that uses Javascript 
	-Javascript is so common and widespread that most use it
	
- XSS Process:
	-1. Attacker sends a link w/ malicious script to victim
	-2. Victim clicks link and visits legitimate site
	-3. Legit site loads in victims browser & malicious script is executed
	-4. Malicious script sends victim's data to attacker (session cookie, login info, etc)
			-Giving attacker same access as victim to legit website
			-Data gets intercepted before its encrypted

- Persistent XSS attack (stored)
	-Script is always stored somewhere for people to access 
		-Stored on a public webpage and anyone visiting webpage run script
		-No specific target 
			-Those who visit webpage run scripted attack
		-If posted on social media
			-Anyone who visits that post runs script
			-If reshared it continues to propagate 
- Example of XSS vulnerability:
	-Subaru website June 2017
	-Authenticating with Subaru, user gets token
		-Token never expired! (not best practice)
		-Valid token allowed any service request
			-Changing account information
			-Allowing full access to someone else's car
		-Web front-end included XSS vulnerability
			-Allowing an attacker to target customers and get their token 
- Preventing XSS 
	-Don't run script
		-Never click any unknown/untrusted email/website links
	-Disabling Javascript
		-Difficult since Java is so widespread that website won't operate as they should
		-Or control with an extension
	-Keep browser and applications updated
		-Avoids vulnerabilities 
	-Validate app input
		-Developers need to validate user input
			-This way users don't add their own scripts to an input field

###### **Business Email Compromise (BEC) 2.5**

- Email is popular attack vector
	-Popular form of business communication 
- Everyone in company has an email address
	-Not everyone is trained in IT security 
- Social Engineering component 
	-Difficult to ID and prevent 
	-Automated systems can't stop every instance of a social engineering attack
- Examples:
	-Title company sends you an email providing wire transfer account information
		-Not your actual title company; you send your money to an attacker instead of title company
	-Email from CEO asking you to buy a stack of gift cards for employee rewards
		-You email the gift card numbers along with secret codes to the attacker 
	-Attacker gets an employees internal email and spoofs an email to payroll department
		-They update employees banking information to attackers bank 
- How it works:
	-1. Identify target: 
		-Use social media, company records, etc to
	-2. Attacker uses email to talk with victim, to get them comfortable
		-Simple requests, small talk, projects in company, etc
	-3. Once victim is comfortable execute attack
		-Example: Provide payroll with the fake banking info
	-4. Attacker may double back to try and attack again
		-Since it worked once they will try to see if victim caught on
- Prevent BEC 
	-Watch for email spoofing
		-james@professormesser.com is not james@profesormesser.com
	-Spearfishing is a common method 
		-Directed phishing or BEC attacks towards a specific person or department
		-Give extra training to departments that could be vulnerable
	 -Part of larger breach
		 -Attacker compromises email from a vendor and you get emails form legitimate company address but it's really an attacker sending out the emails
	-Verify all requests!
		-Especially if there is a sense of urgency
		-Voice/video calls to verify requests
		-Train your company/community!

###### **Supply Chain Attacks 2.5**

- Chain containing many moving parts for products:
	-Raw materials, suppliers, manufacturers, distributers, customers/consumers
- Attackers try to infect any step in the supply chain line 
	-One exploit can have an effect in the entire supply chain
- Service providers 
	-You can't control providers security 
	-Usually have access to your network
		-Creating opportunities for attackers 
	 -Security audit of service providers should be done
		 -Security audits should be included in contracts
		 -Many type of service providers:
			 -Office cleaning, system admin, networking, cabling, etc
 - Example of supply chain attack:
	-Target breach November 2013
		-40 million credit cards stolen
	-HVAC firm in Pennsylvania was infected
		-Malware delivered in email
		-VPN credentials for HVAC techs was stolen
		-VPN had access to Target network
		-Attacker got access Vendor resources
	-Attacker gets to POS systems
		-Target network wasn't segmented
		-Attacker went from vendor resources to POS 
		-Infected POS systems and collected C.C info
		-Collected millions of cards before malware was discovered
- Hardware providers 
	-Can you trust new server/router/switch/firewall/software?
		-Cybersecurity supply chain
	-Use a small supplier base 
	-Added Security checks 
		-To ensure equipment is legitimate and from OEM
		-Part of normal security policy now 
	-Example:
		-July 2022 DHS arrests Cisco Reseller CEO
			-Sold over $1 billion of counterfeit Cisco products 
			-Created over 30 different companies
			-Selling since 2013
			-China knockoff sold as authentic Cisco
				-Started breaking & catching fire
				-No compromised software 
- Software Providers
	-Is software code legitimate?
	-Initial install
		-Digital signature should be confirmed during install
	-Updates & Patches
		-Software updates can be auto
		-How secure are the updates?
	-Open source is not immune
		-Attacker can inject malicious and have it compiled
		-Closed source software isn't the only type to be susceptible
	-Example:
		-SolarWinds Orion
			-March & June 2020 software updates were compromised
			-Existing install were infected and undetected until December 2020
			-Additional breach took advantage of exploit and infected 
				-Microsoft, Intel, Pentagon, Homeland Security, State Dept., etc. 

###### **Security Vulnerabilities 2.5** 

- In a company devices tend to have similar if not identical laptops/desktops
	-Makes it easier to 
		-Manage, update, secure
- Non-compliant systems 
	-Not part of Standard Operating Environment (SOE)
		- Set of tested and approved hardware/software systems
		- Often a standard operating system image 
		-Up to date and follows security protocols or organization
	-Staying in compliance
		-Operating System and application updates
			-Must have patches to remain in compliance
			-OS & anti-virus signatures up to date
			-All updates/patches must be checked & verified before install access is given
- Protection against non-compliant system
	-Active Directory infrastructure 
		-Set group policies 
			-Prevents non compliant OS features/apps
	-Monitor network traffic
		-Next-generation firewalls with application visibility
		-Set policies to allow/disallow access to individual apps
	-Periodic scans
		-For devices on network that shouldn't be there
		-Login systems can scan for non-compliance 
- Unpatched systems
	-Can contain known vulnerabilities that an attacker can take advantage of 
	-Microsoft Patch Tuesday
		-Second Tuesday of every month latest updates released (10:00 am PST)
		-Once released vulnerabilities are known to entire world
			-This causes security vulnerabilities
			-Race to test and deploy patch all OS and applications in network
				-Same time attackers writing exploits to deploy 
	-Patch management is crucial
		-Organization might have thousands of systems 
		-1 missed system and you have a weak link
			-Fence is as strong as its weakest link..
		-Need to have a system in place to rapidly
			-Test, prioritize, and deploy patches
- Unprotected systems
	-Security often seen as roadblocks
		-Applications/Hardware may not work properly with additional configurations in place 
		-Security isn't a roadblock but may cause additional troubleshooting
	-Troubleshooting tasks can leave network exposed
		-Disabling antivirus and try malfunctioning app/hardware
		-Disable firewall and try malfunctioning app/hardware
		-Make sure to re-enable all security tools 
	-Permanently disabling security isn't the answer
		-You don't fix a door lock by removing the door 
		-Become and expert in app troubleshooting
- Product support lifetime 
	-End of life (EOL) date for Operating System
		-Manufacturer stops selling OS
		-May or may not continue supporting OS
			-If they do support will get security patches/updates
	-End of Service life (EOSL)
		-Manufacturer stops selling OS
		-Support is no longer available
			-No ongoing security patches/updates
		-May offer premium cost support to large organizations
- BYOD
	-Bring your own device/technology
	-Employee owns device
		-Needs to meet company requirements
	-MDM incorporate to 
		-Protect corporate data
			-Partition phone and control from MDM


###### **Removing Malware 2.6**

- Just removing malware is NEVER best practice
	-It's impossible to know if all the malware is removed
- Delete everything and start over
	-Best practice
	-Restore from known good backup
	-Install from original media
	-This is why backing up is so important
- Reasons to remove malware instead of best practice
	-Important user documents that need to be recovered
	-Get system running enough to back up certain files
	-This is why backing up is so important!!
- ==Process to remove malware:==
	==-1. Investigate & verify malware symptoms==
		-Odd error messages 
			-Windows security, app error message, etc
		-App failures, security alerts
		-System performance issues
			-Slow boot, slow applications, etc
		-Investigate symptoms/malware
	==-2.Quarantine infected systems==
		-Disconnect/disable from network
			-Keep system contained/isolated
		-Isolate removable media
			-USBs, external hard-drives, etc, should not be connected anywhere else
		-Prevent spreading 
			-No backups!!! No file transfers
			-That ship has sailed; you will save malware at this point.
	==-3.Disable system restore==  
		-Malware infects system restore points  
		-May already be disabled in a corporate environment
			-Windows Home you need to disable
		-Disable system protection
			-Completely deletes previous system restore points
			-This will delete any malware saved in those restore points
	==-4.Remediate infected systems==
		-Provide a remedy to solve malware issue
		-Remove any malicious files
			-Could be easy; anti-virus might ID malware and remove them
		-Quarantined files
			-Identified in real time scan
				-Remove files into protected folder
				-Cannot access/execute in protected folder 
				-Malware may be difficult to remove
					-Embeds itself in many different points in OS 
					-Complicating removal
	==-5.Update anti-virus signatures/software==
		-Anti-virus software engine, what runs the program
		-Virus signatures, lists of known malware 
			-Changes constantly
		-Both are important to keep up to date 
		-Usually done automatically
			-Pointless to change to manual process
			-Many updates a day and will do it automatically. 
		-Malware may prevent update process
			-May need to manually download files on separate device and transfer into infected device and update manually
	==-6.Scan and removal techniques==
		-Safe mode
			-If malware is affecting boot process 
			-Loads bare minimum OS
			-Rarely prevents malware from running, but it can
		-Pre-installation Environment (WinPE)
			-If you can't boot into safe mode
			-Recovery console, bootable USB/CD/DVD
			-Can also build you own from Windows Assessment & Deployment Kit (ADK)
			-If WinPE can't find windows installation
				-May require repair or boot records & sectors 
	==-7. Reimage/Reinstall OS==
		-At this point you should be able to boot, gain file system access, & transfer any important files 
		-Then delete everything & reinstall
		-Reinstall from known good image 
			-Fast, includes all necessary software 
			-Drivers, files, apps, etc. 
		-This is why documents are saved to a network drive
			-Delete everything on local device
			-No important data is lost 
	==-8.Schedule scans & run updates==
		-Make sure anti-virus is running in real-time mode
		-Also schedule periodic scans to avoid missing any files 
		-Make sure you always up to date
			-If process isn't auto in anti-virus software
				-Use task scheduler to check for updates periodically
		-Check for OS updates auto config
	==-9.Enable System Restore==
		-Now that device is clean
		-Enable system protection/restore
		-Create a restore point immediately
	==-10.Educate end user==
		-1 to 1 training
		-Posters & signs in high visibility areas
		-Message board posting (physical/online)
		-Intranet posts/Login messages


###### **Security Best Practices 2.7**

- Data Encryption
	-Full-Disk Encryption (FDE)
		-Windows uses Bitlocker to achieve this 
		-Referred to as 'Data-at-rest'
	-File System Encryption
		-Single files/folders encrypted
		-Often built into file system
			-Look into file/folder properties to encrypt
	-Removable Media
		-Protect data in drives
	-Keys are used to encrypt
		-Key backups are critical!
		-Always need a copy of key
			-Encryption & Decryption keys
		-Key often built into OS and integrated in login process
			-Usually stored on local machine/Active Directory database
- Password complexity & length 
	-Make password strong 
		-Resists guessing & brute-force attacks
	-Increase password entropy
		-Different character types
		-Mix upper/lower case, numbers, & special characters
		-Don't use single words, words in dictionary, etc.
	-At least 8 characters 
- Password age/expiration
	-Best practice to change often
	-Age = how long since password was changed/modified
	-Expiration date
		-After date password doesn't work and must be changed
		-30/60/90 days
		-Systems usually remember password history
			-This way you can't cycle back to a previous password
			-Unique password required
		-Critical systems might change more frequently
			-7/15 days
- Password best practices
	-Change default username/passwords
		-All devices have defaults
		-Websites that document these logins
		-Anyone can use the defaults, very susceptible
	-BIOS/UEFI passwords
		-Supervisor/Admin password
			-Password to get into BIOS
			-Prevents unwanted BIOS changes
		-User password
			-Prevents booting 
	-Requiring Passwords
		-Always to prevent unwanted logins/changes
		-No blank passwords
		-No automated logins
- End-user best practices
	-Set a screensaver
		-Don't let your computer be accessible when away
	-Require a screensaver/lock screen password
		-Integrate with login credentials
		-Can be admin enforced/required
	-Should manually lock screen
		-Can also config auto lock for non-use/timeout
		-Screen timeout
	-Physical locks
		-Secure critical hardware
		-Laptops can easily be stolen
- Securing Personally Identifiable Infor (PII) & Passwords
	-PII: Name, Address, SSN, etc.
	-Control input
		-Be aware of your surroundings
		-Treat it like your debit card PIN number
		-Shield screen or use privacy filters 
			-Even those sitting next to you can't see display
	-Keep your monitor out of sight
		-Away from windows/hallways, others line of sight
	-In public
		-Be mindful of others line of sight
- Password managers
	-Use different password for different sites
		-Best practice
		-If attacker gets 1 password, can't get access to other sites
	-Use password manager/vault
		-Don't have to remember all your passwords
		-Encrypted/protected
		-Can include multifactor tokens
		- Can be built into OS or browsers
	-Enterprise password manager
		-Central management & recovery
		-Everyone in organization has safe/encrypted password storage	
	-Can also generate passwords
- Account management
	-User permissions
		-Don't want everyone to have Admin privileges
		-Assign proper rights and permissions
	-Assign rights based on groups
		-Easier to manage than per user rights
		-Rights and permissions to group
			-Assign user to group
			-User takes privileges of group
		-Easier to scale 
	-Login time restrictions
		-Login during working hours
		-Restricts after hour activities 
- Disable unnecessary accounts
	-All OS's include other accounts
		-Guest, root, mail, etc.
	-Not all accounts are necessary 
		-Disable/remove those accounts
	-Disable system accounts
		-No interactive logins
		-Not all accounts need to login
		-Stops brute force/guessing attacks too
	-Change default admin usernames/passwords
		-Helps with guessing/brute force attacks
- Lock the desktop
	-Failed passwords attempts
		-Lock account after failed password attempts
		-Prevents brute force online attacks
	-Automatically lock the system
		-After certain amount of time of inactivity
		-Or if you walk away (if possible)
	-Use expiration date for account
		-Account auto disables after time limit (ex. 30 days_)
		-For contractors and temp workers especially important
- Autorun & Autoplay
	-Autorun ran executable files (.exe)
	-Disable on older OSes 
		-autorun.inf in Vista
	-No autorun in Windows 7,8,8.1,10,11
		-Last was Win Vista  
	-Disable through registry 
	-Autoplay ran media automatically
		-Music, video, images, etc.
		-Disable in settings -->Bluetooth & devices --> Autoplay
- Disable unnecessary services
	-Unused or unknown services
	-Installed with OS or from other applications
	-Each service is potential breach
	-Disabling a service removes a potential threat 


###### **Mobile Device Security 2.8**

- Full Device Encryption
	-Encrypts all device data
	-Phone keeps key 
		-If you lose phone, data remains safe
	-iOS and later
		-Personal data encrypted with passcode
	-Android
		-Version 5.0 and later already encrypted 
		-Encrypted with passcode
- Screen lock
	-Restrict access to device
	-Facial Recognition
	-Password
	-PIN
	-Fingerprint reader
	-Swipe a pattern
	-Failed attempts
		-iOS: Erases data after 10 failed attempts
		-Android: Locks device & requires google login or wipe device
- Configuration profiles 
	-Mobile device management (MDM)
		-Centralized management of mobile device
	-Corporate config profiles speed up process
		-Predefined set of system configurations
		-Devices added to profile take on config
		-Controls 
			-Email, lock screen, data encryption configs, and more
		-Push to enrolled devices through MDM
- Creating a configuration profile
	-Microsoft Intune, Apple configurator
		-Frontend to building profile
	-Select wanted features & restrictions
	-Include security restrictions
		-Lock screens, passcode requirements, etc. 
	-Program creates a single profile created in XML
		-Profile then added & saved to an MDM
		-After adding profile pushed to devices 
- Patching/OS updates 
	-All devices need updates
	-Device patches
		-Including security updates 
	-OS updates
		-New features, bug fixes
	-Application updates 
	-Most updates are auto
		-Check in case to make sure you're not vulnerable!
- Anti-virus/malware
	-Apple iOS
		-Closed environment, Apple App Store 
		-Malware has to exploit an unpatched vulnerability (OS or app)
	-Android
		-Apps can be installed from anywhere
			-More open/vulnerable
	-3rd party virus/malware protection
	-Content filtering
		-Restrict website/app access
- Device locator applications & remote wipe
	-To view where device is
	-Built in GPS & other mobile networks
	-Find phone on a map
	-Control from a distance
		-Play sounds 
		-Display a message 
	-Remote wipe data
		-If you can't get phone back
- Remote Backup
	-Difficult to backup a device constantly moving
		-Backup to cloud instead
	-Constant backup, no manual process
	-Doesn't use wires
		-Uses existing networks
	-Restore with one click
		-Login & download
		-Restored!
- Firewalls
	-Mobile phone don't include a firewall
		-Most activities are outbound not inbound
	-Mobile firewall apps are available
		-Most are for Android, iOS not many 
		-Rarely used
	-Enterprise MDM control mobile apps
- Policies & Procedures
	-Companies manage company & user owned devices (BYOD)
		-Using an MDM
			-Set policies on apps, data, camera, mic, etc.
			-Control remote device
			-Entire device controlled or a partitioned portion
		-Bring your own device (BYOD) or COPE, CYOD
			-Choose your own device (CYOD)
			-Corporate owned personally enabled (COPE)


###### **Data Destruction 2.9**

- Valuable data that you don't want anyone else to get, ways to destroy
	-Physical destruction
		-Drill/Hammer
		-Get all the platters 
	-Shredder
		-Grinds hard drives into small pieces
	-Electromagnetic (degaussing)
		-Doesn't work on SSD or Flash drives
		-Removes magnetic field with a powerful magnet
		-Destroys data and renders drive unusable
	-Incineration
		-Fire
- Erasing data
	-Repurpose drive instead of destroying the drive 
		-Delete all previously stored data securely
	-File level overwriting
		-Sdelete; located on Windows Sysinternals
			-Securely deletes files where they can't be restored
		-Remaining files are still available
	-Whole drive wipe, secure data removal
		-DBAN tool; Darik's Boot and Nuke
		-Removes all data on drive
		-But you're still able to use drive again
		-Great for HDD but SSD can store data outside of file system scope
- Disk Formatting
	-Low level formatting
		-Preformatted at the manufacturer/factory
		-Not recommended and usually not available to user
	-Standard format/Quick format
		-Sets up file system (index), and installs a boot sector
		-Clears master file table (index) but not data 
		-With right software data can be recovered
	-Standard format/ Regular Format
		-Clears index and overwrites every disk sector with zeros
			-Time consuming
		-Default for Windows Vista and later
		-Data can't be recovered
- Drive destruction (physical)
	-Drive no longer usable, might seem like a waste
	-May be mandatory
		-Healthcare
		-Financial services
		-Research organizations
		-Any organization with privacy or confidentiality concerns
	-Check with local regulations & policies
- Certificate of destruction
	-When destruction is done by 3rd party
	-When confirmation is needed that data is destroyed
		-Service should include a certificate
	-Paper trail of destroyed data
- Hard drive security 
	-Bigger issue than you imagine
	-2019 Blancco & Ontrack study 
		-bought 159 drives form ebay
		-42% contained sensitive data


 ###### **Securing a SOHO Network 2.10**

- SOHO= Small Office Home Office
- Change default passwords
	-All access points (AP's) have default usernames/passwords
	-This is a security vulnerability
		-Can have full admin control
	-Default username & password very easy to find
		-www.routerpasswords.com
- IP address filtering
	-Content/Website filter, IP address ranges filter
		-Or a combo
	-Allow List
		-Nothing passes through unless you approve
		-Very restrictive
	-Deny list
		-Visit any site unless it's listed 
		-If it's listed, site is not allowed
		-Specific URLs, IP addresses, Domains
- Firmware updates
	-SOHO appliances (router, access point, switch, etc.)
		-OS (firmware) that has to be updated 
		-Firmware is proprietary, closed architecture
		-Updates come from manufacturer
	-Updates address different issues:
		-Bug fixes
		-New features
		-Security patches
	-Install latest software
		-Update/upgrade firmware
		-Firewalls, routers, switches, etc.
- Content filtering
	-Control traffic based on data within content
		-URL filters, website category filter
			-A gambling website vs. any gambling website
	-Corporate control of inbound/outbound data
		-Stop access to file sharing data sites, cloud services, etc.
	-Controls for inappropriate content
		-Not Safe For Work (NSFW)
		-Parental controls
	-Protection against virus/malware
		-You can visit site but scan all inbound data
- Physical placement
	-In SOHO environment often 1 device with multiple features
		-Router, switch, access point, firewall, modem, etc.
		-Combined into 1 device 
		-More for home setups
	-Location may be in a secured room
		-Prevent access to servers & network devices
		-More for a small office setup
	-Wi-Fi placement is important
		-Think about coverage (access)
		-To service device
- Universal Plug & Play (UPnP)
	-No IT tech or config needed
		-Software included to config, if you want 
	-Network devices auto configure & find other network devices
		-0 config
	-Applications on internal network open inbound ports using UPnP
		-App on computer talks to router and makes configs
		-No approval needed
		-Used for many peer-to-peer (P2P) apps
		-Best practice is to disable UPnP
			-Don't want an app to make changes on inbound rules
			-Only enable if application requires it
				-Even then try not to
- Screened subnet 
	-Previously known as DMZ 
	-Added layer of security between you and internet
		-After firewall public services (like a web server) are segmented on a screened subnet switch
	-Internal Network stays separate 
		![[Screenshot 2026-07-26 191654.png|377]]
 - Secure management access
	 -Access to SOHO router management needs to be tightly controlled
		 -Admin has complete control over network
	-Change default password
	-Use complex password
	-Additional authentication factor, if possible
	-Some devices have cloud login options
	-Limit management access by IP
		-Limit what IP's can connect to router
		-Disable remote access, local network only
		-Local logins only
- SSID management
	-Service Set Identifier (SSD)
		-Name of wireless network
	-Change SSID to something that isn't as obvious or related to organization
	-Disable SSID Broadcasting
		-Name of wifi (SSID) doesn't show up in a dropdown list of possible connections
		-Security through obscurity (not real security)
		-SSID easily determined through wireless network analysis
- Wireless channels & encryption
	-Open System
		-No authentication password required
	-WPA2/3-Personal/PSK
		-PSK=pre shared key
		-Everyone uses the same 256 bit key (password)
	-WPA2/3-Enterprise/802.1X
		-Authenticates user individually with an auth server (RADIUS, LDAP, etc.)
	-Open frequency
		-If a lot of access points (APs) in area will be difficult
			-Overlapping frequency (channels) cause interference
			-Some APs auto find good frequencies to use
- Disable Guest Networks
	-Guest networks are enabled by default
	-Limit access to outsiders
	-Guest networks can be used for other connections 
		-IoT
	-Don't enable without security
		-WPA2/3
- Disabling Ports
	-RJ45 jack that connects to switches in rackroom
	-Admin disable unused ports
		-More to maintain, but secure
		-Best practice
	- Network Access Control (NAC)
		- 802.1X controls
		- Can't communicate on network unless authenticated
		-Common for wireless but can be used with wired networks
- Port Forwarding
	-Devices on the internet to gain access to devices on inside of network 
		-24x7 access
		-Makes network less secure
			-Connection has to be secure
		-Usually for access to a web server, game server, security system, etc.
	-Information required to create a port forward
		-Private IP address to communicate internally
		-Public access port # 
		-Private port # to access server internally  
			-Public & Private port # are sometimes the same
	-Enterprise devices it's called:
		-Destination NAT or Static NAT
			-Destination address is translated from public IP to private IP
			-Doesn't expire or timeout
	![[Screenshot 2026-07-26 194818.png|334]]


###### **Browser Security 2.11**

- Browser download & Install
	-Only use trusted sources
	-Attackers release their own malware version
		-No fancy exploit required
	-Avoid untrusted 3rd party sites
		-Don't click links in email
		-Don't follow links to other sites
		-Visit browser site directly
	-Use hashes to verify the download 
		-Confirm the downloaded file matches the version on site server
- Hash verification
	-Install a hash checking application
		-Available for command line and GUI
	-Hash values may be available on the download site
		-Usually includes digital signature for verification
		-Will show hash algorithm type (SHA256, SHA 512, MD5)
	-Verify downloaded file 
		-Compare download file hash with:
		-App or command line hash output
		-If they are exactly the same original developer file
- Browser patching 
	-Stay up to date
		-Browser version
		-Security patches
	-Update manager
		-Most browsers have own update manager 
			-Upgrade may be done from browser itself
		-Often integrated with OS update manager
- Extension & plugins
	-Adds capabilities to browser
		-Same control as your browser
	-Trusted sources
		-Microsoft store, Chrome web store, etc.
		-Use known good or verified websites
	-Untrusted sources
		-3rd party website
			-Random or unfamiliar website
		-Install malware
		-Significant attack vector
			-Almost everything we do is in a browser
 - Malicious browser extensions
	 -Extension study by research group
		-March 2021 malware discovered
		-24+ chrome extensions
		-40 malicious domains
		-Not identified by anti-virus/malware before this research study
	 -Malicious activity
		-Credential theft
		-Screenshots & keylogging
		-Data exfiltration
	-Don't install untrustworthy software!
- Password managers
	-Password vaults
		-All passwords in one location
		-Database of creds that can also create strong passwords
	-Secure storage
		-Credentials encrypted
		-Cloud based sync
	-Create unique passwords
		-Passwords not the same across sites 
	-Corporate & personal options
- Secure connections
	-Security alerts & invalid certificated
		-When first visiting a site a message will pop up
	-Look at certificate details
		-Expired or wrong domain name
		-Certificate not properly signed
			-Untrustworthy certificate authority
		-Correct time & date is important
			-Make sure your computer has right time
	-www.badssl.com
		-examples of insecure connections
- Enable pop-up blocker
	-Blocker
		-Prevents unwanted notification windows
	-Enable or disable
		-Should be enabled
		-Disable to troubleshoot, only temporarily
	-Block & Allow
		-Set exemptions for popups
			-A website you trust
			-Block 3rd party sites
- Clearing private data
	-Clear browsing data
		-History
		-Saved passwords
		-List of downloaded files
	-Clear cache
		-Troubleshooting app or website issues
		-Parts of website stored locally
		-Remove all local data 
- Private browsing mode
	-Don't store information from browsing session
		-For privacy
		-Information removed when browser is closed
			-No history tracking
			-No download file list
			-Cached information deleted
	-Useful to troubleshoot 
		-Won't use stored cache for websites
		-Can verify if issue persists 
	-Great to use on others computers
		-Public computers (library)
		-Another persons computer
		-This way your information won't be saved to their browser
- Browser data sync
	-Share browsing data across multiple systems
		-Login in to browser
	-Login to different devices (laptop, tablet, etc.) and share:
		-Browsing history
		-Favorites
		-Installed extensions
		-Other settings
- Ad blockers
	-Browsers sometimes include ad blockers
		-Not great, doesn't block all ads
		-Control level of security
	-Site track visits
		-Recognize return visits
	-Extensions for ad blockers
		-Block more and trackers
		-Always use a trusted source
- Proxy
	-Sits between users and external network
	-Receives user requests and sends request on their behalf to internet
		-Checks for malicious data/software and prevents from getting on device
	-Added functions
		-Authentication
		-Access control
		-Local caching 
		-URL filtering
		-Content scanning
	-Explicit proxy
		-Have to configure proxy settings in browser 
	-Transparent proxy
		-Performs proxy functions
		-No additional configurations on local device
- Proxy configuration
	-Proxy settings in browser
		-Set up to automatically detect
		-Or manual config
		-Usually linked to OS settings
	-Explicit proxy
		-Only time config is really required
		-Config proxy IP & port number 
	-Transparent proxy
		-Invisible to user
		-Works without config
	-Troubleshooting
		-If on corporate network & no connection
			-Required proxy config
			-Proxy blocking access
- Secure DNS
	-DNS normally sends traffic in the clear
		-See every Fully Qualified Domain Name (FQDN) being visited 
		-Packet capture can see all this traffic
	-DNS over HTTPS (DoH)
		-How secure DNS sends information
		-Same HTTPS used for web servers
		-Perfect way to encrypt web traffic information
	-DNS server & DoH
		-DNS server must support DoH
		-Many large DNS providers support DoH
- Browser feature management
	-Enable/Disable
		-Plugins
		-Extensions
		-Features
	-Manual install
		-Official browser store
		-3rd party website

### **Section 3**
###### **Troubleshooting Windows 3.1**

- Blue screen of death (BSOD)
	-Startup/shutdown BSOD
		-Bad hardware, drivers, application
	-Use last known good configuration
		-Last known good option
		-System restore
		-Rollback driver
		-Try safe mode
	-Reseat/Remove hardware
		-If possible 
		-If hardware issue is suspected
	-Run hardware diagnostics
		-If you are unsure if hardware issue or software issue
		-Tests CPU, RAM, etc.
			-Helps rule out hardware issues
		-Provided by manufacturer (usually)
			-BIOS may have hardware diagnostics
- Degraded performance
	-Task manager 
		-Check for high CPU & I/O utilization
		-Performance tab for last 60secs utilization of device
	-Windows Update
		-Could be known bug
		-Check for latest patches/drivers
	-Disk space
		-OS need disk space
			-Check for available space
		-If using HDD
			-Defrag to help with issues
	-Power saving mode
		-Laptops throttle CPU in power saving mode
		-Connect to power source and monitor CPU usage
	-Virus/Malware
		-Could cause performance issues
		-Update anti-virus/malware
		-Scan for attackers
- Boot Issues
	-Can't find or Missing OS
		-Can't start OS if system can't find it
	-Boot loader replaced or changed
		-Dual boot systems
		-Multiple OSes installed
	-Check boot drives
		-If OS is missing 
		-Remove media (USB, external drive) 
		-Try again
	-Startup repair
		-Goes through common issues 
		-Tries to resolve them automatically
		-Missing NTLDR
			-Main Windows boot loader is missing
			-Run startup repair or replace manually & reboot
			-Disconnect removable media
		-Missing Operating System
			-Change Windows dir name or changed drive
			-Boot config data may be incorrect
			-Run startup repair or manually config BCD storage (below)
		-Auto boots to Safe Mode
			-Windows is not running normally
			-Run startup repair to find out why
	-Bootloader or location change of OS
		-Modify Windows Boot Configuration Database (BCD)
			-Formerly boot.ini
			-Recovery console: bootrec /rebuildbcd
				-Use command in recovery console
				-Scans all disks for Windows installs
				-Asks to add install to boot list 
- Starting the system
	-Hardware not starting
		-Check device manager & event viewer
		-Often a bad driver
		-Remove, replace, or rollback driver
	- One of more services failed to start
		- Background service doesn't start 
		- Bad/incorrect driver, bad hardware
		- Services app
			- Try starting service manually
		-Check account permissions
			-Sometimes an account doesn't have perms to run service
		-Confirm service dependencies
			-Order of services running
			-At times one service needs to run before another can start
		-Windows service
			-SFC; check system files 
				-confirm base OS is configured properly
		-Application service
			-Uninstall application
			-Reinstall with admin privileges
-  Applications crashing
	-Stops working
		-May provide error message
		-App may just disappear
	-Check Event viewer log
		-Shows log for everything
		-Filter to find info you need
	-Check Reliability Monitor
		-Tracks performance of applications
		-History of application problems
		-Check for resolutions
	-If you think its an application issue
		-Uninstall/Reinstall
		-Contact app support
- Low memory warning
	-Your computer is low on memory
		-Applications need RAM to run
	-Close large memory processes
		-Check task manager
	-Increase virtual memory
		-Take some info in RAM and send it to storage temporarily
			-When you need it again it will pull out of storage and send back to RAM
			-More room for swapping applications
		-Sys>About>Advanced sys settings>Performance>Settings>Virtual Memory
- USB controller resource warning
	-USB controllers contain buffers or 'endpoints'
	-USB devices use up those endpoints
		-The more complex the device the more endpoints used
		-If you have too many USB devices connected USB controller may not be able to support them
	-Move USB device to a different USB interface
		-USB 3.0 might support larger number of endpoints
		-Different controller than a USB 2.0 and might have more resources to use
	-Match USB interface type to device
		-USB 2.0 devices to 2.0 interface, etc.
- System Instability
	-General system failures
		-Software errors, system hangs, application failures
		-No error messages
	-Run full hardware diagnostic
		-Confirm all hardware operating as should
		-Most manufacturers have diagnostics
		-UEFI BIOS has hardware troubleshooting at times
		-Windows has memory diagnostic tools
			-Confirm RAM is working
		-Check OS
			-Run SFC (System File Checker)
			-Run anti-virus/malware
			-Confirm OS operating as it should
- Slow profile load
	-Using Windows at work
	-Roam profile from one computer to another
		-Desktop follows you to any computer
		-Configuration settings changed to device
	-Authentication taking a long time
		-Network latency to domain controller
			-Slow login script transfers
			- Slow to apply comp & user policies
			- Requires excessive LDAP queries
			- Remote site transfer to WAN and have congestion
		- Local domain controller not working properly
			- Device has to go outside domain controller for file transfer
		-IT can repair local domain controller
			-Device won't have to query remote domain controller 
- Time Drift
	-Computers internal clock drift over time
	-Solution is to fix the symptom
		-Fixing issue would require changing computer design
	-Automatic Time Setting
		-Periodically checks in with time server to make sure time is synced
		-Time zone may need to be configured if privacy settings are enabled
		-Settings>Time & language>Date & time

###### **Troubleshooting Mobile Devices 3.2**

- App issues
	-Fail to launch
	-Slow performance
	-Restart the phone
		-No command line 
	-Stop & Restart app
		-iPhone: Double tap home | slide app up
		-Android: Settings/Apps> Select app>Force stop
	-Update app
		-Latest version may fix a known bug
- App fails to close or crashes
	-App hangs
		-But other apps still working
	-App crashes
		-May show error message or just disappear
	-Restart device
		-May be OS related
	-Update app
		-Could be a bug
	-Delete app & reinstall app
- App fails to update
	-If app doesn't auto update
		-Go into app store and try to manually force an update 
		-Some stores require a valid payment method
	-Restart device 
		-Try update process again
- App fails to install
	-Bad internet connection
	-Limited storage space
		-Clear space if storage is limited
	-Valid payment method
	-MDM policy
		-If work phone policy might not allow app install
	-App store down
		-Rare but happens
- OS fails to update 
	-Updates include:
		-New features, bug fixes, security updates
	-Check available storage
		-If you don't have enough free space OS update won't download
		-Remove unused documents/apps
	-Check download bandwidth
		-Need high speed connection
		-Connect to wifi
	-Network filtering
		-A network might not allow you to connect to app store or updating OS
		-Connect to a different network, bypass filtering
	-Reboot
		-Always helps
- Battery life issues
	-Bad reception
		-Always searching for signal 
			-Turn on airplane mode, wont look for signal & not use battery
		-Aging battery
		-Disable unnecessary features
			-802.11 wireless, bluetooth, gps, etc.
		-Check application battery usage 
			-iOS/Android: Setings>Battery
- Random Reboots
	-Device reboots during normal operation
		-May occur randomly
	-Check OS & App versions
		-Update everything
	-Perform hardware health check
		-Check battery health
		-Not many diagnostic options
	-Contact OS tech support for options
		-Crash logs should be on device
		-Difficult to find logs help to find issues
- Connectivity issues
	-Intermittent connectivity
		-Mover closer to access point
		-Try a different AP
	-No WiFi connectivity
		-Check/enable WiFi connectivity
		-Check security key config
		-Hard reset can restart wireless connection
	-No bluetooth connectivity
		-Check/enable bluetooth connectivity
		-Check/pair bluetooth component
		-Restart bluetooth connectivity
	-NFC not working
		-Enable/disable NFC
		-Reset device
		-If payment related check card and remove/add card again
		-Limited troubleshooting options 
	-Airdrop not working
		-Distance has to be less than 30 feet
		-Turn on Wi-Fi & Bluetooth
		-Check Airdrop discovery options
			-Off/Contacts only/Everyone
- Screen does not auto rotate
	-Turning device doesn't rotate view
		-Landscape/Horizontal
		-Disable rotation lock
			-Prevents auto rotation when lock enabled
		-Restart app
			-App/device might not be working right
		-Restart device
			-Device might not be working right
		-Hardware issue
			-Accelerometer
		-Contact support
###### **Troubleshooting Mobile Device Security 3.3**

-Malware
	-Don't install Android Package Kit (APK) Files fomr untrusted sources
		-This is called sideloading
	-iOS all comes from apple app store
-Developer mode
	-Enables developer specific settings
		-USB debug
		-Memory statistics
		-Demo mode settings/ 
		-More details/logs
	-iOS/iPadOS
		-Xcode is developer mode
		-Must use macOS connected to device
	-Android 
		-Can config developer mode
			-Enable from settings>about phone>software info (on some phones)
			-Tap build number 7 times 
-Root access/jailbreaking
	-Mobile phone don't give direct access to OS
	-Getting access to OS
		-Android = Rooting
		-Apple iOS = Jailbreaking
	-Installing custom firmware
		-Replacing existing firmware, giving access to underlying OS
	-Uncontrolled access
		-Sideload apps without app store
		-Bypass security features
		-MDM becomes essentially useless
-Application spoofing
	-App store
		-Sometimes an app is actually malware
	-Google removed 150 apps from store in 2021
		-QR code scanners, camera filters, games, etc.
	-Attacker have tried to infect application used to build apps
		-Malicious version of Xcode: Xcode ghost malware
	-Always check download source:
		-Check legitimacy of app
		-Remember you are giving app permissions and control
-High network traffic
	-Higher than normal network use (app/service)
		-May indicate malware
		-Proxy use 
		-Command & control
	-Check built in data use reports
		-Or use built in 3rd party reporting app
	-Run malware scan
-Degraded performance/response time 
	-Running slow
		-Screen lags, poor input response time
	-Restart
		-Clear cache/slate
	-Check for OS/ap updates
		-Fixes to bugs in code
	-Close apps that aren't in use
		-Frees up memory
	-Factory reset 
		-If issue is constant and nothing else fixes it
		-If not a hardware problem
-Data usage limit notification
	-Built in Android feature
	-Not iOS native
	-Set a warning for limit & limit amount
		-Notification for traffic usage
	-Can indicate malware 
		-If network usage is more than what you use/expect
	-Run malware scan
-Limited or no connectivity
	-Malware does this to not be removed
		-Prevents access to network
	-Disable/enable WiFi
		-Or enable/disable airplane mode
	-Restart the device
		-Clear memory & reload drivers
	-Run malware scan
-High number of ads
	-Malware showing you ads
		-Revenue from each view/click
	-Ad blocker difficult
		-Apps that claim to block ads but do opposite
		-2019 Ads blocker for Android
			-Showed more ads
			-Once installed wasn't listed as available apps 
			-Fakeadsblock malware strain
	-Run anti-malware to verify app
-Fake security warnings
	-Get user to install malware themselves 
		-Easiest way to get malware on phone
		-Usually happens when surfing web
	-Warnings seem legit
		-Not actual security threats 
		-DON'T install
	-Malware can directly access user data
		-Steals credit card info, stored passwords, browsing history, texts, etc.
	-DON'T CLICK!
		-If you click run malware removal tool 
-Unexpected application behavior
	-App developers & device manufacturers are different
		-This may cause erratic behavior in apps
	-Apps close unexpectedly/long delays
	-App doesn't seem to have normal features
		-Or included features not working 
	-High battery usage
		-When app is running 
	-Update app
		-Latest version could have fixed know bugs
-Personal Data leaks
	-Most likely malware
	-Unauthorized account access
		-Unauthorized root access
		-Leaked personal files/data
	-Determine cause of data breach
		-Run app scan & anti-malware scan
	-Factory reset & clean install
	-Check online data sources
		-Change passwords
		-All logins for clouds & account
		-Add multifactor auth
###### **Troubleshooting Security Issues 3.4**

-Unable to access the network
	-Malware related
		-Slow performance, locks up
		-Malware isn't best written code
			-Likes to stop internet connection 
	-Internet connectivity issues
		-Malware likes to control everything, including internet connection
			-Stops you from downloading anti-malware
			-Or from updating anti-malware program
		-Can't protect yourself if you can't download 
	-OS updates failure
		-Malware uses vulnerabilities 
		-Malware wants to stop updates so vulnerabilities stay open
			-No bug fixes 
		-Restore/clean
			-Restore from a known good backup or malware remover
-Desktop alerts
	-Browser notifications push messages
		-Pretends to be anti-virus/malware
			-Actually malware trying to infect
		-Real notifications come from your anti-virus app
	-Disable browser notifications
		-Or create an allow list of legit sites
	-Scan for malware
		-If you suspect malware was installed
	-False anti-virus alerts
		-May include recognizable logos
		-Not legit virus, malware to achieve scam
			-Require money to unlock, clean, or sub to their service
		-Malware scan or restore from a known good backup
-Altered system/personal files 
	-Renamed sys files
	-Files disappeared
		-Or encrypted
	-File permission changes
	-Access denied to documents/sys files
		-Malware locks itself away 
		-Doesn't leave easy
	-Use malware removal or restore from known good point
-Unwanted OS notifications
	-Notifications can be useful but annoying 
	-Control notifications from OS settings
		-System>notifications
		-Global enable/disable
			-Effects all apps/system services
		-Or App by app basis
-OS update failures
	-OS auto updates
		-Unless there is an issue
	-Updates from cloud
		-Check network connectivity, firewalls/filtering, & bandwidth restrictions
	-Windows includes own update troubleshooter
		-Tries to resolve any issues it finds on its own
-Popup browser messages
	-Looks legit
		-May be malware
	-Update browser
		-Check popup block feature
	-Scan for malware
		-Or known good backup
-Certificate warnings
	-Security alerts/invalid certs
	-Look at certificate details
		-Click on lock icon
		-Domain name expired or wrong
		-Certificate may not be signed or from untrusted source
		-Date & time is important, make sure computers time is set correct
-Browser redirection
	-Instead of google your browser goes elsewhere
	-Usually malware 
		-Redirect where ads run or more malware runs
	-Clean by malware removal or delete/restore from known good backup
-Degraded browser performance
	-Complex issue, may be many things
	-Check for latest browser version
		-Check for how many tabs are open
	-Clear cache & cookies in browser
	-Check local device performance
		-Task manager for utilization metrics
		-CPU, RAM, network, etc.
	-Malware might cause issues
		-Crypto miner for example
	-Try a different browser and see if issues persist
### **Section 4**

###### **Ticketing Systems 4.1**

-Best way to manage support requests
	-Documents, assign, resolve, report
-Helpdesk responsibility of tickets
	-Take calls, emails, text, im
	-Triage
	-Determine best next step
	-Assign ticket and monitoring of ticket
	-Many diff ticket system
		-Very similar in function
-Managing a support ticket
	 -Information gathering
		 -User & device info
		 -Problem description
	-Context
		-Category of problem
			-Login issue, networking issue, etc.
		-Assign severity/importance
			-Many people having an outage vs. 1 person
			-Some issues more severe than others
		-Determine if escalation is required
	-Clear and concise communication
		-Problem description
		-Notes about progress 
		-Resolution details 
-User information
	-Assign ticket to correct user
		-Name of person (or group) with issue and name of person reporting issue
	-Usually integrated into a name service
		-Active Directory of similar
	-User can be added automatically
		-Email, phone number, etc. associated with user
	-Always confirm user & contact info
		-Database may not be up to date 
-Device & description
	-Device information
		-Laptop, printer, conference projector, etc.
	-Description 
		-Make description clear & concise
	-Next steps
		-Determined by description field
		-Callback for more info
		-Associate issue with a larger problem
		-Assign to another person/department
-Category & escalation
	-General description of issue
		-Change request, hardware request/failure, problem investigation, onboarding/offboarding (hr)
	-Severity
		-Established set of standard in organization
			-Depending on issue, department, etc.
		-Low, medium, high, critical 
	-Escalation level
		-Unique or difficult issues handled by specialist
		-Escalate ticket to new tier or specific group
-Resolving the issue
	-Progress notes
		-Multiple access and take action on a ticket
			-That's why progress notes are important
		-Keep notes concise but include all important details
		-Documents any changes or added information
	-Problem resolution
		-Document the solution when done fixing problem
		-May be referenced later by others with same problem
		-Knowledgebase of issues & resolutions
###### **Asset Management 4.1**

-Inventory (Configuration Management) Database
	-Record of every asset
		-Laptops, desktops, servers, routers, switches, cables, fiver modules, etc.
	-Support ticket association
		-Can include device make/model in support ticket
	-Financial records
		-Provides paperwork for audits & tax depreciation
		-Make/model, configuration, purchase date, location, etc.
	-Asset tag
		-Barcode, RFID, tracking number, organization name
		-Used to reference inventory
-Configuration Management Database (CMDB)
	-Central asset tracking system
		-Used across organization
	-Assigned users
		-Useful for tracking devices
		-And associating that device with a person
	-Warranty
		-To determine if in/out of warranty
			-Financial department
	-Licensing 
		-Software costs
		-Ongoing renewal dates
-Procurement life cycle
	-Purchasing process
		-Multistep process for requesting & obtaining goods, services, or devices
	-Starts with request form from user
		-Usually includes
			-Budgeting information
			-Formal approvals
	-Purchasing department
		-Receives requests from user
		-Negotiates with suppliers
			-Terms & conditions 
		  -Then purchase, invoice, & payment
###### **Document Types 4.1**

- Incident Reports
	-Security Policy to report incident
		-What led to incident
		-Incident itself
		-Reaction to incident
	-Documentation about incident
		-Actions prior/after
	-Incidents are ongoing
		-Organizations have formal incident plans
		-Creates reference for future incidents
- Standard Operating Procedures (SOP)
	-Organizations have varying business objectives
		-This documents established processes & procedures for organization
	-Operational procedures
		-Downtime notifications
			-Who do we contact to inform & fix
		-Facilities issues
			-Who to contact internally & externally to fix issues
		-Software install & upgrades
			-Custom install of software package
			-Testing & change control
		-Documentation is key
			-Anyone can review & understand policies
- Onboarding
	-Bring a new person into organization
		-New user checklist
	-IT agreements must be signed 
		-Employee handbook or acceptable use policy (AUP)
	-Create accounts
		-Associate user with proper groups/departments
	-Provide required IT hardware 
		-Laptop, desktop, tablet, etc.
		-Preconfigured & ready to use
- Offboarding
	-User termination checklist
	-Process should be predefined
		-What happens to hardware?
		-What happens to data?
	-Account information is usually deactivated
		-But not always deleted, if info is needed
- Service Level Agreement (SLA)
	-Minimum terms of services provided
		-Uptime, response time, etc. 
		-Commonly used between customers & service providers 
		-May also be used for internal customers
			-Minimum requirements for inter-department work
	-Contract with internet service provider (ISP)
		-Example: Downtime of no more than 4 hours 
			-If more than 4 hours credit given
		-Technician dispatch
		-Customer keep spare equipment onsite
		 -All above are just examples of what might be included in an SLA
- Knowledge base 
	-Articles on detailed technical information about support for 
		-Hardware, software, etc. 
	-External sources
		-Manufacturer knowledge base
		-Internet communities
	-Internal documentation
		-Organization knowledge
		-Usually part of helpdesk software
	-Find solution rapidly
		-Detailed information on issues & solution
		-Searchable archive
		-Auto searches with helpdesk ticket keywords
			-Can be incorporated into helpdesk software


###### **Change Management 4.2**

- How to manage a change
	-Software upgrades, application patches, firewall configuration changes, modify switch ports, etc.
	-Managing a change is often dismissed/overlooked
	-Changes can cause more issues to occur
		-Most common risk in enterprise
			-Happens often
- Have clear policies
	-Frequency, duration, install process, rollback procedures, etc.
    -If corporate doesn't have change management procedure
		-Hard to incorporate/change corporate culture
- Change management process
	-Formal process for managing change
		-Avoid downtime, confusion, & mistakes
		-Everybody needs to be made aware that could be affected by changes
	-No changes without process
		-Complete request forms
		-Purpose of change
		-Identify scope of change
			-Affected systems & impact
		-Schedule date & time of change 
		-Analyze risk associated with change 
		-Get approval from change control board 
		-Get end user approval of successful change
	-Rollback plan
		-In case something goes wrong
			-Plan to revert changes to original configuration
			-Sometimes difficult/impossible to revert
				-Ex. Firmware changes, would need to have equipment with old firmware on standby
		-Always have a backup
- Backup plan
	-In case original plan doesn't go as expected
	-Need a plan B, C, and D
		-Give yourself multiple options in case things go wrong 
- Sandbox testing
	-Isolated testing environment 
		-No connection to production environment
		-Tech safe space to make changes
	-Test before production change
		-Try upgrade/patch
		-Confirm working as intended before deployment
	-Confirm rollback plan
		-Deploy change
		-Pretend there is an issue
		-Revert back to original configuration
- Responsible staff members
	-Team effort to make changes
		-IT team
			-Implementing changes
		-Business customer
			-End user of technology/software
		-Organization sponsor
			-Either end user or 
			-Part of organization who is paying for change
				-Change could be intended for meeting rooms but:
				-Commission of changes was procured by finance dept AND:
				-IT department has to approve final changes
- Change request forms
	-Formal process
	-Ensures nothing is missed
		-Detailed reports & statistics
		-Easier to manage
	-Transparent process
		-To make everyone involved & in organization aware of changes
- Purpose of the change
	-Why?
		-Needs to be a good reason
		-Financial justify cost
	-App upgrades
		-New features, bug fixes, performance enhancements 
	-Security fixes
		-Monthly patches & vulnerability fixes 
- Scope of change
	-Determine effect of change
		-Single server almost nobody uses or
		-Entire site used by entire organization
	-Far reaching 
		-Single change can affect many people
			-Multiple apps, internet connectivity, remote site access, external customer access, etc.
	-Duration to implement change 
		-How long does it take?
		-Will it have impact?
			-Schedule during downtime
		-Set date/time for change
- Change types
	-Standard/low risk
		-Preapproved change
		-Happens often & is will documented
			-Replacing keyboard/mouse, monitor, etc.
	-Normal/ medium risk
		-Not urgent, follows full change management process
		-Update firewall rule
		-Replace a core switch on network
	-Emergency/high risk
		-Must be implemented rapidly
		-A patch for a public facing zero day vulnerability 
- Date/Time of change
	-Change management board will usually make decision
	-Maintenance windows
		-Best dates/times to implement change
	-On demand change
		-Not in maintenance window 
		-Date/time scheduled as needed
	-Regularly scheduled downtime
		-Always at a specific date/time 
	-Change freeze
		-No changes allowed
			-Usually a specific block of time
		-Unless emergency happens
- Affected systems & impact
	-Change may be more than a single service
		-Ex. Rebooting firewall brings down all internet traffic
	-Scope might be limited
		-Software only used by a few people
	-Unclear scope
		-Unknown number of applications on a server
			-Or who uses apps/server
	-Determine total number of services
		-Understand impact on systems
		-Change board can make best educated decision
- Risk Analysis
	-Determine risk level
		-low, medium, high
	-Possible risks
		-Fix doesn't actually fix issue
		-Fix breaks something else
		-Fix causes OS failures
		-Fix 'works' but data associated with app is corrupted
	-Risks for NOT making change
		-Security vulnerability
		-Application vulnerability
		-Unexpected downtime to other services
- Change control board & approvals
	-Determine if change is approved/denied
	-Every department is informed
		-They also discuss changes/impacts
	-Change priority
		-Board decides priority level
		-That priority level will decide how fast change is implemented
	-Change approval
		-Up to IT to implement change
- Implementation & peer review
	-After you build a plan
		-Get second opinion
		-Especially from a professional in that topic
	-Outside evaluation
		-Think of issues you might miss
		-Expert opinions save time & avoid problems
- End user acceptance
	-Need a sign off that change works
		-From end users of app/network
	-End user is involved in process from start to end
		-Still need to make sure implementation is successful from their perspective


###### **Managing Backups 4.3**

-Extremely important!
	-Recover important data
	-Plan for worst case scenario
-Many implementation methods/variables
	-Amount of data
	-Type of backup
	-Storage location
	-Backup/recovery software
	-Schedule of backups
-Full Backup
	-Backup everything to one set
		-All OS & user files
	-Usually longest process
	-Difficult to perform everyday
		-Long backup times
		-Lots of storage space
-Differential backup
	-1st day fullback up
	-Subsequent backups 
		-Contain only data that was changed since last full backup
		-Subsequent changes tend to get larger as days pass
	-Restoration requires:
		-1st full backup + last subsequent (differential) backup
-Incremental backup
	-1st day full backup taken
	-Subsequent backups 
		-Back up everything since last full backup & 
		-Since last incremental backup
		-Every backup since full backup are of different sizes
			-Depends on how much data has changed from one day to another
		-Restoration backup:
			-1st full back up + every incremental backup
-Synthetic Backup
	-Create a fullback up without actually performing a full backup
	-1st day full back up taken
		-Like all other backup plans
	-Subsequent incremental or differential backups are taken
	-Restoration or next full backup:
		-All previous backups concatenated together
		-Doesn't take another full backup + subsequent backups
	-Faster & use less bandwidth
		-Advantage of a full backup without the cons
		-Efficiency of incremental & differential backups 
-Backup Types
	-Full
		-All data
		-High backup time/low restore time (1 set)
	-Differential
		-All data modified since last full backup
		-Moderate backup time/moderate restore time (No more than 2 backup sets(full/differential))
	-Incremental
		-New files & files modified since last full or incremental back up
		-Low backup time/High restore time (multiple backup sets(full backup/all incremental backups))
	-Synthetic
		-All selected data
		-low back up time/low restore time (one backup set)
-Backup Testing
	-Not enough to just perform backup
	-Disaster recovery testing
		-Simulate situation
		-Restore from backup
	-Confirm restoration
		-Test restored app/data
	-Perform periodic audits
		-Changes to data/backup may occur
		-Always have good up to date backup
		-Weekly, monthly, quarterly checks
-Recovery/Restoration
	-Recovering/restoring from backup
		-Should have tested this process already
	-In place/overwrite
		-Replace files on the original system
			-Overwriting
		-Original files are not viable
		-Often used with reimaging
	-Alternative location
		-In place restore can overwrite data that was changed since last restore
		-Restore to a separate system or drive
			-Leave original system alone
		-Won't lose anything to in original system
-On site vs. Off site backups
	-On site
		-No internet link required
		-Backup systems & data in same facility
		-High bandwidth between backup systems & data
		-Data is available immediately
		-Generally less expensive than off site
	-Off site
		-Data and location are separate
		-Data transfer over internet or WAN link
		-Data is available in case of location disaster
			-Fire, flood, tornado, hurricane, etc.
		-Restoration can be performed from anywhre
	-Organizations often use both
		-More backups
		-More options when restoring
-Grandfather/father/son (GFS)
	-Layering of backups 
		-Grandfather backups
			-12 monthly full backups
			-Good choice for offsite storage
		-Father backups
			-Weekly backups 
			-4/5 backups in a month
		-Son backups
			-31 day or differential backups
	-Choose a rotating schedule
-3/2/1 Backup Rule
	-Popular & effective backup strategy
		-For business & home use
	-3 copies of data should always be available
		-1 primary
		-2 backups
		-Or any combo
	-2 different types of media
		-Local drive, tape backup, or network attached storage (NAS)
	-1 copy of backup should be offsite
		-Cloud 
		-Offsite storage


###### **Managing Electrostatic Discharge 4.4**

-Static Electricity
	-Electricity that doesn't move
	-'Looks' for a conductor to discharge & equalize electrical potential
-Harm to computers
	-Static electricity itself doesn't harm computers
	-It's the discharge of static electricity that causes damage
	-Electro Static Discharge (ESD) is very damaging to computer components
		-Silicon is sensitive to high voltage
	-Static discharge
		-Approx. 3,500 volts (very low current(amperage))
		-Damage to electronic components: 100 volts or less
-Controlling Electro Static Discharge (ESD)
	-Keep humidity over 60%
		-Not very practical for indoors
		-Air conditioning prevent this amount of humidity 
	-'Self ground'
		-Touch exposed metal chassis of device being worked on
			-Equalizes electrical potential between self & device
		-Unplug power connection of device
		-DON'T connect yourself to the ground of an electrical system!!!!!!
			-SERIOUSLY DON'T
-Preventing Static Discharge
	-Anti-static strap
		-Connect to wrist & connect other end to metal part of device
	-Anti-static pad
		-Connect pad to metal of device being worked on
		-Workspace for device
	-Anti-static mat
		-Floor mat for standing/sitting
		-Prevent/minimize static buildup
	-Anti-static bag
		-Minimizes cases of ESD
		-To put components in 
			-Once out of device
			-To transport/ship  
-Component handling & storage
	-Try not to touch components directly
		-Card edges only
		-Might still have static electricity
	-Store in HVAC regulated environment
		-Between 50-80 degrees F
		-Or 10-27 degrees C
	-Avoid high humidity
		-Components don't like water in air
		-Silica gel packs to control humidity
	-Store in original padded box
		-Bubble wrap is a good alternative


###### **Safety Procedures 4.4**

-WARNING
	-Power is dangerous
	-Disconnect power
	-Don't touch any component you are unsure of
		-Capacitors store power
	-Don't work on inside power supplies
		-Meant to be swapped out as a unit
	-High Voltage
		-Power supplies, displays, laser printers
			-Have capacitors
-Equipment grounding
	-Electrical faults go into grounds 
		-Avoids person getting shocked
		-Computer products connect to grounds
	-Equipment racks
		-Components in rack & rack itself are all grounded
	-DON'T remove ground connections
	-NEVER CONNECT YOURSELF TO GROUND OF ELECTRICAL SYSTEM
-Cable management
	-Cables runs
		-Avoid across floors
			-Trip hazard
			-Follow edges of wall or use cable covers
		-Use cable ties or velcro
			-Relatively permanent attachment
			-Groups cables, easier to manage cables
-Personal safety
	-Lifting techniques
		-Lift with legs
		-Equipment to lift heavy objects
			-Don't carry overweight items
	-Electrical fire safety
		-Don't use water or foam
		-Use carbon dioxide, FM-200, or other dry chemicals
		-Remove power source
	-Safety googles
		-Working with chemicals
			-Printer toner, batteries, etc.
	-Air filter mask
		-Dust or toner in air
-Government regulations (OSHA)
	-Health/safety laws
		-Hazard free workplace
	-Building Codes 
		-Electrical codes, fire prevention/mitigation
	-Environmental regulations
		-Tech waste disposal


###### **Environmental Impacts 4.5**

-Disposal procedures
	-Read Material Safety Data Sheets (MSDS)
		-OSHA regulated
		-Sometimes referred to as Safety Data Sheet (SDS)
	-Provide information for all hazardous materials/chemicals
-MSDS info
	-Company/Product info
	-Composition & ingredients
	-Hazard info
	-First aid measure
	-Firefighting measure
	-Accidental leak/release
	-Handling & Storage & more
-Handling toxic waste
	-Batteries
		-Used a lot in many devices
		-Dispose at local hazardous waste facility
	-Toner 
		-Manufacturer recycle programs (sometimes)
		-Or dispose of properly
	-Other devices/components
		-Refer to MSDS
		-Don't just throw away 
-Room control
	-Temperature
		-Device needs constant cooling
	-Humidity levels
		-High humidity = condensation
		-Low humidity = static discharges 
		-Aim for 50%
	-Proper ventilation
		-Dust creates a mess
		-Use compressed air outside, computer vacuums inside
-Battery backup
	-Uninterruptible power supply
		-Backup power
			-Under voltage, power outage, surges
	-UPS types
		-Standby UPS
			-Small delay between switch
		-Line interactive UPS
			-Regulates power sag/surge
			-Switches in an outage in 2 to 4 milliseconds
		-Online UPS
			-Always running from battery
			-Main power charges batteries
	-Features
		-Auto shutdown
		-Battery capacity
		-Number of outlets 
		-Phone/ethernet suppression 
-Surge suppressor
	-Power isn't 'clean'
		-Voltage spikes & noise
	-Spikes are diverted to ground
	-Noise Filters 
		-Remove noise from electrical line
		-Remove decibels at certain frequencies
			-Higher decibel rating = more noise filtering
-Surge suppressor specs
	-Joule ratings
		-Surge absorption
		-200=good, 400=better, 600+ = best 
	-Surge amp rating
		-The higher the rating the better
	-UL 1449 voltage let through rating
		-Ratings at 500, 400, & 330 volts
		-The lower the better


###### **Incident Response 4.6**

-Chain of custody
	-Control evidence
	-Document everyone who contacts evidence
		-Avoid tampering
		-Use hashes for digital evidence
	-Label & catalog everything
		-Seal, store, protect (physical)
		-Digital signatures 
			-Ties a person to access of evidence
-First response
	-Identify issue
		-Check logs
		-Ask people
		-Monitoring data
	-Report to proper channel
		-Internal management, law enforcement, etc. 
		-Don't delay
	-Collect & protect info relating to event
		-Different data sources
		-Protection mechanisms
-Copy of drive
	-Copy contents of entire drive
		-Not just a file or folder
		-Bit for bit, byte for byte 
	-Remove physical drive
		-Use hardware write blocker
		-Preserve existing data
	-Software imaging tools
		-If you don't have hardware tools
		-Use a bootable device to copy internal drive to external evice
	-Use hashes & digital signatures 
		-Ensures data integrity
		-Drive image is hashed to ensure data has not been modified
-Documentation
	-Document findings
		-Everything you did & found
	-For internal use, legal proceedings, etc. 
	-Summary information
		-Overview of security event
	-Detailed explanation of data acquisition
		-Step by step process
	-Findings 
		-Analysis of data 
		-Others can compare their findings with yours
	-Conclusion
		-Professional results, given analysis
-Order of volatility
	-How long data sticks around.
		-Some data/media is more volatile than others
	-Gather data in order from most volatile to least volatile 
		-Most volatile↓
			-CPU registers, CPU cache
			-Router table, ARP cache, process table, kernel stats, RAM
			-Temp file systems
			-Disk
			-Remote logging & monitoring data
			-Physical config, network topology
			-Archival media
		-Least volatile↑


###### **Privacy, Licensing, & Policies 4.6**

-Software licensing
	-Most software includes a license
		-Terms & conditions
		-Use, number of copies, & backup options
	-Valid licenses
		-Per-seat = per person
		-Concurrent = how many people can use this at one time
			-If you have 20 people in organization but only 5 use software at a time:
				-You only need 5 licenses
		-Non expired licenses
			-Ongoing subscription
				-Annual, 3 year etc.
			-Use software until expiration date
-License 
	-Personal license
		-For home user
		-Usually associate with a single device
		-Perpetual license purchase (one time charge)
	-Corporate use license
		-Per seat/site license
		-Software may be installed in all company systems
		-Annual renewal costs (usually)
	-Open source license
		-Free & Open Source Software (FOSS)
			-Source code is open & available
			-End user can compile their own excutable
		-Closed source/ Comercial
			-Source code is private
			-End user gets compile .exe (executable)
		-End User Licensing Agreement (EULA)
			-How software can be used
-Non-disclosure Agreement (NDA)
	-A party/ies to contract cannot disclose information to outside parties
	-Protects confidential information
		-Trade secrets
		-Business activities
		-Anything listed in NDA
	-Unilateral or Bilateral (or multilateral) NDA
		-1 way or mutual NDA
		-Depends on how information is being shared
	-Formal Contracts
		-Signatures required
-Regulating credit card data
	-Payment Card Industry Data Security Standard (PCI DSS)
		-or PCI
	-6 control objectives
		-Build & maintain secure network & systems
		-Protect cardholder data
		-Maintain vulnerability management program
		-Implement strong access control measures
		-Regularly monitor & test networks
		-Maintain an information security policy 
-Personal government issues information
	-Used for government services 
		-SSN, driver license, etc.
	-Restrictions on collecting or storing gov information
		-Check local & federal regulations
	-U.S Office of Personnel Management (OPM)
		-Compromised PII (personal identifiable information)
		-July 2015 ~21.5 million people affected
		-Name, SSN, date of birth, etc.
-PII  (Personal Identifiable Information)
	-Any data that can identify an individual
		-Part of privacy policy
		-How will you handle PII
	-Very important data
		-Normalized data processing & protection
		-Easy to forget importance
	-Attackers use PII to gain access to impersonate/fraud
		-Bank account info
		-Password reset questions (with stolen info)
-PHI (Protected Health Information)
	-Health information associated with individual
		-Health status, records, payments, etc.
	-Data between providers 
		-Must maintain security requirements
	-HIPAA regulations
			-Health Insurance Portability & Accountability Act of 1996
-Data retention requirements
	-Keep files that frequently change for version control
		-Keep a week for example
	-Recover from virus infection
		-May need to retain 30 days of backups
		-Infection may not be identifiable immediately
	-Legal requirements for data retention
		-Email storage required for years
		-Tax information storage, PII, tape backups, etc.
-AUP (Acceptable Use Policy)
	-Outlines acceptable use of company assets
		-May be documented in rules of behaviors
	-Cover many topics
		-Internet, telephones, computers, mobile devices, etc.
	-Used by organization to limit legal liability
		-Someone is dismissed, documented reasons why
-Splash Screens
	-Message, logo, or graphic 
		-On startup/login
	-Informational 
		-Maintenance or system change info
	-Or Required for legal/admin purpose
		-System misuse warnings
		-Information about relying on app data 


###### **Professionalism 4.7** 

-Professional appearance
	-Match attire of current environment
	-Formal
	-Business casual
	-Follow your organizations rules
		-Find right balance
-Don't judge
	-Corporate cultural sensitivity
		-Use appropriate titles & designation
	-You are the teacher
		-Not a warden or judge
	-Make people smarter
		-They will use tech better
	-We all make mistakes 
		-Pobodies nerfect
-Be on time & avoid distractions
	-Avoid interruptions
	-Apologize for delays & unintended distractions
		-Apologize to customer/end user
	-Create a welcoming environment
		-Stay off speaker phone
		-Quiet background/ clear audio
-Difficult situations
	-Tech problems can be stressful
	-Don't argue/be defensive
		-Don't dismiss or contradict
	-Diffuse a difficult situation with active listening/questions
		-Build relationships
	-Communicate effectively
		-Let everyone know what is going on
	-Never put situation in a public space
		-Use discretion
-Maintain confidentiality
	-Privacy concerns
		-Sensitive professional and private info
	-Professional responsibilities
		-IT has access to a lot of corporate data
	-Respect
		-Treat others the way you want to be treated


###### **Communication 4.7**

-Comm skills
	-One of the most useful skills
	-Difficult to master
	-Skilled communicator is very marketable
-Avoid tech jargon
	-Abbreviations & 3 letter acronyms (TLAs)
-Avoid acronyms & slang
	-Be tech translator
-Communicate in ways anyone can understand
	-Think like a teacher, want your students to learn
	-Keep it simple!
	-Break down terms and use analogies that others understand 
-Maintain positive attitude
	-Positive tone of voice
	-Treat others as equals
	-Helps with issues that can't be fixed 
		-Do your best
		-Give options to move forwards
	-Your attitude has a direct impact on customer experience
-Avoid interrupting
	-Even if you know the answer!
	-Active listening, ask questions
		-Take notes
		-Build relationships with people
			-You will most likely come across them again
-Clarify customer statements
	-Ask pertinent questions
	-Repeat what customer explained to you back to them
		-Verifies what you heard & they meant
		-Everyone is one the same page
		-Identifies end user issue & able to work on resolution
		-Doesn't matter if you seem dumb. 
			-I rather be dumb & right than smart & wrong!
	-Ask clarifying questions
		-Don't assume
-Set expectations
	-Offer different options
		-Repair/replace
			-Explain pros/cons of each decision
	-Document everything
		-Follow up email
			-Issue documented
			-Both parties on same page
	-Keep everyone informed
		-Even if status is unchanged
		-Don't leave customers/ end user in the dark
	-Follow up after the fact
		-Verify resolution still working
		-Verify customer is happy


**Scripting Languages 4.8**

-Automation & Scripting
	-Script should match requirement
	-Task specific or OS available
	-Will probably learn more than 1 scripting language
		-Important skill for any tech
-Batch files
	- .bat file extension
	-Scripting language for Windows @ the command line
	-Legacy language going back to DOS & OS/2 
-Windows Powershell
	-Command link for system administrators
	- .ps1 file extension
	-Windows 10/11 included and/or can be installed easy
	-Extend command line functions
		-Use cmdlets (command-lets)
		-Powershell scripts & functions
		-Standalone executables (.exe)
			-Built from powershell scripts
		-Access OS directly or change OS config/settings
			-Gives you access you wouldn't normally have in a command line/batch file
	-Automate & integrate
		-Perfect for 
			-System Admin
			-Active domain admin
-Microsoft Visual Basic Scripting Edition
	-General purpose scripting in Windows
		-Runs outside of command line
		-Back end web server scripting
		-Scripting on Windows desktop
		-Scripting inside of Microsoft Office apps
			-Very common use
	-VBscript	
		- .vbs file extension
-Shell script
	-Scripting in Unix/Linux shell
		-Automate & extend command line
	-Don't require file extension
		-Commonly use .sh file extension
		-Starts with a shebang or hash-bang; #!
			-Script always start with this symbol
			-Indicates its a Unix/Linux shell script
-JavaScript
	-Scripting inside your browser
		- .js file extension
		-Work behind the scenes
	-Add interactivity to HTML & CSS
		-Used on almost every website
		-Lets you interact with items on a webpage 
	-JavaScript is NOT Java
			-Java is programming language to create applications
			-Different developers & origins
			-Different use & implementation
-Python
	-General purpose scripting language 
		- .py file extension
		-can apply to many OS
	-Popular in many technologies 
		-Broad appeal & support


**Scripting Use Cases 4.8**

-Basic Automation
	-Automate tasks
		-You don't have to be there
		-Don't have to watch event logs
		-Or wait for events to occur
		-Monitor & resolve problems before they happen
	-Speed
		-Script is faster than a human
			-As fast a computer deploying script
		-No typing, delays, or human errors
	-Automate mundane tasks
		-You can do something for important/creative
-Restarting machines/devices
	-Scripting device to turn off & back on
	-Application updates
		-Some apps require a system restart
	-Security patches
		-Deploy patch overnight & reboot system
	-Troubleshooting
		-Once a day restart
	-These help especially when you don't have physical access
-Remapping network drives
	-Login script to
		-Connect network drives
		-Automate other common tasks during startup
	-Automate software update/changes
		-Map a drive to the app repository 
	-Add or move user data 
		-Automate backup process
-Application Installations
	-Install applications automatically
		-Don't have to visit every device with a drive
		-Many apps have an automated install process
			-Scripting can turn install into a hands-off process
	-On demand or automatic install scripts 
		-Process
			-Map app install drive
			-Install app without user prompts
			-Disconnect the drive
			-Restart system
-Automated backups
	-Usually performed at night or off hours
	-Time consuming
		-File systems & network connections
	-Script an automated backup process
		-Works while you are away from work
		-Don't have to think about it
		-Systems ready to go for working hours
-Information gathering
	-Get specific information from remote device
		-Monitoring & reporting
		-All happens behind the scenes
		-Can resolve issues automatically
	-Performance monitoring
		-Confirm proper operation of a device
	-Inventory management
		-Check hardware or software config of devices
	-Security & vulnerability checks
		-Check for application or library versions
		-Plan for latest patches
		-If update/patch is available:
			-Can run update script with conditionals
	-All items can be scripted to be done automatically
		-Saves time
		-Catch issues before they get bigger
-Initiating updates
	-Constantly happening
		-Nothing stays the same
	-OS
		-New features, security patches
	-Device drivers
		-Bug fixes
		-New hardware, OS support
	-Applications
		-New version rollouts
-Other scripting considerations
	-Don't unintentionally introduce malware
		-Make sure you only install from trusted sources 
	-Inadvertently change system settings
		-Test all updates
		-Track file and registry changes 
		-Rollback script in case unwanted changes occur 
			-Best practice
	-Browser or system crashes
		-Syntax errors, misplaced characters, etc. in script can have unintended consequences
			-Can create downtime with script errors 
		-Always backup & have a backup
		-Always test scripts before deployment


**Remote Access 4.9**

-Remote desktop connections
	-Share a desktop from a remote location
	-RDP (Microsoft Remote Desktop Protocol)
		-Clients for macOS, Linux, & other OSes
	-VNC (Virtual Network Computing)
		-Open source options
			-Some are closed source
		-Uses Remote Frame Buffer (RFB) protocol
		-Clients for many operating systems
	-Commonly used for technical support
		-Scammers too, beware
-Remote desktop security
	-Microsoft Remote Desktop Service
		-Open port of tcp/3389 is evidence of connection
			-Most likely running RDP
		-Username & password to login
			-Brute force attack is common
			-Add multifactor authentication
				-Limits scammers
			-Same thing for 3rd party remote desktops
				-Ex. VNC
		-Once you remote connect, you're in
			-Can control the computer as if its their own
			-Makes scams/fraud very easy
-VPNs
	-Virtual Private Network
		-Encrypts data traversing public networks
	-Concentrator
		-Encryption/decryption device
		-Often integrated into firewall
	-Many deployment options
		-Software based options
		-Specialized cryptographic hardware 
			-Part of next gen firewalls
	-Used with client software 
		-OS built in, sometimes
-VPN security
	-VPN data on the network is very secure
		-Best encryption technologies
	-Authentication is critical
		-Attacker with right credentials can gain access
		-Brute force attacks
		-Almost always includes multifactor authentication
-SSH (Secure Shell)
	-Connect to remote device
	-Can make configuration changes
	-Encrypted console communication tcp/22
		-Looks & acts same as Telnet tcp/23
			-Telnet data is in the clear; unencrypted
-SSH security
	-Network traffic is encrypted
		-Nothing to see in packets
	-Authentication is a vulnerability concern
		-SSH supports public/private key pairs
	-SSH to certain accounts should be disabled
		-Root or any superuser
		-Consider removing pass based authentication & only use certificate auth
	-Limit access to SSH by IP address
		-Configure local firewall or network fiter
			-Only allow certain IP address access
-RMM (Remote Monitoring & Management)
	-Managed Service Provider
		-Organization outsource monitoring & maintenance of network
		-MSP's provide that service
		-Many customer & systems to monitor
		-Many different service levels
	-RMM
		-Manage a system from a remote location
	-Many features
		-Patch OSes
		-Remote login
		-Anomaly monitoring
		-Hardware/software inventory
-RMM security 
	-Popular point of attack
		-Has access to many systems & information
	-Access should be limited
		-Don't allow anyone to connect to RMM service
		-Require multifactor auth
	-Auditing
		-To monitor who is connecting to RMM service
-SPICE
	-Simple Protocol for Independent Computing Environments
	-Remote desktop specialized for virtual machines
		-"VM-centric"
		-View & control remote display of a virtual machine
	-Helps maintain virtual machines
		-Across many different OSes/VMs
		-One seamless remote control solution
	-Operates like other remote desktops
		-Efficient graphics rendering
		-Fast response time
		-Folder & clipboard sharing between device & VM
-WinRM (Windows Remote Management)
	-Run command line commands/scripts on remote Windows server
		-Default on most Windows servers
	-Admin sends a script to remote device
		-Secure communication & authentication required
	-Script runs on remote device
		-As if admin was local
	-Output sent back to requesting workstation
		-Don't have to leave chair to get results of script 
-3rd party tools
	-Screen sharing
		-GoToMyPC, TeamViewer, etc.
	-Video-conferencing
		-Zoom, Webex, etc.
	-File transfer 
		-Dropbox, Google drive, etc.
	-Desktop management
		-Citric endpoint management, etc.

**Managing AI 4.10**

-Artificial Intelligence
	-Technology designed to meet/exceed human intelligence
		-Learn, infer, & reason
		-Not new concept
	-Content generation
		-Music, video, pictures, etc.
-Application integration
	-AI is everywhere
		-Integrated into apps
	-Search engines
		-Search results are consolidated & summarized
		-Combines results from multiple sites into single view 
	-Email applications & services
		-Summarize emails
		-Take meeting notes
	-Graphic editors
		-Fill in or remove content with generative AI
		-Describe an image and AI will generate
-Appropriate AI use 
	-Process large data repositories
		-Parse & summarize data
		-Correlate data types & identify trends 
		-Parse through TB of log files & ID potential security issues 
	-Automation
		-Incorporated into scripting/automation
		-Identify issues & correct without human intervention
	-Healthcare
		-Provide diagnostics (mri, x-ray, etc.), ongoing monitoring, drug interactions, etc.
	-Communication
		-Real time language translation
		-Proofreading 
-Inappropriate AI use 
	-Fraud
		-Impersonate a real person
		-Deepfake audio/video
	-Unethical shortcuts
		-Create code with human knowledge/input
		-Graphic design not human generated
	-Plagiarism
		-Paraphrase existing works without proper citation
		-Or worse
-AI bias 
	-AI only knows what it is told
		-Can make wrong/biased assumptions/conclusions
		-Bias in the data
		-Bias in the algorithms
	-Ex. of bias
		-Amazon resume AI analysis to hire
			-Based on 10 years of submitted resumes
			-Terms such as 'executed' & 'captured' largely male used
			-AI bias towards picking male resumes
-AI hallucinations
	-Misinterpretation of data 
		-Confidently incorrect AI
	-Ex. Tell AI pictures having a snout, tail, and 4 legs is a dog
			-Show picture of a pig
			-The pig is obviously a real dog 
-AI accuracy  
	-Builds conclusions using models
		-Models can make bad predictions
	-AI measurement
		-Get predictions form AI
		-Compare predictions to known test data
-Public vs Private AI
	-Public AI
		-ChatGPT, Google Gemini, etc.
		-Available on internet
	-Private AI
		-Internal AI engine
		-Contains proprietary company data
		-Organization has complete control over AI modeling 
	-Data security
		-Information added to public AI engines can be retrieved
			-Passwords, encryption keys, certificate details
	-Data source
		-Private; data is specific to single entity
		-Public; more accurate since it has more data input
	-Data privacy
		-Huge amounts of data about anyone, including YOU!
		-AI knows where you live, habits, memberships, etc.