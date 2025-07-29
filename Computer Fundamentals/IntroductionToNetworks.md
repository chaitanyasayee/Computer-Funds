In simple terms network is like a group of devices that are connected so they can share Information and work together.

A Network is just a way to link devices so they can talk to each other and share stuff easily

A Computer Network is just a way for devices to woke together, sharing and helping each other much like a human network but using Technology

## Benifits of Computer Network

### Resource Sharing

In Computer networks, resource sharing allows multiple devices or user to access shared resources such as files, printers, or databases over the network, optimizing resource utilization and reducing redundancy

### Load Balancing

It distributes network traffic or computional task across multiple servers or devices to ensure efficient utilization, prevent bottlenecks and enhance system performance

### High Reliability

High realiabilty in computer network ensures consistent and dependable operation by incorporating fault tolerance, redundancy and failure mechanism to minimize down time and data loss

### Location Independence

Location independence enables user to access network resources or services without needing to know the physical location of the resources, promoting seamless and flexible connection

## Transmission Mode:

It refers to the direction in which data flows between 2 devices in a [network.It](http://network.It) defines how data in sent and received over a communication channel.

### 1. Simplex Mode

Data flows in only 1-D, means one device can send data while other can only receive.

Eg. Televison

### 2.Half -Duplex Mode

Data can Travel in 2-D, but not simultneously.

eg. Walkie-talkie

### 3.Full -Duplex Mode

This mode allows data to flow in 2-D simultaneously.

eg. phone call

## Components of Network:

### 1 Hardware Components:

### Node(End Devices):Computers,Smart Phones or servers that exchange data

### Transmission Media:

**Wired**:Ethernet cables, fibre optics

**Wireless:** Wi-Fi,Bluetooth

**Network Interface Card(NIC):** Hardware allowing devices to connect to a network

### Switches and router:

**Switch:**Connects devices within a local network

- **Forwards data** based on **MAC addresses** (hardware addresses of devices).
- Creates a network by connecting multiple devices together.
- Operates at **Layer 2 (Data Link layer)** of the OSI model (sometimes Layer 3 with advanced models).
- **No IP addressing** involved for basic switches.

**Router:** Connects multiple networks and directs data packet

A **router** connects **different networks** together – most commonly, your home network to the internet.

- Forwards data based on **IP addresses**.
- Assigns IP addresses via **DHCP**.
- Can perform **Network Address Translation (NAT)** to share one public IP.
- Operates at **Layer 3 (Network layer)** of the OSI model.
- Often includes firewall and wireless (Wi-Fi) capabilities.

### Software Components

### **Protocols**

- Set of **rules** and **standards** for data communication.
- Ensure reliable and structured data transfer.
- Common Protocols:
  - **TCP/IP**: Core suite for internet communication.
  - **HTTP/HTTPS**: Web browsing.
  - **FTP**: File transfers.
  - **SMTP/IMAP**: Email transmission.
  - **DNS**: Resolving domain names to IP addresses.

### **Network Operating System (NOS)**

- A specialized OS that manages **network resources** and **user access**.
- Provides services like:
  - File and printer sharing
  - User authentication
  - Network security
- Examples:
  - **Windows Server**
  - **Linux (Ubuntu Server, Red Hat)**
  - **Novell NetWare**

## Types Of Networks & InterConnected Networks

Computer networks can be broadly categorized based on their **geographic scope** and **functionality**. The main types include:

### **1. Local Area Network (LAN)**

**Definition:**

A LAN is confined to a small geographic area, such as a home, office, or campus. It connects devices like computers, printers, and servers to share resources.

**Real-Life Analogy:**

Your home Wi-Fi network connecting all your devices in a small space.

**Key Features:**

- High-speed data transfer.
- Covers a limited range (few meters to a few kilometers).
- Easy to install and manage.
- Secure, with limited external access.

**Example:**

A college campus where computers in labs, libraries, and admin offices are connected to share files and applications.

### **2. Wide Area Network (WAN)**

**Definition:**

A WAN spans a large geographic area and connects multiple smaller networks (LANs or MANs). The **Internet** is the best example of a WAN.

**Real-Life Analogy:**

A vast highway system connecting different cities, enabling long-distance communication.

**Key Features:**

- Covers countries or continents.
- Typically slower than LAN due to long distances.
- Expensive to set up and maintain.
- Utilizes leased telecommunication lines.

**Example:**

A bank's network connecting branches across the country.

### **3. Metropolitan Area Network (MAN)**

**Definition:**

A MAN connects multiple LANs within a city or metropolitan area.

**Real-Life Analogy:**

A city's public transit network connecting various districts for smooth commuting.

**Key Features:**

- Covers up to 50 km.
- Faster than WAN but slower than LAN.
- Usually maintained by ISPs or telecom providers.

**Example:**

City-wide broadband internet or a university’s network spread across different campuses.

### **4. Personal Area Network (PAN)**

**Definition:**

A PAN connects devices in an individual’s workspace.

**Real-Life Analogy:**

The space around a person where personal devices like a phone, smartwatch, and Bluetooth headphones connect.

**Key Features:**

- Short range (typically up to 10 meters).
- Mostly wireless.
- Focused on personal device intercommunication.

**Example:**

Bluetooth connection between a laptop and a wireless mouse.

| **Feature**            | **LAN**                 | **WAN**                        | **MAN**                    | **PAN**                      |
| ---------------------- | ----------------------- | ------------------------------ | -------------------------- | ---------------------------- |
| **Geographical Scope** | Small (building/campus) | Very large (country/continent) | Medium (city/metropolitan) | Very small (personal space)  |
| **Speed**              | High                    | Moderate to Low                | Moderate                   | High                         |
| **Cost**               | Low                     | High                           | Moderate                   | Low                          |
| **Examples**           | Home, school networks   | Internet, bank networks        | City cable TV              | Bluetooth headset with phone |

## **Interconnected Networks (LANs, MANs, WANs)**

Interconnecting various network types allows for **seamless communication and resource sharing** across local, regional, and global levels.

**Real-Life Analogy:**

A hierarchy of highways connecting neighborhoods (LANs), cities (MANs), and countries (WANs).

**Example:**

A multinational corporation linking its branch LANs, city MANs, and global WANs into a unified system.

## **Internet**

The **Internet** is the largest example of a WAN — an interconnected network of millions of devices and smaller networks around the globe.

**Key Features:**

- Provides **global communication** and access to information.
- Based on **open standards and protocols** (e.g., TCP/IP).
- Decentralized, fault-tolerant architecture.

**Components:**

- Client Devices: Smartphones, laptops, PCs.
- **Servers:** Host websites, applications, databases.
- **Backbone Networks:** High-speed fiber optic lines connecting continents.
- **ISPs:** Internet Service Providers offering end-user connectivity.

## **Routing and Switching**

These are fundamental processes for directing traffic in a network.

### **1. Routing**

**Definition:**

Routing is selecting the **optimal path** for data to travel from source to destination across networks.

**Key Points:**

- Operates at **OSI Layer 3 (Network Layer)**.
- Uses **IP addresses** and **routing tables**.
- Common routing protocols: **OSPF**, **BGP**, **RIP**.
  ### **2. Switching**
  **Definition:**
  Switching is the process of transferring data within the same network, directing it to the correct destination device.
  **Key Points:**
  - Operates at **OSI Layer 2 (Data Link Layer)**.
  - Uses **MAC addresses** to forward frames.
  - Ensures fast and secure intra-network communication.

## **Network Protocols for Interconnectivity**

**Protocols** define how data is formatted and transmitted between devices in a network.

### **Key Protocols:**

| **Protocol**   | **Function**                                                                    |
| -------------- | ------------------------------------------------------------------------------- |
| **TCP/IP**     | Core protocol for end-to-end data transmission. Splits and reassembles packets. |
| **HTTP/HTTPS** | Transfers web content between clients and servers.                              |
| **SMTP**       | Sends emails between mail servers.                                              |
| **FTP**        | Transfers files between computers.                                              |
| **DNS**        | Resolves domain names into IP addresses.                                        |

---

## **Global Backbone Networks**

Backbone networks are the **infrastructure layer** of the internet, enabling **high-speed, international data flow**.

**Key Features:**

- Built using **undersea fiber-optic cables**, satellites, and terrestrial lines.
- Maintained by **large telecoms and ISPs**.
- Provide redundancy, low latency, and fault tolerance.

**Example:**

**APNIC** (Asia-Pacific Network Information Centre) manages backbone routes in the Asia-Pacific region.

## Network and logical Topology

## **Network Topologies**

A **network topology** refers to the **arrangement of devices (nodes)** and **connections** in a network. It determines how data travels between devices and defines the network's structure, efficiency, scalability, and fault tolerance.

---

### 📂 **Types of Topologies**

### **1. Physical Topology**

- Represents the **actual layout** of cables, computers, and devices.
- Focuses on **hardware setup**.

### **2. Logical Topology**

- Describes **how data flows** across the network, regardless of physical layout.
- Focuses on **communication rules** and **data pathways**.

---

### **Real-Life Analogy**

Think of topologies like a **city's road system**:

- **Physical Topology** = actual roads and intersections.
- **Logical Topology** = traffic flow rules and preferred paths for vehicles (data).

---

## **Common Physical Topologies**

---

### **1. Star Topology**

**Structure:** All devices connect to a **central hub/switch**.

**Key Features:**

- Centralized management and control.
- Easy to add/remove devices.
- If the hub fails, entire network goes down.

**Example:** Office LANs where all devices connect to a switch/router.

---

### **2. Ring Topology**

**Structure:** Devices connected in a **circular loop**.

**Key Features:**

- Data travels **sequentially** in one direction.
- A break in the ring can disrupt the entire network.
- Dual-ring systems improve fault tolerance.

**Example:** Legacy token-ring networks.

---

### **3. Mesh Topology**

**Structure:** Each device connects **directly** to every other device.

**Key Features:**

- **No single point of failure**.
- Extremely reliable and secure.
- High implementation cost due to cabling.

**Example:** Military or emergency systems requiring high availability.

---

### **4. Bus Topology**

**Structure:** All devices share a **single backbone cable**.

**Key Features:**

- Cost-effective and simple.
- Signal degradation over long distances.
- Entire network fails if the backbone is damaged.

**Example:** Older Ethernet networks.

---

### **Comparison of Topologies**

| **Feature**     | **Star**            | **Ring**                | **Mesh**               | **Bus**                |
| --------------- | ------------------- | ----------------------- | ---------------------- | ---------------------- |
| Structure       | Central hub         | Circular loop           | Fully connected        | Shared cable           |
| Fault Tolerance | Moderate (hub fail) | Low (break affects all) | High (redundant paths) | Low (backbone failure) |
| Cost            | Moderate            | Low                     | High                   | Low                    |
| Scalability     | Easy                | Difficult               | Complex                | Limited                |
| Performance     | High                | Medium                  | High                   | Low                    |

---

## **Logical Topologies**

Logical topologies focus on **how data is transmitted** within a network, regardless of the physical connections.

---

### **1. Logical Bus Topology**

- All devices share a **common channel** for data transfer.
- Devices listen to all data but only process intended packets.

**Use Case:** Small networks or older Ethernet setups.

---

### **2. Logical Ring Topology**

- Data moves in a **predefined circular path**.
- Each device passes the data along the ring.

**Use Case:** Controlled environments needing **sequential access** (e.g., Token Ring).

---

## **Token Passing**

**Definition:**

A method where a special data packet, called a **token**, circulates in the network. A device must **possess the token** to send data.

**Key Features:**

- Prevents data collisions.
- Ensures orderly data transmission.
- Common in **logical ring topologies**.

**Example:** Manufacturing plant networks ensuring critical device data isn’t interrupted.

---

## **FDDI (Fiber Distributed Data Interface)**

**Definition:**

FDDI is a high-speed standard that uses **dual-ring topology** for redundancy and employs **fiber optics or copper cables**.

**Key Features:**

- Supports speeds up to **100 Mbps**.
- Dual ring provides **automatic failover**.
- Suitable for large networks like **campuses or research labs**.

**Use Case:** Backbone networks in universities and data centers.

---

## **Virtual LANs (VLANs)**

**Definition:**

A **VLAN** is a **logical grouping** of devices in the same broadcast domain, **regardless of physical location**.

**Key Features:**

- Improves performance and security by isolating traffic.
- Reduces unnecessary broadcast traffic.
- Configurable through **managed switches and routers**.

**Use Case:**

In a corporate office, VLANs separate traffic between departments like HR, Finance, and IT.

---

## **Logical vs Physical Topologies**

| **Aspect**         | **Logical Topology**                       | **Physical Topology**                           |
| ------------------ | ------------------------------------------ | ----------------------------------------------- |
| **Definition**     | Describes **data flow**                    | Describes **physical arrangement**              |
| **Focus**          | Virtual/communication rules                | Hardware layout (cables, devices)               |
| **Dependency**     | Independent of hardware layout             | Dependent on actual cable/device setup          |
| **Examples**       | Logical Bus, Ring, VLANs                   | Star, Mesh, Bus, Ring                           |
| **Implementation** | Software/protocol based                    | Hardware based                                  |
| **Use Case**       | Network management and communication logic | Physical installation and infrastructure design |
