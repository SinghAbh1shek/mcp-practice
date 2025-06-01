
## 🔧 Install UV (if not already installed)

```bash
pip install uv
```

---

## 🚀 Sync Dependencies


```bash
uv sync
```

---

## 🧩 Add to Your MCP Client

Add this code to your MCP client (update the path):

```json
{
  "mcpServers": {
      "arthm": {
          "command": "uv",
          "args": [
              "--directory",
              "C:\\Users\\abhi0\\OneDrive\\Desktop\\MCP\\01_mcp",
              "run",
              "server.py"
          ]
      }
  }
}
```

---