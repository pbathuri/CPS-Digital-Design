module decoder( 
    input a, b, c,
    output d0, d1, d2, d3, d4, d5, d6, d7);
   
logic a_bar, b_bar, c_bar;

not not_1(a_bar, a);
not not_2(b_bar, b);
not not_3(c_bar, c);

and and_0(d0, a_bar, b_bar, c_bar   );
and and_1(d1, a_bar, b_bar, c       );
and and_2(d2, a_bar, b,     c_bar   );
and and_3(d3, a_bar, b,     c       );
and and_4(d4, a,     b_bar, c_bar   );
and and_5(d5, a,     b_bar, c       );
and and_6(d6, a,     b,     c_bar   );
and and_7(d7, a,     b,     c       );

endmodule