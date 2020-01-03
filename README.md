MicroPython and C code used for making the TTGO T-Display (ESP32 board with 135x240 LCD display) run MicroPython. In particular, it has the example code for LCD work.

You need to use the C code in to_565.c (and `imagemagick`) to compile a PNG into BGR565 byte format. Compile the code like this:

`gcc to_565.c`

Convert PNG images like this:

`convert indexs.png -depth 8 rgb:- | ./a.out > file.bgr565`
