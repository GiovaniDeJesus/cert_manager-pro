# Cert Monitor Pro

A Python tool for monitoring SSL certificate expiration dates and automating certificate management workflows.

## What Is This?

SSL certificates expire, and when they do, websites go down. This tool helps prevent those midnight emergencies by monitoring certificate expiry dates and (eventually) automating the renewal process.

I started with a bash script that did basic certificate checking, but realized Python would give me much more flexibility for adding features like web dashboards, automated renewals, and multi-cloud deployment support.

## Current Status (Week 1)

Right now, this is a command-line tool that checks individual SSL certificates and tells you how much time is left before they expire.

## Architecture Overview

The tool follows a complete certificate management lifecycle:

graph TD
    A[Infrastructure Discovery] --> B[Certificate Monitoring]
    
    B --> C{Certificate Status}
    C -->|Valid| D[Schedule Next Check]
    C -->|Warning 30 days| E[Send Alert]
    C -->|Critical 7 days| F[Urgent Alert]
    C -->|Expired| G[Emergency Alert]
    
    E --> H[Renewal Decision]
    F --> H
    G --> H
    
    H --> I{Renewal Method}
    I -->|Let's Encrypt| J[Automated Renewal]
    I -->|Commercial CA| K[Manual Process]
    I -->|Internal CA| L[Custom Workflow]
    
    J --> M[Certificate Obtained]
    K --> M
    L --> M
    
    M --> N{Deployment Targets}
    N -->|AWS| O[CloudFront/ALB]
    N -->|GCP| P[Load Balancer]
    N -->|Azure| Q[Application Gateway]
    N -->|On-Premise| R[Web Servers]
    N -->|CDN| S[Content Delivery]
    
    O --> T[Verify Deployment]
    P --> T
    Q --> T
    R --> T
    S --> T
    
    T --> U[Update Certificate Database]
    U --> V[Generate Compliance Report]
    V --> W[Archive Old Certificate]
    W --> D
    
    D --> B
    
    subgraph "Alert Channels"
        E --> E1[Email]
        F --> F1[Slack/Teams]
        G --> G1[PagerDuty/SMS]
        E --> E2[Dashboard]
        F --> E2
        G --> E2
    end
    
    subgraph "Tracking & Compliance"
        U --> U1[Certificate History]
        V --> V1[Audit Logs]
        W --> W1[Retention Policy]
        U1 --> U2[Expiry Trends]
        V1 --> V2[Compliance Status]
    end
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style J fill:#e8f5e8
    style T fill:#fff3e0
    style V fill:#fce4ec

This diagram shows the five core phases: Monitor → Alert → Renew → Deploy → Track, with the supporting systems for notifications and compliance.

### What Works

- Check any SSL certificate expiration date
- Handles common input mistakes (strips `https://`, trailing slashes, etc.)
- Robust error handling for network issues, DNS problems, and SSL errors
- Clean command-line interface
- Detects expired certificates

### Usage

```bash
python cert_checker.py google.com 443
# Output: 67 days, 12:48:30.976882

python cert_checker.py expired.badssl.com 443  
# Output: Error: SSL error for 'expired.badssl.com': certificate has expired

python cert_checker.py https://GITHUB.COM/ 443
# Output: 89 days, 3:22:15.123456
```

The tool handles various input formats and provides clear error messages when things go wrong.

## Development Process

This project follows a structured approach with weekly milestones. Each week's code is analyzed with SonarQube to maintain code quality and catch potential issues early. 

SonarQube analysis helps ensure the codebase stays maintainable as features are added, and provides objective metrics for code quality improvements.

## Roadmap

### Week 2: Multi-Domain Support (Next)
- Check multiple certificates at once
- Configuration file support (YAML)
- Tabular output with status indicators
- Enhanced command-line interface

### Week 3-4: Automation
- Scheduled monitoring
- Integration with Let's Encrypt for automatic renewal
- Email and webhook notifications
- Configuration management

### Week 5-6: Deployment & Upload
- Upload renewed certificates to cloud providers (AWS, GCP, Azure)
- SFTP and webhook deployment options
- Certificate deployment automation

### Week 7-8: Web Interface
- FastAPI-based dashboard
- REST API endpoints
- Certificate management interface
- Historical tracking and reporting

### Future Enhancements
- Support for commercial certificate authorities (DigiCert, Sectigo, etc)
- Team collaboration features
- Enterprise integrations
- Multi-tenant support

## The Big Picture

The goal is to build a comprehensive SSL certificate management platform that handles the entire lifecycle:

1. **Monitor** certificates across your infrastructure
2. **Alert** when certificates are approaching expiry
3. **Renew** certificates automatically where possible
4. **Deploy** renewed certificates to the right places
5. **Track** certificate history and compliance

Many companies struggle with certificate management across multiple domains, cloud providers, and teams. This tool aims to centralize that process while remaining flexible enough for different infrastructure setups.

## Technical Philosophy

- **Start simple, add complexity gradually** - Each week builds on the previous foundation
- **Code quality matters** - Regular SonarQube analysis ensures maintainable code
- **Real-world focus** - Built to solve actual SSL certificate pain points
- **Flexible architecture** - Designed to work with any hosting setup or cloud provider

## Requirements

- Python 3.7+
- No external dependencies (current version uses only built-in libraries)

## Contributing

This is primarily a learning project, but the code is structured to be maintainable and extensible. Each week's development includes comprehensive testing and code quality analysis.

## License

MIT License - See LICENSE file for details.

