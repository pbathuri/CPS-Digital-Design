module decoder_2_4(b, c, e, d0, d1, d2, d3);


wire b_bar, c_bar;

not not_1(b_bar, b);
not not_2(c_bar, c);

and and_0(d0, e, b_bar, c_bar);
and and_1(d1, e, b_bar, c);
and and_2(d2, e, b, c_bar);
and and_3(d3, e, b, c);


endmodule 