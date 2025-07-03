# odoo-cli

A simple command-line tool to manage Odoo projects using a **pew-managed virtual environment**.

## 📦 Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/phuctranfxvn/odoo-cli.git
```

## ❌ Uninstallation

To remove the tool:

```bash
pip uninstall odoo-cli
```

## 🚀 Usage

### Virtual Environment
- Create a virtual environment with the same name as the project folder

### Start Odoo

```bash
odoo start
```

### Start Odoo in Debug Mode (port `5678`)

```bash
odoo debug
```

### Upgrade Odoo Modules

```bash
odoo upgrade -d <db_name> -m <module1,module2,...>
```

Replace `<db_name>` with your database name and `<module1,module2,...>` with a comma-separated list of modules to upgrade.

---

## 📁 Project Structure

This CLI is designed to be used inside a [pew](https://github.com/berdario/pew)-managed virtualenv containing an Odoo project, structured as follows:

```
<project_root>/
│
├── odoo/
├── addons/
├── project/
├── config/local.conf
└── ...
```

## 🛠 Requirements

- Python 3.7+
- `pew` for managing virtual environments
- `odoo-bin` available in your Odoo project path
