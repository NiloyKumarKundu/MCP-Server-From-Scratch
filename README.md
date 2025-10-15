# MCP Server From Scratch

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.12.4-green.svg)](https://gofastmcp.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive learning repository for building Model Context Protocol (MCP) servers from the ground up. Master MCP development through 8 progressive examples, from basic local servers to advanced cloud-integrated applications with real-world expense tracking.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd MCP-Server-From-Scratch
uv sync

# Run your first MCP server
uv run fastmcp run "1.Basic_Local_Server.py"

# Debug with MCP Inspector
uv run fastmcp dev "2.Expense_Tracker_Local_Server.py"
```

## 📚 Learning Path

This repository follows a **progressive 8-step learning approach**:

### **Phase 1: Foundations**

- **[1.Basic_Local_Server.py](1.Basic_Local_Server.py)** - Simple local MCP server with basic tools
- **[2.Expense_Tracker_Local_Server.py](2.Expense_Tracker_Local_Server.py)** - Local server with SQLite database
- **[3.Basic_Remote_Server.py](3.Basic_Remote_Server.py)** - HTTP-based remote server

### **Phase 2: Real-World Applications**

- **[4.Expense_Tracker_Remote_Server.py](4.Expense_Tracker_Remote_Server.py)** - Async remote server with advanced features
- **[5.Use_Custom_Server_Free_in_Claude-Desktop.py](5.Use_Custom_Server_Free_in_Claude-Desktop.py)** - Claude Desktop integration

### **Phase 3: Advanced Patterns**

- **[6.Client_Using_Config_File.py](6.Client_Using_Config_File.py)** - MCP client with configuration
- **[7.Build_Expense_Tracker_SSE_Server.py](7.Build_Expense_Tracker_SSE_Server.py)** - Server-Sent Events transport
- **[8.Build_Expense_Tracker_SSE_Client.py](8.Build_Expense_Tracker_SSE_Client.py)** - SSE client implementation

## 🛠️ What You'll Learn

### **Core MCP Concepts**

- **Local vs Remote Servers** - STDIO vs HTTP transport protocols
- **Tools & Resources** - Building interactive MCP capabilities
- **Async Operations** - Modern Python async/await patterns
- **Database Integration** - SQLite with aiosqlite for async operations

### **Advanced Features**

- **Server-Sent Events (SSE)** - Real-time communication patterns
- **Cloud Integration** - FastMCP Cloud proxy connections
- **Claude Desktop** - Custom server integration
- **Client Development** - Building MCP clients with memory and conversation

### **Real-World Skills**

- **Expense Tracking System** - Complete CRUD application
- **Category Management** - JSON-based configuration system
- **Error Handling** - Production-ready exception management
- **Configuration Management** - Flexible server setup

## 📁 Repository Structure

```
MCP-Server-From-Scratch/
├── 📄 1.Basic_Local_Server.py              # Basic MCP server with dice & math tools
├── 📄 2.Expense_Tracker_Local_Server.py     # Local expense tracker with SQLite
├── 📄 3.Basic_Remote_Server.py             # HTTP remote server with resources
├── 📄 4.Expense_Tracker_Remote_Server.py  # Async remote expense tracker
├── 📄 5.Use_Custom_Server_Free_in_Claude-Desktop.py  # Claude Desktop integration
├── 📄 6.Client_Using_Config_File.py        # MCP client with Groq LLM
├── 📄 7.Build_Expense_Tracker_SSE_Server.py  # SSE transport server
├── 📄 8.Build_Expense_Tracker_SSE_Client.py  # SSE client implementation
├── 📁 config/
│   └── expense_tracker.json                # MCP client configuration
├── 📄 categories.json                      # Expense categories configuration
├── 📄 expense.db                          # SQLite database (auto-generated)
├── 📄 pyproject.toml                      # Project dependencies
└── 📄 README.md                           # This documentation
```

## 🚀 Development Workflow

### **Running MCP Servers**

```bash
# Local server (STDIO transport)
uv run fastmcp run "1.Basic_Local_Server.py"

# Remote server (HTTP transport)
uv run fastmcp run "3.Basic_Remote_Server.py"

# Debug with MCP Inspector
uv run fastmcp dev "2.Expense_Tracker_Local_Server.py"
```

### **Installing in Claude Desktop**

```bash
# Install custom server in Claude Desktop
uv run fastmcp install claude-desktop "5.Use_Custom_Server_Free_in_Claude-Desktop.py"

# Restart Claude Desktop to load the server
```

### **Running SSE Server-Client**

```bash
# Terminal 1: Start SSE server
uv run "7.Build_Expense_Tracker_SSE_Server.py"

# Terminal 2: Run SSE client
uv run "8.Build_Expense_Tracker_SSE_Client.py"
```

## 💡 Key Features

### **Expense Tracker Application**

- **Complete CRUD Operations** - Add, list, and summarize expenses
- **Date Range Filtering** - Query expenses by date ranges
- **Category Management** - Hierarchical expense categories
- **Async Database Operations** - High-performance SQLite with aiosqlite
- **Error Handling** - Robust exception management

### **Transport Protocols**

- **STDIO** - Local communication (Claude Desktop)
- **HTTP** - Remote server access
- **SSE** - Real-time server-sent events

### **Cloud Integration**

- **FastMCP Cloud** - Deploy servers to the cloud
- **Proxy Connections** - Connect to remote MCP servers
- **Claude Desktop** - Seamless integration with Claude

## 🛠️ Technologies

- **[FastMCP](https://gofastmcp.com)** - Modern Python MCP framework
- **[SQLite](https://sqlite.org)** - Embedded database with aiosqlite
- **[Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)** - Real-time communication
- **[Claude Desktop](https://claude.ai/desktop)** - AI assistant integration
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package manager

## 📖 Usage Examples

### **Basic Server Tools**

```python
# Dice rolling
roll_dice(n_dice=3)  # Returns: [4, 2, 6]

# Math operations
add(15.5, 4.3)  # Returns: 19.8
```

### **Expense Tracking**

```python
# Add expense
add_expense(
    date="2025-01-15",
    amount=25.50,
    category="Food & Dining",
    subcategory="groceries",
    note="Weekly grocery shopping"
)

# List expenses
list_expenses("2025-01-01", "2025-01-31")

# Summarize by category
summarize("2025-01-01", "2025-01-31", category="Food & Dining")
```

## 🔧 Prerequisites

- **Python 3.8+** - Modern Python with async support
- **uv** - Fast Python package manager
- **Basic Python knowledge** - Functions, classes, async/await
- **Optional**: Claude Desktop for integration testing

## 🤝 Contributing

We welcome contributions! Please feel free to:

- 🐛 **Report bugs** - Help us improve the examples
- 💡 **Suggest features** - Propose new learning examples
- 📝 **Improve documentation** - Make the learning path clearer
- 🔧 **Submit pull requests** - Add your own MCP implementations

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

---

**🎯 Ready to master MCP development?** Start with `1.Basic_Local_Server.py` and progress through all 8 examples to become an MCP expert!

**📚 Learn more**: [FastMCP Documentation](https://gofastmcp.com) | [MCP Specification](https://modelcontextprotocol.io)
