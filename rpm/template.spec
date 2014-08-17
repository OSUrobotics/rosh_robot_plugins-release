Name:           ros-hydro-rosh-robot-plugins
Version:        1.0.2
Release:        0%{?dist}
Summary:        ROS rosh_robot_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosh_robot_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-rosh-common
Requires:       ros-hydro-rosh-geometry
Requires:       ros-hydro-rosh-robot
BuildRequires:  ros-hydro-catkin

%description
ROSH related packages. This is a temporary stack that is expected to go away
after the Diamondback release. For C Turtle and Diamondback it provides a
convenient way to install rosh until it is properly stabilized.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Aug 17 2014 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.2-0
- Autogenerated by Bloom

