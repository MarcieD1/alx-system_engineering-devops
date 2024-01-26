# 0x09. Web infrastructure design

## Overview

This project is broken up into sections to design a web infrastructure, creating diagrams, and explaining components. Each section is outlined below.

## Tasks

### Task 0: Simple Web Stack

#### Web Infrastructure Diagram:
![Web Infrastructure Diagram](https://lucid.app/lucidchart/b412fac2-22d3-44f8-b3c9-cd5331d5baba/edit?viewport_loc=-1880%2C-786%2C3312%2C1572%2C0_0&invitationId=inv_8403d157-cbfd-43e9-9a4e-a10cf3936571)

#### Explanation:
- **User Access:** A user initiates access to the website.
- **Internet Cloud:** Represents the broader internet infrastructure.
  
#### Issues with the Infrastructure:
- **SPOF (Single Point of Failure):** The entire system depends on a single server, creating a vulnerability.
- **Downtime during Maintenance:** Performing maintenance requires restarting the web server, resulting in downtime.

### Task 1: Distributed Web Infrastructure

#### Explanation:
- **Addition of Elements:** Each additional element serves a specific purpose in enhancing the infrastructure.
- **Distribution Algorithm:** Load balancer configured with [algorithm] for distributing traffic.

#### Issues with the Infrastructure:
- **SPOF:** Identify single points of failure.
- **Security Issues:** No firewall, no HTTPS.
- **No Monitoring:** Lack of monitoring for system health.

### Task 2: Secured and Monitored Web Infrastructure

#### Whiteboard Diagram:

#### Explanation:
- **Addition of Elements:** Firewalls, SSL certificate, and monitoring clients added for security and monitoring.
- **Firewalls:** Added for network security.
- **HTTPS Traffic:** Implemented for secure communication.

#### Issues with the Infrastructure:
- **SSL Termination at Load Balancer Level:** Identified as an issue.
- **Single MySQL Server for Writes:** Recognized as a potential problem.
- **Uniform Server Components:** May pose a problem for diverse workload scenarios.

## General Requirements

- A README.md file is mandatory at the root of the project folder.
- Each task includes a whiteboard diagram and an explanation.
- Screenshot links are uploaded to [image hosting service].
- The project will be manually reviewed.

## Submission

- Push the answer file to GitHub.
- Insert the GitHub file link into the URL box.

## Review Process

- The project will be whiteboarded in front of a mentor, staff, or student.
- No computers or notes will be allowed during the whiteboarding session.

## Time Limit

- 30 minutes for the exercise.
- Points will be awarded based on meeting specified requirements.

## Caution
- Focus on answering what is asked.
- Avoid unnecessary details unless requested.

