`timescale 1ns / 1ps

module top(
    input [15:0] sw,
    output [15:0] LED
);

demux d0 (
    .a(sw[0]),
    .b(sw[1]),
    .c(sw[2]),
    .e(sw[3]),
    .d0(LED[0]),
    .d1(LED[1]),
    .d2(LED[2]),
    .d3(LED[3]),
    .d4(LED[4]),
    .d5(LED[5]),
    .d6(LED[6]),
    .d7(LED[7])
);
    //assign LED[15:8] = 'h0;

endmodule