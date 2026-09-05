Name:		python-comfyui-frontend-package
Version:	1.49.6
Release:	1
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

# setup.py reads this instead of the PyPI version
%build -p
export COMFYUI_FRONTEND_VERSION=%{version}

%description
Prebuilt Vue web UI served by ComfyUI. Without this package ComfyUI
refuses to start.

%files
%doc README.md
%{py_sitedir}/comfyui_frontend_package
%{py_sitedir}/comfyui_frontend_package-*.*-info
