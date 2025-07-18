# odoo-runner

A simple command-line tool to manage Odoo projects using a **pew-managed virtual environment**.

## 📦 Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/phuctranfxvn/odoo-runner.git
```

## ❌ Uninstallation

To remove the tool:

```bash
pip uninstall odoo-runner
```

## 🚀 Usage

### Virtual Environment
- Create a virtual environment with the same name as the project folder

### Start Odoo

```bash
odoorunner start
```

### Start Odoo in Debug Mode (port `5678`)

```bash
odoorunner debug
```

### Upgrade Odoo Modules

```bash
odoorunner upgrade -d <db_name> -m <module1,module2,...>
```

Replace `<db_name>` with your database name and `<module1,module2,...>` with a comma-separated list of modules to upgrade.

---

## 📁 Project Structure

This CLI is designed to be used inside a [pew](https://github.com/berdario/pew)-managed virtualenv containing an Odoo project, structured as follows:

```
<project_root>/
│
├── odoo/                             # Odoo core (source code)
│
├── addons/
│   ├── custom_3rd_party_addons_1/    # 3rd party modules (OCA, ...)
│   │   ├── module_a/
│   │   ├── module_b/
│   ├── custom_3rd_party_addons_2/
│   │   ├── module_c/
│   │   ├── module_d/
│   ...
│
├── project/                          # Customized modules for project
│   ├── project_module_1/
│   ├── project_module_2/
│   ├── project_module_3/
│
├── config/
    ├── local.conf (or dev.conf)

```

#### Notes:
- You don't need to specify the addons_path in the .conf file, the script will automatically prepare it for you.
- 

## 🛠 Requirements

- Python 3.7+
- `pew` for managing virtual environments
- `odoo-bin` available in your Odoo project path
