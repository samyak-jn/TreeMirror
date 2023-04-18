Name:           treemirror
Version:        0.1.1
Release:        1%{?dist}
Summary:        A program to mirror the directory structure of a source directory to a destination directory

License:        MIT
URL:            https://github.com/samyak-jn/treemirror
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
TreeMirror is a program to mirror the directory structure of a source directory to a destination directory.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}


%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/treemirror

%changelog
* Mon Apr 17 2023 Samyak Jain <samyak.jn11@gmail.com> - 1.0-1
- Initial package for TreeMirror
