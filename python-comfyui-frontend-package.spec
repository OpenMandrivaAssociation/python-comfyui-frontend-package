Name:		python-comfyui-frontend-package
Version:	1.49.6
Release:	2
Summary:	Official web frontend for ComfyUI
License:	GPL-3.0
Group:		Development/Python
URL:		https://github.com/Comfy-Org/ComfyUI_frontend
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-frontend-package/comfyui_frontend_package-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

# setup.py defaults to 0.1.0 unless COMFYUI_FRONTEND_VERSION is set.
# There is no pyproject.toml, so %install re-runs setup.py without
# %build's environment and would record 0.1.0. Pin the real version.
%prep -a
sed -i 's/os.getenv("COMFYUI_FRONTEND_VERSION") or "0.1.0"/"%{version}"/' setup.py

%description
Prebuilt Vue web UI served by ComfyUI. Without this package ComfyUI
refuses to start.

%files
%doc README.md
%{py_sitedir}/comfyui_frontend_package
%{py_sitedir}/comfyui_frontend_package-*.*-info
