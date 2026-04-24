module demux(
    input a, b, c,
    input e,
    output d0, d1, d2, d3, d4, d5, d6, d7);
    
logic d0i, d1i, d2i, d3i, d4i, d5i, d6i, d7i;

decoder de (
    .a,
    .b,
    .c,
    .d0(d0i),
    .d1(d1i),
    .d2(d2i),
    .d3(d3i),
    .d4(d4i),
    .d5(d5i),
    .d6(d6i),
    .d7(d7i)
);


assign d0 = d0i & e;
assign d1 = d1i & e;
assign d2 = d2i & e;
assign d3 = d3i & e;
assign d4 = d4i & e;
assign d5 = d5i & e;
assign d6 = d6i & e;
assign d7 = d7i & e;

//and and_0 (d0, e, d0);
//and and_1 (d1, e, d1);
//and and_2 (d2, e, d2);
//and and_3 (d3, e, d3);
//and and_4 (d4, e, d4);
//and and_5 (d5, e, d5);
//and and_6 (d6, e, d6);
//and and_7 (d7, e, d7);

endmodule