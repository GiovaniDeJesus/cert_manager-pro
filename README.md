# Cert Manager Pro

A Python tool for SSL certificate managering and automated renewal management.

## What is Cert Manager Pro?

Cert Manager Pro monitors SSL certificate expiration dates and automates certificate renewal processes to prevent unexpected website outages. Keep your certificates up to date without manual intervention.

## Quick Start

```bash
# Check a certificate
python cert_checker.py google.com

# Example output:
# Certificate for google.com expires in 92 days
```

## Requirements

- Python 3.7 or higher
- Built-in Python libraries only (no external dependencies)

## Current Features

- Check SSL certificate expiration for any domain
- Command-line interface
- Zero external dependencies

## Development Roadmap

### Phase 1: Core Managering (Week 1-2)
- [x] Basic certificate expiry checking
- [ ] Error handling improvements
- [ ] Better output formatting
- [ ] Multiple domain support

### Phase 2: Automation (Week 3-4)
- [ ] Scheduled certificate monitoring
- [ ] Certificate renewal with Let's Encrypt/Certbot
- [ ] Configuration file support
- [ ] Email and webhook notifications

### Phase 3: Upload & Deploy (Week 5-6)
- [ ] Upload renewed certificates to:
  - AWS S3/CloudFront
  - Google Cloud Storage  
  - Azure Blob Storage
  - SFTP servers
  - Custom webhook endpoints

### Phase 4: Web Interface (Week 7-8)
- [ ] FastAPI web dashboard
- [ ] REST API endpoints
- [ ] Certificate management interface
- [ ] Historical monitoring data

### Phase 5: Enterprise Features (Future)
- [ ] Multi-user support
- [ ] Team collaboration
- [ ] Audit logs
- [ ] Wildcard certificate support
- [ ] Custom certificate authorities

## Usage

### Basic Certificate Check
```bash
python cert_checker.py example.com
```

### Planned Features
```bash
# Manager multiple domains
python cert-manager-pro.py --config domains.yml

# Check and renew certificates
python cert-manager-pro.py --renew --upload s3://my-bucket/certs/

# Run web dashboard
python cert-manager-pro.py --web --port 8080
```

## Project Structure

```
cert-manager-pro/
├── cert_checker.py          # Current: Basic certificate checker
├── cert_renewer.py          # Week 3: Renewal logic
├── uploaders/               # Week 5: Upload handlers
│   ├── aws.py
│   ├── gcp.py
│   └── sftp.py
├── web/                     # Week 7: Web interface
│   ├── app.py
│   └── templates/
├── config/
│   └── domains.example.yml
├── tests/
├── requirements.txt
├── LICENSE
└── README.md
```

## Current Development Status

**Week 1 Progress:**
- [x] Core SSL certificate checking functionality
- [x] Command-line interface
- [ ] Error handling improvements
- [ ] Output formatting enhancements
- [ ] Multiple domain support

**Currently Working:**
- Check SSL certificate expiry for any domain
- Basic command-line usage

**In Development:**
- Improved error messages
- User-friendly output format
- Edge case handling

## Contributing

Contributions are welcome! This project follows standard open source practices.

### Development Setup
```bash
git clone https://github.com/GiovaniDeJesus/cert-manager-pro
cd cert-manager-pro
python cert_checker.py google.com
```

### Guidelines
- Write clean, readable code
- Add tests for new features
- Update documentation
- Follow PEP 8 style guidelines

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Project Goals

Cert Manager Pro is designed to become a comprehensive SSL certificate management solution:
- **Simple** - Easy setup for individuals and small teams
- **Powerful** - Enterprise-grade features for larger organizations  
- **Reliable** - Automated monitoring prevents certificate expiration
- **Flexible** - Compatible with any hosting setup or cloud provider

## Support

- Star this repository if you find it useful
- Open an issue for questions or bug reports
- Contributions and feedback are welcome