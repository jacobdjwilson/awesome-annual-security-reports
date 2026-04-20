# Model Context Protocol: A View from the Trenches
## What Enterprise MCP Deployments Actually Look Like

**Organization:** ClutchSecurity  
**Year:** 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [The MCP Ecosystem: 2,200% Growth in 13 Months](#the-mcp-ecosystem-2200-growth-in-13-months)
- [In The Trenches: What We Found in Enterprise Deployments](#in-the-trenches-what-we-found-in-enterprise-deployments)
- [The Target Surface: 115 Services Exposed](#the-target-surface-115-services-exposed)
- [The Architecture Problem: Plaintext Credentials by Design](#the-architecture-problem-plaintext-credentials-by-design)
- [Speed, Scale & The Detection Gap](#speed-scale--the-detection-gap)
- [The Visibility Imperative](#the-visibility-imperative)
- [About Clutch Security](#about-clutch-security)

---

## Executive Summary

Clutch Security analyzed MCP server deployments across enterprise environments between October 2024 and November 2025, examining both the published ecosystem and real-world enterprise adoption patterns. The findings reveal silent, explosive adoption with total security blindness.

The bottom line: Your employees are installing arbitrary code from npm, GitHub, and PyPI—registries with no verification mechanisms—and feeding your most critical non-human identities to that code. You have no visibility into this. The problem is accelerating.

### What we found
- **15.28%** of enterprise employees run at least one local MCP server (1,528 per 10,000 employees).
- **3,056** total server installations in a typical 10,000-person organization (average 2 per user, maximum 10+).
- **86%** local vs 14% remote architecture—developers choose local servers despite remote alternatives being available.
- **95%** run on employee endpoints where security tools have no visibility.
- **38%** are unofficial implementations—unvetted code from unknown authors with full credential access.
- **5%** run in production CI pipelines, cloud workloads, and automated systems.
- **3%** of published servers contain valid, hardcoded credentials embedded in their source code.
- **115** distinct enterprise services exposed.

![Distribution sources chart showing 46% Packages (npm), 31% Repositories (GitHub), 16% Packages (PyPI), and 7% Marketplaces]

---

## The MCP Ecosystem: 2,200% Growth in 13 Months

Model Context Protocol launched in late 2024 as a standard for connecting AI assistants to external tools and data sources. The adoption curve wasn't gradual; it was explosive.

October 2024: 3 published MCP servers. November 2025: 6,878 published MCP servers. That's 2,200% growth in 13 months.

![Monthly MCP server publications chart showing growth from 3 in Oct 2024 to 6,878 in Nov 2025]

Developers discovered they could extend Claude, ChatGPT, and other AI assistants with specialized capabilities through single-command installation. The value proposition was immediate: `npm install @modelcontextprotocol/server-github` and you have GitHub automation inside your AI workflow.

Some developers used `npx -y [package-name]` to run MCP servers on-demand. The `-y` flag auto-accepts all installation prompts. This "I'm feeling lucky" approach means arbitrary code execution from unknown authors with a single command, no vetting, and no verification.

---

## In The Trenches: What We Found in Enterprise Deployments

Our analysis of enterprise MCP deployments reveals adoption at scale.

- **15.28% of enterprise employees are running at least one local MCP server.** In a 10,000-employee company, that translates to 1,528 employees with MCP servers and 3,056 total installations.
- **86% of MCP users adopt local servers versus 14% using remote alternatives.** Local servers run on endpoints with full credential access. Remote servers run in vendor-controlled environments where credentials never leave secure infrastructure.
- **38% of deployed servers are unofficial implementations.** Not vendor-published, not verified, and not reviewed. In a 10,000-person organization, that's 1,161 instances of unvetted code with credential access.
- **5% of servers run in production environments.** CI pipelines, cloud workloads, Kubernetes pods, and other automated systems. These are more dangerous: persistent, privileged, and automated.

---

## The Target Surface: 115 Services Exposed

MCP servers connect to the infrastructure that runs your business using the non-human identities that provide programmatic access to those systems. Our analysis identified 115 distinct services with active MCP server connections:

- **Generic utility servers (20.5%)**: Tools like memory management and filesystem access.
- **Browser automation (18.6%)**: Playwright and Puppeteer.
- **Atlassian (12.3%)**: Jira and Confluence integration.
- **Cloud Infrastructure**: AWS (5.0%), Docker (4.7%), Microsoft (0.8%), Google Cloud (0.5%), and Cloudflare (0.3%).
- **DevOps and Source Control**: GitHub (3.6%), Terraform (3.3%), Notion (3.3%), Git (3.3%), and GitLab (2.5%).
- **Data platforms**: Postgres (1.2%), Snowflake (0.4%), and others.

---

## The Architecture Problem: Plaintext Credentials by Design

MCP servers operate in two modes:
1. **Remote servers**: Run in vendor-controlled environments. The trust boundary holds.
2. **Local servers**: Run on developer endpoints as arbitrary processes. This is where 86% of adoption concentrates.

The local deployment model creates direct credential access. The MCP server runs as a program with developer privileges and reads configuration files where credentials are stored in plaintext.

> Here's the actual `.env.example` file from an unofficial Salesforce MCP server published on GitHub:
> ```
> SF_LOGIN_URL=https://login.salesforce.com
> SF_USERNAME=your-username@example.com
> SF_PASSWORD=your-password
> SF_SECURITY_TOKEN=your-security-token
> ```

---

## Speed, Scale & The Detection Gap

### Attack Timeline: 60 Seconds
1. **Publish**: Attacker publishes an MCP server to npm with a compelling name.
2. **Install**: Developer runs `npm install -g [package]` or `npx -y [package]`.
3. **Configure**: Developer provides credentials to the tool.
4. **Exfiltrate**: Server loads the config, initializes, and makes a background HTTPS POST to an attacker-controlled endpoint.

### Publisher Credential Exposure
Our analysis found that 3% of servers contain valid, hardcoded credentials in their source code—including Anthropic Claude keys, AWS access keys, and GitHub tokens.

---

## The Visibility Imperative

These numbers represent non-human identity exposure at scale. MCP servers provide real productivity value, and developers adopt them because they work. Prohibition will fail.

What needs to change is security visibility and governance. Security teams need answers to:
- What MCP servers exist in our environment?
- Which are official versus unofficial?
- What credentials are they configured to access?
- What network connections are they making?

Without this visibility, the alternative is blind trust. The MCP ecosystem will continue growing, and the visibility requirement is clear.

---

## About Clutch Security

Clutch Security provides the industry's most comprehensive platform for non-human identity security, including the MCP servers and AI agents that use those identities. The platform delivers complete visibility across cloud environments, SaaS applications, on-premises infrastructure, code repositories, CI/CD pipelines, and vaults.

![Summary infographic showing distribution percentages and service categories]

**Securing Non-Human Identities. Everywhere.**  
clutch.security