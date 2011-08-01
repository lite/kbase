QEMU ARM system emulation using Ubuntu

This section describes how to boot Ubuntu Linux for the ARM architecture using QEMU.

Prerequisites

    sudo aptitude install qemu-kvm-extras debootstrap rootstock

Obtaining a kernel

    wget http://ports.ubuntu.com/ubuntu-ports/dists/lucid/main/installer-armel/current/images/versatile/netboot/vmlinuz

Creating the root fs

One of the easiest ways to obtain an armel rootfs is using a small shell script called rootstock. It creates an empty fs image using dd and mkfs.ext3. Then the image gets mounted via the loop device and debootstrap is used to fetch and extract the armel distro packages onto the image. It chroots into the image and uses a statically linked qemu to configure the debs.

    rootstock -f myarmhost -l dli -p dli --seed ubuntu-minimal,build-essential,openssh-server --keepimage

The resulting image file is called qemu-armel-*.img.

Boot the system using QEMU

    qemu-system-arm -M versatilepb -cpu cortex-a8 -m 256 -kernel ./vmlinuz -hda qemu-armel-*.img -append "root=/dev/sda mem=256M devtmpfs.mount=0 rw init=/sbin/init"

Thanks:
http://www.ailis.de/~k/archives/19-ARM-cross-compiling-howto.html
