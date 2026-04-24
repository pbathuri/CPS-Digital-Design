module demux_3_8( 
    input a, b, c, e, 
    output d0, d1, d2, d3, d4, d5, d6, d7);
   
logic a_bar, b_bar, c_bar;

not not_1(a_bar, a);
not not_2(b_bar, b);
not not_3(c_bar, c);

and and_0(d0, e, a_bar, b_bar, c_bar);
and and_1(d1, e, a_bar, b_bar, c);
and and_2(d2, e, a_bar, b, c_bar);
and and_3(d3, e, a_bar, b, c);
and and_4(d4, e, a, b_bar, c_bar);
and and_5(d5, e, a, b_bar, c);
and and_6(d6, e, a, b, c_bar);
and and_7(d7, e, a, b, c);

wire wire1; //declare a wire
assign wire1 = 'h1; // assign to 1
wire wire2 = 'h1; //declare and assign

endmodule