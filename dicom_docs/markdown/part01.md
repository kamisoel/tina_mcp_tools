# PS3.1

## DICOM PS3.1 2025b - Introduction and Overview

# 1 Scope and Field of Application

PS3.1 provides an overview of the entire Digital Imaging and Communications in Medicine
 (DICOM) Standard. It describes the history, scope, goals, and structure of the Standard. In
 particular, it contains a brief description of the contents of each Part of the
 Standard.

## 1.1 Scope of DICOM

Digital Imaging and Communications in Medicine (DICOM) is the standard for the communication and management of medical imaging information and related data.

The DICOM Standard facilitates interoperability of medical imaging equipment by
 specifying:

* For network communications, a set of protocols to be followed by devices claiming
 conformance to the Standard.
* The syntax and semantics of Commands and associated information that can be
 exchanged using these protocols.
* For media communication, a set of media storage services to be followed by devices
 claiming conformance to the Standard, as well as a File Format and a medical directory
 structure to facilitate access to the images and related information stored on
 interchange media.
* Information that must be supplied with an implementation for which conformance to
 the Standard is claimed.

The DICOM Standard does not specify:

* The implementation details of any features of the Standard on a device claiming
 conformance.
* The overall set of features and functions to be expected from a system implemented
 by integrating a group of devices each claiming DICOM conformance.
* A testing/validation procedure to assess an implementation's conformance to the
 Standard.

## 1.2 Field of Application

The DICOM Standard pertains to the field of Medical Informatics. Within that field, it
 addresses the exchange of digital information between medical imaging equipment and other
 systems. Because such equipment may interoperate with other medical devices and information systems, the scope of this
 Standard needs to overlap with other areas of medical informatics. However, the DICOM Standard
 does not address the breadth of this field.

This Standard has been developed with an emphasis on diagnostic medical imaging as practiced in radiology, cardiology, pathology, dentistry,
 ophthalmology and related disciplines, and image-based therapies such as interventional radiology, radiotherapy and surgery.
 However, it is also applicable to a wide range of image and non-image related information exchanged in clinical, research,
 veterinary, and other medical environments.

This Standard facilitates interoperability of systems claiming conformance in a multi-vendor environment, but does not, by itself,
 guarantee interoperability.

## 1.3 History

With the introduction of computed tomography (CT) followed by other digital diagnostic
 imaging modalities in the 1970's, and the increasing use of computers in clinical
 applications, the American College of Radiology (ACR) and the National Electrical
 Manufacturers Association (NEMA) recognized the emerging need for a standard method for
 transferring images and associated information between devices manufactured by various
 vendors. These devices produce a variety of digital image formats.

The American College of Radiology (ACR) and the National Electrical Manufacturers
 Association (NEMA) formed a joint committee in 1983 to develop a standard to:

* Promote communication of digital image information, regardless of device
 manufacturer
* Facilitate the development and expansion of picture archiving and communication
 systems (PACS) that can also interface with other systems of hospital
 information
* Allow the creation of diagnostic information data bases that can be interrogated
 by a wide variety of devices distributed geographically.

ACR-NEMA Standards Publication No. 300-1985, published in 1985 was designated version
 1.0. The Standard was followed by two revisions: No. 1, dated October 1986 and No. 2, dated
 January 1988. These Standards Publications specified a hardware interface, a minimum set of software commands, and a consistent set of data formats.

ACR-NEMA Standards Publication No. 300-1988, published in 1988 was designated version
 2.0. It included version 1.0, the published revisions, and additional revisions. It also
 included new material to provide command support for display devices, to introduce a new
 hierarchy scheme to identify an image, and to add data elements for increased specificity
 when describing an image.

In 1993, ACR-NEMA Standard 300 was substantially revised and replaced by this Standard, designated Digital Imaging and Communications in
 Medicine (DICOM). It embodies a number of major enhancements to previous versions of the
 ACR-NEMA Standard:

* It is applicable to a networked environment. The ACR-NEMA Standard was applicable
 in a point-to-point environment only; for operation in a networked environment a
 Network Interface Unit (NIU) was required. DICOM supports operation in a networked
 environment using the industry standard networking protocol TCP/IP.
* It is applicable to off-line media exchange. The ACR-NEMA Standard did not
 specify a file format or choice of physical media or logical filesystem. DICOM
 supports operation in an off-line media environment using industry standard media such
 as CD-R, DVD-R and USB and common file systems.
* It is a service oriented protocol, specifying the semantics of commands and associated data, and how devices claiming conformance to the Standard react to commands
 and data being exchanged. Specified services include support for management of the workflow of an imaging department. The ACR-NEMA Standard was confined to the transfer of data
 with only implicit service requirements.
* It specifies levels of conformance. The ACR-NEMA Standard specified a minimum
 level of conformance. DICOM explicitly describes how an implementor must structure a
 Conformance Statement to select specific options.

In 1995, with the addition of DICOM capabilities for cardiology imaging supported by the American College of Cardiology, the ACR-NEMA Joint Committee
 was reorganized as the DICOM Standards Committee, a broad collaboration of stakeholders across all medical imaging specialties.

## 1.4 Principles

### 1.4.1 Global Applicability and Localization

DICOM is a world-wide standard that can be used in every locale. It provides mechanisms to handle data that support cultural requirements,
 such as different writing systems, character sets, languages, and structures for addresses and person names. It supports the variety of workflows,
 processes and policies used for biomedical imaging in different geographic regions, medical specialties and local practices.

Localization to meet the requirements of national or local health and workflow policies can be done without deviating from the Standard.
 Such localization may include specifying code sets (e.g., procedure codes), or profiling data element usage (both specifying locally allowed
 values, and making elements that are optional in the Standard mandatory for local use).

Localization and profiling can be specified in a number of mechanisms outside the purview of the DICOM Standard.
 One such mechanism is Integration Profiles from the Integrating the Healthcare Enterprise (IHE) organization.
 It is important that Profiling adhere to the concept of non-contradiction.
 A Profile can add requirements but should not contradict DICOM requirements, as that would make it
 impossible to comply with both DICOM and the Profile.

### 1.4.2 Continuous Maintenance

The DICOM Standard is an evolving standard and it is maintained in accordance with
 the Procedures of the DICOM Standards Committee.
 Proposals for enhancements are welcome from all users of the Standard, and may be submitted to the Secretariat.
 Supplements and corrections to the Standard are balloted and approved several times a year.
 When approved as Final Text, each change becomes official, is published separately, and goes into effect immediately.
 At intervals, all of the approved Final Text changes are consolidated and published in an updated edition of the Standard.
 Once changes are consolidated into an updated edition of the Standard, the individual change documents are not maintained;
 readers are directed to use the consolidated edition of the Standard.

A requirement in updating the Standard is to maintain effective compatibility with previous editions.

The maintenance process may involve retirement of sections of the Standard.

Retirement does not imply that these features cannot be used. However, the DICOM
 Standards Committee will not maintain the documentation of retired features. The reader is
 referred to earlier editions of the Standard.

The use of the retired features is discouraged for new implementations, in favor of those
 alternatives remaining in the Standard.

### 1.4.3 Information Objects and Unique Object Identification

Many DICOM services involve the exchange of persistent information objects, such as images.
 An instance of such an information object may be exchanged across many systems and many organizational contexts, and over time.
 While minor changes may be made to the attributes of an instance to facilitate its handling within a particular organization
 (e.g., by coercing a Patient ID to the value used in a local context), the semantic content of an instance does not change.

Each instance is identified by a globally unique object identifier, which
 persists with the instance across all exchanges. Changes to the semantic content of an instance are defined to create a new instance,
 which is assigned a new globally unique object identifier.

### 1.4.4 Conformance

Conformance to the DICOM Standard is stated in terms of Service-Object Pair (SOP) Classes, which represent Services
 (such as Storage using network, media, or web) operating on types of Information Objects (such as CT or MR images).

SOP Class specifications in the DICOM Standard are only changed in a manner that is intended to be forward and backward
 compatible for all editions of the Standard. Conformance requirements and conformance claims are therefore referenced to the
 identifier of the SOP Class, and never referenced to an edition of the Standard.

Each implementation is required to provide a Conformance Statement, in accordance with a consistent pro forma structure,
 facilitating comparison of products for interoperability.

### 1.4.5 Consistency of Information Model

A large number of information objects defined in the DICOM Standard follow a common composite information model with
 information entities representing Patient, Study, Series, Equipment, Frame of Reference, and the specific instance data type.
 This information model is a simplification of the real world concepts and activities of medical imaging;
 for acquisition modalities, a Study is approximately equivalent to an ordered procedure, and a Series is approximately
 equivalent to a performed data acquisition protocol element. In other domains, such as Radiotherapy, the Study and Series are
 less clearly related to real world entities or activities, but are still required for consistency.
 This simplified model is sufficient for the pragmatic needs of managing imaging and related data collected in routine practice.

New information objects defined in DICOM will typically conform to this existing common information model,
 allowing reuse of implementations with minimal changes to support the new objects.

# 2 Normative References

[ISO/IEC Directives, Part 2] ISO/IEC. 2016/05. 7.0. *Rules for the structure and drafting of International Standards*. <http://www.iec.ch/members_experts/refdocs/iec/isoiecdir-2%7Bed7.0%7Den.pdf>. 

[ACR/NEMA 300] ACR/NEMA. 1988. *Digital Imaging and Communications*. 

[EBU-SMPTE-VSF JT-NM Phase 2 Report] European Broadcasting Union (EBU), Society of Motion Picture and Television Engineers (SMPTE), and Video Services Forum (VSF). 2015. v1.0. *Joint Task Force on Networked Media (JT-NM) Phase 2 Report- Reference Architecture*. <https://static.jt-nm.org/RA-1.0/JT-NMReferenceArchitecturev1.0%20150904%20FINAL.pdf>. 

[ISO/IEC 8822] ISO/IEC. 1994. *Information Processing Systems - Open Systems Interconnection - Connection Oriented Presentation Service Definition*. 

[ISO/IEC 8649] ISO/IEC. 1996. *Information Processing Systems - Open Systems Interconnection - Service Definition for the Association Control Service Element*. *Withdrawn 2012.*. 

[SMPTE ST 2110-10] Society of Motion Picture and Television Engineers (SMPTE). 2017. *Professional Media over IP Networks: System Timing and Definitions*. 

[SMPTE ST 2110-20] Society of Motion Picture and Television Engineers (SMPTE). 2017. *Professional Media over IP Networks: Uncompressed Active Video*. 

[SMPTE ST 2110-30] Society of Motion Picture and Television Engineers (SMPTE). 2017. *Professional Media over IP Networks: PCM Digital Audio*. 

# 3 Definitions

Attribute
:   A property of an Information Object. An Attribute has a name and a value that are independent of any encoding scheme.

Command
:   A request to operate on information across a network.

Command Element
:   An encoding of a parameter of a command that conveys this parameter's value.

Command Stream
:   The result of encoding a set of DICOM Command Elements using the DICOM encoding scheme.

Conformance Statement
:   A formal statement that describes a specific implementation of the DICOM Standard. It specifies the Service Classes, Information Objects, Communication Protocols, Security Profiles, and Media Storage Application Profiles supported by the implementation.

Data Dictionary
:   A registry of DICOM Data Elements that assigns a unique tag, a name, value characteristics, and semantics to each Data Element.

Data Element
:   A unit of information as defined by a single entry in the data dictionary.

Data Set
:   Exchanged information consisting of a structured set of Attributes. The value of each Attribute in a Data Set is expressed as a Data Element.

Data Stream
:   The result of encoding a Data Set using the DICOM encoding scheme (Data Element Numbers and representations as specified by the Data Dictionary).

Information Object
:   An abstraction of a real information entity (e.g., CT Image, Structured Report, etc.) that is acted upon by one or more DICOM Commands.

### Note

This term is primarily used in PS3.1, with a few references in [PS3.3](part03.html#PS3.3). It is an informal term corresponding to a formal term that is introduced in [PS3.3](part03.html#PS3.3). In all other parts of the DICOM Standard this formal term is known as an Information Object Definition.

Information Object Class
:   A formal description of an Information Object, which includes a description of its purpose and the Attributes it possesses. It does not include values for these attributes.

### Note

This term is only used in PS3.1. It is an informal term corresponding to a formal term that is introduced in [PS3.4](part04.html#PS3.4). This formal term is known as a Service-Object Pair Class or more commonly as a SOP Class.

Information Object Instance
:   A representation of an occurrence of a real-world entity, which includes values for the Attributes of the Information Object Class to which the entity belongs.

### Note

This term is only used in PS3.1. It is an informal term corresponding to a formal term that is introduced in [PS3.4](part04.html#PS3.4). This formal term is known as a Service-Object Pair Instance or more commonly as a SOP Instance.

Message
:   A data unit of the Message Exchange Protocol exchanged between two cooperating DICOM Applications. A Message is composed of a Command Stream followed by an optional Data Stream.

Part
:   Subdivision of the DICOM Standard that covers related subject material.

Service Class
:   A structured description of a service that is supported by cooperating DICOM Applications using specific DICOM Commands acting on a specific class of Information Object.

Service-Object Pair Class (SOP Class)
:   The pair of an Information Object and either a DIMSE Service Group, a Media Storage Service, or a Web Service.

Essence
:   Video, audio or data type of source, as defined in [[EBU-SMPTE-VSF JT-NM Phase 2 Report]](#biblio_EBU-SMPTE-VSF_JT-NM_Phase2Report "Joint Task Force on Networked Media (JT-NM) Phase 2 Report- Reference Architecture").

Flow
:   A sequence of Grains from a Source; a concrete representation of content emanating from the Source, as defined in [[EBU-SMPTE-VSF JT-NM Phase 2 Report]](#biblio_EBU-SMPTE-VSF_JT-NM_Phase2Report "Joint Task Force on Networked Media (JT-NM) Phase 2 Report- Reference Architecture").

Grain
:   Represents an element of Essence or other data associated with a specific time, such as a frame, or a group of consecutive audio samples, or captions, as defined in [[EBU-SMPTE-VSF JT-NM Phase 2 Report]](#biblio_EBU-SMPTE-VSF_JT-NM_Phase2Report "Joint Task Force on Networked Media (JT-NM) Phase 2 Report- Reference Architecture").

Rendition
:   A collection of time-synchronized Flows intended for simultaneous presentation, providing a complete experience of a Source Group, as defined in [[EBU-SMPTE-VSF JT-NM Phase 2 Report]](#biblio_EBU-SMPTE-VSF_JT-NM_Phase2Report "Joint Task Force on Networked Media (JT-NM) Phase 2 Report- Reference Architecture").

Source
:   An abstract concept that represents the primary origin of a Flow or set of Flows, as defined in [[EBU-SMPTE-VSF JT-NM Phase 2 Report]](#biblio_EBU-SMPTE-VSF_JT-NM_Phase2Report "Joint Task Force on Networked Media (JT-NM) Phase 2 Report- Reference Architecture").

# 4 Symbols and Abbreviations

ACSE
:   Association Control Service Element

API
:   Application Programming Interface

CT
:   Computed Tomography

DICOM
:   Digital Imaging and Communications in Medicine

DICOM-RTV
:   DICOM Real-Time Video

DIMSE
:   DICOM Message Service Element

HIS
:   Hospital Information System

HTTP
:   Hyper-Text Transfer Protocol

HTTPS
:   Hyper-Text Transfer Protocol Secure

JIRA
:   Japan Medical Imaging and Radiological Systems Industries Association

OSI
:   Open Systems Interconnection

PACS
:   Picture Archiving and Communication Systems

PTP
:   Precision Time Protocol

REST
:   Representational State Transfer

RESTful
:   A RESTful Web service is a Web service implemented using REST architecture and HTTP (see <http://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf>)

RIS
:   Radiology Information System

RTP
:   Real-Time Transport Protocol

SMPTE
:   Society of Motion Picture and Television Engineers

STOW-RS
:   STore Over the Web by RESTful Services

TCP/IP
:   Transmission Control Protocol/Internet Protocol

WADO-RS
:   Web Access to DICOM Objects by RESTful Services

WADO-URI
:   Web Access to DICOM Objects by URI

# 5 The DICOM Communication Model

The DICOM Standard facilitates interoperability of devices claiming conformance. In
 particular, it:

* Addresses the semantics of Commands and associated data. For devices to interact,
 there must be standards on how devices are expected to react to Commands and associated
 data, not just the information that is to be moved between devices.
* Addresses the semantics of file services, file formats and information directories
 necessary for off-line communication.
* Is explicit in defining the conformance requirements of implementations of the
 Standard. In particular, a conformance statement must specify enough information to
 determine the functions for which interoperability can be expected with another device
 claiming conformance.
* Facilitates operation in a networked environment.
* Is structured to accommodate the introduction of new services, thus facilitating
 support for future medical imaging applications.
* Makes use of existing international standards wherever applicable, and itself
 conforms to established documentation guidelines for international standards.

[Figure 5-1](#figure_5-1 "Figure 5-1. General Communication Model") presents the general communication model of the Standard, which spans both
 network (on-line) and media storage interchange (off-line) communication. Applications may
 utilize any of the following transport mechanisms:

* the DICOM Message Service and Upper Layer Service, which provides independence from specific physical networking communication support and protocols such as TCP/IP.
* the DICOM Web Service API and HTTP Service, which allows use of common hypertext and associated protocols for transport of DICOM services.
* the Basic DICOM File Service, which provides access to Storage Media independently from specific media storage formats and file structures.
* DICOM Real-Time Communication, which provides real-time transport of DICOM metadata based on SMPTE and RTP.

![General Communication Model](figures/PS3.1_5-1.svg)**Figure 5-1. General Communication Model**

  

# 6 Overview of The Content of The DICOM Standard

## 6.1 Document Structure

DICOM consists of the following parts:

* PS3.1: Introduction and Overview (this document)
* [PS3.2: Conformance](part02.html#PS3.2)
* [PS3.3: Information Object Definitions](part03.html#PS3.3)
* [PS3.4: Service Class Specifications](part04.html#PS3.4)
* [PS3.5: Data Structures and Encoding](part05.html#PS3.5)
* [PS3.6: Data Dictionary](part06.html#PS3.6)
* [PS3.7: Message Exchange](part07.html#PS3.7)
* [PS3.8: Network Communication Support for Message Exchange](part08.html#PS3.8)
* PS3.9: Retired
* [PS3.10: Media Storage and File Format for Media Interchange](part10.html#PS3.10)
* [PS3.11: Media Storage Application Profiles](part11.html#PS3.11)
* [PS3.12: Formats and Physical Media](part12.html#PS3.12)
* PS3.13: Retired
* [PS3.14: Grayscale Standard Display Function](part14.html#PS3.14)
* [PS3.15: Security and System Management Profiles](part15.html#PS3.15)
* [PS3.16: Content Mapping Resource](part16.html#PS3.16)
* [PS3.17: Explanatory Information](part17.html#PS3.17)
* [PS3.18: Web Services](part18.html#PS3.18)
* [PS3.19: Application Hosting](part19.html#PS3.19)
* [PS3.20: Imaging Reports using HL7 Clinical Document Architecture](part20.html#PS3.20)
* [PS3.21: Transformations between DICOM and other Representations](part21.html#PS3.21)
* [PS3.22: Real-Time Communication (DICOM-RTV)](part22.html#PS3.22)

These parts of the Standard are related but independent documents. A brief description
 of each Part is provided in this section.

## 6.2 PS3.2: Conformance

[PS3.2](part02.html#PS3.2) of the DICOM Standard defines principles that implementations claiming
 conformance to the Standard shall follow:

* Conformance requirements. [PS3.2](part02.html#PS3.2) specifies the general requirements that must be
 met by any implementation claiming conformance. It references the conformance sections
 of other parts of the Standard.
* Conformance Statement. [PS3.2](part02.html#PS3.2) defines the structure of a Conformance Statement. It
 specifies the information that must be present in a Conformance Statement. It
 references the Conformance Statement sections of other parts of the Standard.

[PS3.2](part02.html#PS3.2) does not specify a testing/validation procedure to assess an implementation's
 conformance to the Standard.

[Figure 6.2-1](#figure_6.2-1 "Figure 6.2-1. Construction Process for a Network Conformance Claim") and [Figure 6.2-2](#figure_6.2-2 "Figure 6.2-2. Construction Process for a Media Conformance Claim") depict the construction process for a Conformance Statement for
 both network communication and media exchange. A Conformance Statement consists of the
 following parts:

* Set of Information Objects that is recognized by this implementation
* Set of Service Classes that this implementation supports
* Set of communications protocols or physical media that this implementation
 supports
* Set of security measures that this implementation supports.

![Construction Process for a Network Conformance Claim](figures/PS3.1_6.2-1.svg)**Figure 6.2-1. Construction Process for a Network Conformance Claim**

  

![Construction Process for a Media Conformance Claim](figures/PS3.1_6.2-2.svg)**Figure 6.2-2. Construction Process for a Media Conformance Claim**

  

## 6.3 PS3.3: Information Object Definitions

[PS3.3](part03.html#PS3.3) of the DICOM Standard specifies a number of Information Object Classes that
 provide an abstract definition of real-world entities applicable to communication of digital
 medical images and related information (e.g., waveforms, structured reports, radiation
 therapy dose, etc.). Each Information Object Class definition consists of a description of
 its purpose and the Attributes that define it. An Information Object Class does not include
 the values for the Attributes that comprise its definition.

Two types of Information Object Classes are defined: normalized and composite.

Normalized Information Object Classes include only those Attributes inherent in the
 real-world entity represented. For example the study Information Object Class, which is
 defined as normalized, contains study date and study time Attributes because they are
 inherent in an actual study. Patient name, however, is not an Attribute of the study
 Information Object Class because it is inherent in the patient on which the study was
 performed and not the study itself.

Composite Information Object Classes may additionally include Attributes that are
 related to but not inherent in the real-world entity. For example, the Computed Tomography
 Image Information Object Class, which is defined as composite, contains both Attributes that are inherent in the image (e.g., image date) and Attributes that are related to but
 not inherent in the image (e.g., patient name). Composite Information Object Classes provide
 a structured framework for expressing the communication requirements of images where image
 data and related data needs to be closely associated.

To simplify the Information Object Class definitions, the Attributes of each Information
 Object Class are partitioned with similar Attributes being grouped together. These groupings
 of Attributes are specified as independent modules and may be reused by other Composite
 Information Object Classes.

[PS3.3](part03.html#PS3.3) defines a model of the Real World along with the corresponding Information Model
 that is reflected in the Information Object Definitions. Future editions of this Standard
 may extend this set of Information Objects to support new functionality.

To represent an occurrence of a real-world entity, an Information Object Instance is
 created, which includes values for the Attributes of the Information Object Class. The
 Attribute values of this Information Object Instance may change over time to accurately
 reflect the changing state of the entity that it represents. This is accomplished by
 performing different basic operations upon the Information Object Instance to render a
 specific set of services defined as a Service Class. These Service Classes are defined in [PS3.4](part04.html#PS3.4) of the Standard.

## 6.4 PS3.4: Service Class Specifications

[PS3.4](part04.html#PS3.4) of the DICOM Standard defines a number of Service Classes. A Service Class
 associates one or more Information Objects with one or more Commands to be performed upon
 these objects. Service Class Specifications state requirements for Command Elements and how
 resulting Commands are applied to Information Objects. Service Class Specifications state
 requirements for both providers and users of communications services.

[PS3.4](part04.html#PS3.4) of the DICOM Standard defines the characteristics shared by all Service Classes,
 and how a Conformance Statement to an individual Service Class is structured. It contains a
 number of normative annexes that describe individual Service Classes in detail.

Examples of Service Classes include the following:

* Storage Service Class
* Query/Retrieve Service Class
* Basic Worklist Management Service Class
* Print Management Service Class.

[PS3.4](part04.html#PS3.4) defines the operations performed upon the Information Objects defined in [PS3.3](part03.html#PS3.3). [PS3.7](part07.html#PS3.7) defines the Commands and protocols for using the Commands to accomplish the
 operations and notifications described in [PS3.4](part04.html#PS3.4).

## 6.5 PS3.5: Data Structure and Semantics

[PS3.5](part05.html#PS3.5) of the DICOM Standard specifies how DICOM applications construct and encode the
 Data Set information resulting from the use of the Information Objects and Services Classes
 defined in [PS3.3](part03.html#PS3.3) and [PS3.4](part04.html#PS3.4) of the DICOM Standard. The support of a number of standard
 image compression techniques (e.g., JPEG lossless and lossy) is specified.

[PS3.5](part05.html#PS3.5) addresses the encoding rules necessary to construct a Data Stream to be conveyed
 in a Message as specified in [PS3.7](part07.html#PS3.7) of the DICOM Standard. This Data Stream is produced from
 the collection of Data Elements making up the Data Set.

[PS3.5](part05.html#PS3.5) also defines the semantics of a number of generic functions that are common to
 many Information Objects. [PS3.5](part05.html#PS3.5) defines the encoding rules for international character sets
 used within DICOM.

## 6.6 PS3.6: Data Dictionary

[PS3.6](part06.html#PS3.6) of the DICOM Standard is the centralized registry that defines the collection of
 all DICOM Data Elements available to represent information, along with elements utilized for
 interchangeable media encoding and a list of uniquely identified items that are assigned by
 DICOM.

For each element, [PS3.6](part06.html#PS3.6) specifies:

* its unique tag, which consists of a group and element number,
* its name,
* its value representation (character string, integer, etc),
* its value multiplicity (how many values per attribute),
* whether it is retired.

For each uniquely identified item, [PS3.6](part06.html#PS3.6) specifies:

* its unique value, which is numeric with multiple components separated by decimal
 points and limited to 64 characters,
* its name,
* its type, either Information Object Class, definition of encoding for data
 transfer, or certain well known Information Object Instances,
* in which Part of the DICOM Standard it is defined.

## 6.7 PS3.7: Message Exchange

[PS3.7](part07.html#PS3.7) of the DICOM Standard specifies both the service and protocol used by an
 application in a medical imaging environment to exchange Messages over the communications
 support services defined in [PS3.8](part08.html#PS3.8). A Message is composed of a Command Stream defined in [PS3.7](part07.html#PS3.7) followed by an optional Data Stream as defined in [PS3.5](part05.html#PS3.5).

[PS3.7](part07.html#PS3.7) specifies:

* the operations and notifications (DIMSE Services) made available to Service
 Classes defined in [PS3.4](part04.html#PS3.4),
* rules to establish and terminate associations provided by the communications
 support specified in [PS3.8](part08.html#PS3.8), and the impact on outstanding transactions,
* rules that govern the exchange of Command requests and responses,
* encoding rules necessary to construct Command Streams and Messages.

## 6.8 PS3.8: Network Communication Support For Message Exchange

[PS3.8](part08.html#PS3.8) of the DICOM Standard specifies the communication services and the upper layer
 protocols necessary to support, in a networked environment, communication between DICOM
 applications as specified in [PS3.3](part03.html#PS3.3), [PS3.4](part04.html#PS3.4), [PS3.5](part05.html#PS3.5), [PS3.6](part06.html#PS3.6), and [PS3.7](part07.html#PS3.7). These communication
 services and protocols ensure that communication between DICOM applications is performed in
 an efficient and coordinated manner across the network.

The communication services specified in [PS3.8](part08.html#PS3.8) are a proper subset of the services
 offered by the OSI Presentation Service (ISO 8822) and of the OSI Association Control
 Service Element (ACSE) (ISO 8649). They are referred to as the Upper Layer Service, which
 allows peer applications to establish associations, transfer messages and terminate
 associations.

This definition of the Upper Layer Service specifies the use of the DICOM Upper Layer
 Protocol in conjunction with TCP/IP transport protocols.

The TCP/IP communication protocol specified by [PS3.8](part08.html#PS3.8) is a general purpose communication
 protocol not specific to the DICOM Standard. [Figure 5-1](#figure_5-1 "Figure 5-1. General Communication Model") shows this protocol stack.

## 6.9 PS3.9: Retired (formerly Point-to-point Communication Support For Message
 Exchange)

PS3.9 of the DICOM Standard previously specified the services and protocols used for
 point-to-point communications in a manner compatible with ACR-NEMA 2.0. It has been
 retired.

## 6.10 PS3.10 Media Storage and File Format for Media Interchange

[PS3.10](part10.html#PS3.10) of the DICOM Standard specifies a general model for the storage of medical
 imaging information on removable media (see [Figure 6.10-1](#figure_6.10-1 "Figure 6.10-1. DICOM Communication Model for Media Interchange")). The purpose of this Part is to
 provide a framework allowing the interchange of various types of medical images and related
 information on a broad range of physical storage media.

### Note

See [Figure 5-1](#figure_5-1 "Figure 5-1. General Communication Model") for understanding how the media interchange model relates to the
 network model.

[PS3.10](part10.html#PS3.10) specifies:

* a layered model for the storage of medical images and related information on
 storage media. This model introduces the concept of media storage application
 profiles, which specify application specific subsets of the DICOM Standard to which a
 media storage implementation may claim conformance. Such a conformance applies only to
 the writing, reading and updating of the content of storage media.
* a DICOM file format supporting the encapsulation of any Information Object;
* a secure DICOM file format supporting the encapsulation of a DICOM file format in
 a cryptographic envelope;
* a DICOM file service providing independence from the underlying media format and
 physical media.

[PS3.10](part10.html#PS3.10) defines various media storage concepts:

* the method to identify a set of files on a single medium;
* the method for naming a DICOM file within a specific file system.

![DICOM Communication Model for Media Interchange](figures/PS3.1_6.10-1.svg)**Figure 6.10-1. DICOM Communication Model for Media Interchange**

  

## 6.11 PS3.11: Media Storage Application Profiles

[PS3.11](part11.html#PS3.11) of the DICOM Standard specifies application specific subsets of the DICOM
 Standard to which an implementation may claim conformance. These application specific
 subsets will be referred to as Media Storage Application Profiles in this section. Such a Conformance
 Statement applies to the interoperable interchange of medical images and related information
 on storage media for specific clinical uses. It follows the framework, defined in [PS3.10](part10.html#PS3.10),
 for the interchange of various types of information on storage media.

A Media Storage Application Profile annex is organized into the following major parts:

* The name of the Media Storage Application Profile, or the list of Media Storage Application Profiles grouped
 in a related class
* A description of the clinical context of the Media Storage Application Profile
* The definition of the media storage Service Class with the device roles for the
 Media Storage Application Profile and associated options
* Informative section describing the operational requirements of the Application
 Profile
* Specification of the Information Object Classes and associated Information Objects
 supported and the encoding to be used for the data transfer
* The selection of media formats and physical media to be used
* Other parameters that need to be specified to ensure interoperable media
 interchange
* Security parameters that select the cryptographic techniques to be used with
 Secure Media Storage Application Profiles

The structure of DICOM and the design of the Media Storage Application Profile mechanism is such that
 extension to additional Information Object Classes and the new exchange media is
 straightforward.

### Note

[Figure 6.11-1](#figure_6.11-1 "Figure 6.11-1. Relationship Between a Media Storage Application Profile and Parts of DICOM") shows how individual aspects of an Application profile map to the
 various parts of the DICOM Standard.

![Relationship Between a Media Storage Application Profile and Parts of DICOM](figures/PS3.1_6.11-1.svg)**Figure 6.11-1. Relationship Between a Media Storage Application Profile and Parts of DICOM**

  

## 6.12 PS3.12: Storage Functions and Media Formats For Data Interchange

[PS3.12](part12.html#PS3.12) of the DICOM Standard facilitates the interchange of information between
 applications in medical environments by specifying:

* A structure for describing the relationship between the media storage model and a
 specific physical media and media format.
* Specific physical media characteristics and associated media formats.

## 6.13 PS3.13: Retired (formerly Print Management Point-to-point Communication
 Support)

PS3.13 previously specified the services and protocols used for point-to-point
 communication of print management services. It has been retired.

## 6.14 PS3.14: Grayscale Standard Display Function

[PS3.14](part14.html#PS3.14) specifies a standardized display function for consistent display of grayscale
 images. This function provides methods for calibrating a particular display system for the
 purpose of presenting images consistently on different display media (e.g., monitors and
 printers).

The chosen display function is based on human visual perception. Human eye contrast
 sensitivity is distinctly non-linear within the luminance range of display devices. This
 Standard uses Barten's model of the human visual system.

## 6.15 PS3.15: Security and System Management Profiles

[PS3.15](part15.html#PS3.15) of the DICOM Standard specifies security and system management profiles to which
 implementations may claim conformance. Security and system management profiles are defined
 by referencing externally developed standard protocols, such as DHCP, LDAP, TLS and ISCL.
 Security protocols may use security techniques like public keys and "smart cards". Data
 encryption can use various standardized data encryption schemes.

This Part does not address issues of security policies. The Standard only provides
 mechanisms that can be used to implement security policies with regard to the interchange of
 DICOM objects. It is the local administrator's responsibility to establish appropriate
 security policies.

## 6.16 PS3.16: Content Mapping Resource

[PS3.16](part16.html#PS3.16) of the DICOM Standard specifies:

* templates for structuring documents as DICOM Information Objects
* sets of coded terms for use in Information Objects
* a lexicon of terms defined and maintained by DICOM
* country specific translations of coded terms

## 6.17 PS3.17: Explanatory Information

[PS3.17](part17.html#PS3.17) of the DICOM Standard specifies:

* informative and normative annexes containing explanatory information

## 6.18 PS3.18: Web Services

[PS3.18](part18.html#PS3.18) of the DICOM Standard specifies the means whereby Web Services can be used for
 retrieving or storing a DICOM object.

Requests that retrieve data specify the media type (format) of the response body.
 Requests that store data specify the media type of the request body.

The HTTP requests as defined within this Standard are sufficient for the HTTP server to
 act as a DICOM SCU (Service Class User) to retrieve or store the requested objects from an
 appropriate DICOM SCP (Service Class Provider) using baseline DICOM functionality as defined
 in [PS3.4](part04.html#PS3.4) and [PS3.7](part07.html#PS3.7), which is to say that the HTTP server can act as a proxy for the DICOM
 SCP.

## 6.19 PS3.19: Application Hosting

[PS3.19](part19.html#PS3.19) of the DICOM Standard specifies an Application Programming Interface (API) to a
 DICOM based medical computing system into which programs written to that standardized
 interface can "plug-in" (see [Figure 6.19-1](#figure_6.19-1 "Figure 6.19-1. Interface Between a Hosted Application and a Hosting System")). A Hosting System implementer only needs to create the standardized API once to support
 a wide variety of add-on Hosted Applications.

![Interface Between a Hosted Application and a Hosting System](figures/PS3.1_6.19-1.svg)**Figure 6.19-1. Interface Between a Hosted Application and a Hosting System**

  

In the traditional "plug-in" model, the "plug-in" is dedicated to a particular host
 system (e.g., a web browsing program), and might not run under other host systems (e.g.,
 other web browsing programs). [PS3.19](part19.html#PS3.19) defines an API that may be implemented by any Hosting
 System. A "plug-in" Hosted Application written to the API would be able run in any
 environment provided by a Hosting System that implements that API (see [Figure 6.19-2](#figure_6.19-2 "Figure 6.19-2. Illustration of Platform Independence via the Hosted Application")).

![Illustration of Platform Independence via the Hosted Application](figures/PS3.1_6.19-2.svg)**Figure 6.19-2. Illustration of Platform Independence via the Hosted Application**

  

[PS3.19](part19.html#PS3.19) specifies both the interactions and the Application Programming Interfaces (API)
 between Hosting Systems and Hosted Applications. [PS3.19](part19.html#PS3.19) also defines the data models that
 are used by the API.

## 6.20 PS3.20: Imaging Reports using HL7 Clinical Document Architecture

[PS3.20](part20.html#PS3.20) of the DICOM Standard specifies templates for the encoding of imaging reports using the HL7 Clinical Document Architecture Release 2 (CDA R2, or simply CDA) Standard. Within this scope are clinical procedure reports for specialties that use imaging for screening, diagnostic, or therapeutic purposes.

[PS3.20](part20.html#PS3.20) constitutes an implementation guide for CDA, and is harmonized with the approach to standardized templates for CDA implementation guides developed by HL7. It also provides Business Names for data elements that link data in user terminology, e.g., collected by a report authoring application, to specific CDA encoded elements.

As an implementation guide for imaging reports, particular attention is given to the use and reference of data collected in imaging procedures as explicit evidence within reports. This data includes images, waveforms, measurements, annotations, and other analytic results managed as DICOM SOP Instances. Specifically, this Part includes a specification for transformation into CDA documents of DICOM Structured Report instances that represent imaging reports.

## 6.21 PS3.21: Transformations between DICOM and other Representations

[PS3.21](part21.html#PS3.21) of the DICOM Standard specifies the transformations between DICOM and other representations of the same information. Within its scope are transformations to and from the NCI Annotation and Image Markup format.

## 6.22 PS3.22: Real-Time Communication (DICOM-RTV)

[PS3.22](part22.html#PS3.22) of the DICOM Standard specifies an [[SMPTE ST 2110-10]](#biblio_SMPTE_ST2110-10 "Professional Media over IP Networks: System Timing and Definitions")based service for the real-time transport of DICOM metadata. It provides a mechanism for the transport of DICOM metadata associated with a video or an audio flow based on the [[SMPTE ST 2110-20]](#biblio_SMPTE_ST2110-20 "Professional Media over IP Networks: Uncompressed Active Video")and [[SMPTE ST 2110-30]](#biblio_SMPTE_ST2110-30 "Professional Media over IP Networks: PCM Digital Audio"), respectively.

# 7 Referencing The DICOM Standard

Under the procedures of the DICOM Standards Committee, the Standard is in constant
 revision. Supplements and corrections to the Standard are balloted and approved several times
 a year. Each change when approved as Final Text immediately goes into effect. At intervals,
 all of the approved Final Text changes are consolidated into a published edition of the
 Standard, identified by year of publication, but such publication is only a convenience to the
 user; the Standard is officially changed when each change is approved.

Conformance to the DICOM Standard is through specified SOP Classes using DIMSE messages (see [PS3.4](part04.html#PS3.4)), Web Services (see [PS3.18](part18.html#PS3.18)), media interchange (see [Annex I “Media Storage Service Class (Normative)” in PS3.4](part04.html#chapter_I) and [PS3.10](part10.html#PS3.10)), or the hosted application API (see [PS3.19](part19.html#PS3.19)). Additional conformance claims may be made to Profiles
 (see [PS3.11](part11.html#PS3.11) and [PS3.15](part15.html#PS3.15)). Once such a unit of conformance is
 specified in the Standard, all changes thereto are forward and backward compatible (except in
 rare cases where the original specification was non-interoperable, or conflicted with another
 standard). Conformance requirements and conformance claims are therefore referenced to the
 name and/or identifier of the feature, and never referenced to an edition of the Standard.
 Generally, the only appropriate reference to a particular edition of the Standard is to
 identify a retired feature (see [Section 1.4.2 Continuous Maintenance](#sect_1.4.2 "1.4.2 Continuous Maintenance")).

The following citation form is preferred for general references to the Standard, without
 specification of date of edition, when specific conformance requirements are not
 invoked:

NEMA PS3 / ISO 12052, Digital Imaging and Communications in Medicine (DICOM) Standard,
 National Electrical Manufacturers Association, Rosslyn, VA, USA (available free at <http://www.dicomstandard.org/>)

The requirements of this section do not override the requirement to provide a DICOM Conformance Statement as described in [PS3.2](part02.html#PS3.2).

The following forms are preferred for references to units of conformance to the
 Standard when they are made outside the context of a DICOM Conformance Statement (e.g., in customer requirements):

* “… conformant to the DICOM <name> SOP Class for network exchange [as a Service Class <User | Provider>], as specified in DICOM [PS3.4](part04.html#PS3.4): Service Class Specifications.”
* “… conformant to the DICOM <name> SOP Class for media exchange [as a File Set <Creator | Updater | Reader>], as specified in DICOM [PS3.4](part04.html#PS3.4): Service Class Specifications.”
* “… conformant to the DICOM <name> Web Service [as <an Origin-server | a User-agent>] [for the <name> SOP Class], as specified in DICOM [PS3.18](part18.html#PS3.18): Web Services.”
* “… conformant to DICOM Application Hosting [as a <Hosting System | Hosted Application>] for the <name> SOP Class, as specified in DICOM [PS3.19](part19.html#PS3.19): Application Hosting.”
* “… conformant to the DICOM <identifier> Media Storage Application Profile [as a File Set <Creator | Updater | Reader>] [for the <name> SOP Class], as specified in DICOM [PS3.11](part11.html#PS3.11): Media Storage Application Profiles.”
* “… conformant to the DICOM <name> Profile, as specified in DICOM [PS3.15](part15.html#PS3.15): Security and System Management Profiles.”

### Note

1. Some Media Storage Application Profiles and Web Services may fully specify the information objects exchanged,
 while others may require explicit specification of SOP Classes in the references.
2. Examples:

	* “The modality shall be conformant to the DICOM CT Image Storage and MR Image Storage SOP Classes
	 for network exchange as a Service Class User, as specified in DICOM [PS3.4](part04.html#PS3.4): Service Class Specifications.”
	* “The workstation shall be conformant to the DICOM STD-XA1K-DVD Media Storage Application Profile as a File Set Reader,
	 as specified in DICOM [PS3.11](part11.html#PS3.11): Media Storage Application Profiles.”
	* “The PACS shall be conformant to the DICOM WADO-RS and STOW-RS Web Services as an Origin-server for the SOP Classes listed in Table X,
	 as specified in DICOM [PS3.18](part18.html#PS3.18): Web Services.”
3. Such references are not permitted in lieu of a Conformance Statement for a product.
 For example, a product that reads or creates DICOM interchange media is required to have a Conformance Statement
 (as described in [PS3.2](part02.html#PS3.2))
 that enumerates the Media Storage Application Profiles it implements.
 A statement in some other format, or a document that describes that a product supports recording of files of a particular SOP Class defined in [PS3.4](part04.html#PS3.4),
 is not sufficient as an alternative to a Conformance Statement.

Reference may be made to other features of the Standard, but these shall not be construed
 as DICOM conformance requirements (although they may be conformance requirements for non-DICOM
 implementation guides or regulations). Following are some examples:

* “… SOP Instances in accordance with the <name> Information Object Definition, as
 specified in DICOM [PS3.3](part03.html#PS3.3): Information Object Definitions.”
* “… Structured Reporting SOP Instances using DICOM Template ID <number and name>, as
 specified in DICOM [PS3.16](part16.html#PS3.16): Content Mapping Resource.”
* “… HL7 CDA instances using Template ID <identifier and name>, as specified in DICOM [PS3.20](part20.html#PS3.20): Imaging Reports using HL7 Clinical Document Architecture.”
* “… using the <name> Transfer Syntax, as specified in DICOM [PS3.5](part05.html#PS3.5): Data Structure and
 Semantics.”

### Note

For example, products producing or receiving SR documents must conform to a SOP Class, such as Enhanced SR;
 such products may also cite use of Template ID 5200 Echocardiography Procedure Report, but that is not a formal DICOM Conformance assertion.
 However, a non-DICOM implementation guide, such as the IHE Echocardiography Workflow Profile, may require use of that Template,
 and an implementation may describe its use of specific Templates in its Conformance Statement.

Since changes to the Standard shall not be cited prior to adoption as Final Text, and
 since after adoption they are formally part of the Standard, there should be no citations to
 supplements or correction items for the purpose of describing conformance. Reference to such
 change documents may be made for describing the historical development of the DICOM
 Standard.

