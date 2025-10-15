# MCP Server From Scratch

A comprehensive learning repository for understanding and implementing Model Context Protocol (MCP) servers from the ground up. This repository provides all the essential files, examples, and documentation needed to master MCP server development using the **FastMCP library**.

## Table of Contents

- [MCP Server From Scratch](#mcp-server-from-scratch)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [What You'll Learn](#what-youll-learn)
  - [Prerequisites](#prerequisites)
  - [Quick Start](#quick-start)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Run Your First MCP Server](#3-run-your-first-mcp-server)
  - [Development Workflow](#development-workflow)
    - [Debugging with MCP Inspector](#debugging-with-mcp-inspector)
    - [Running MCP Servers](#running-mcp-servers)
    - [Installing in Claude Desktop](#installing-in-claude-desktop)
  - [Repository Structure](#repository-structure)
  - [Learning Path](#learning-path)
  - [Technologies](#technologies)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

This repository is designed for developers who want to understand MCP servers from the fundamentals. Each example builds upon the previous one, providing a progressive learning path from basic concepts to advanced implementations.

### What You'll Learn

- **Local MCP Server Development**: Create and configure MCP servers that run locally
- **Remote MCP Server Implementation**: Build and deploy MCP servers for remote access
- **Custom MCP Client Creation**: Develop clients to interact with MCP servers
- **Best Practices**: Follow industry standards for MCP server development
- **Real-world Examples**: Work with practical examples demonstrating various MCP patterns

## Prerequisites

- Python 3.8 or higher
- `uv` package manager
- Basic understanding of Python and web protocols
- Familiarity with JSON-RPC concepts (helpful but not required)

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MCP-Server-From-Scratch
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Run Your First MCP Server

```bash
uv run fastmcp run "1. Basic Local Server.py"
```

## Development Workflow

### Debugging with MCP Inspector

Use the MCP Inspector for debugging and development:

```bash
uv run fastmcp dev <filename>
```

### Running MCP Servers

Start your MCP server in production mode:

```bash
uv run fastmcp run <filename>
```

### Installing in Claude Desktop

Install your MCP server in Claude Desktop for integration:

```bash
uv run fastmcp install claude-desktop <filename>
```

## Repository Structure

```
MCP-Server-From-Scratch/
├── 1. Basic Local Server.py    # Basic MCP server implementation
├── pyproject.toml              # Project configuration
├── uv.lock                     # Dependency lock file
├── README.md                   # This file
└── LICENSE                     # License information
```

## Learning Path

This repository follows a progressive learning approach:

1. **Basic Local Server** - Start with a simple local MCP server
2. **Advanced Features** - Add tools, resources, and prompts
3. **Remote Implementation** - Deploy servers for remote access
4. **Client Development** - Create custom MCP clients
5. **Best Practices** - Learn production-ready patterns

## Technologies

- **FastMCP Library**: Python-based framework for MCP development
- **Model Context Protocol (MCP)**: Standard protocol for AI model interactions
- **JSON-RPC**: Communication protocol for client-server interactions
- **Python**: Primary development language
- **uv**: Modern Python package manager

## Contributing

We welcome contributions! Please feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

---

**Ready to start building MCP servers?** Begin with the `1. Basic Local Server.py` file and follow the progressive examples to master MCP server development.
